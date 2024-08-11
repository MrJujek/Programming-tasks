from genericpath import exists
import sys
import os.path
from unicodedata import name
from w1thermsensor import W1ThermSensor
sys.path.append('../')
import time
#from time import time as militime## just for tests
import pandas as pd
import RPi.GPIO as GPIO
from datetime import datetime
from DFRobot_ADS1115 import ADS1115
from gpiozero import CPUTemperature
import threading

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

ADS1115_REG_CONFIG_PGA_6_144V        = 0x00 # 6.144V range = Gain 2/3
ADS1115_REG_CONFIG_PGA_4_096V        = 0x02 # 4.096V range = Gain 1
ADS1115_REG_CONFIG_PGA_2_048V        = 0x04 # 2.048V range = Gain 2 (default)
ADS1115_REG_CONFIG_PGA_1_024V        = 0x06 # 1.024V range = Gain 4
ADS1115_REG_CONFIG_PGA_0_512V        = 0x08 # 0.512V range = Gain 8
ADS1115_REG_CONFIG_PGA_0_256V        = 0x0A # 0.256V range = Gain 16
ads1115 = ADS1115()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.output(23, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)
GPIO.output(25, GPIO.HIGH)
GPIO.output(26, GPIO.HIGH)

testing = False
if testing:
    print("Testing enabled")

if not exists('./counter.txt'):
    with open('./counter.txt', 'w') as f:
        f.write('2,2,2,2')

sensors = W1ThermSensor().get_available_sensors()
counter = open("counter.txt", "r")
counter_list = list(counter.read().split(","))
counter.close()

connected_list = [0, 1, 2]

resistance = {0: [220_000, 2_200], 1: [220_000, 220], 2:[220_000, 2_200], 3:[0]}
ports = {0: 23, 1:24, 2:25, 3:26}
cycles_ratio = {0: 0.125, 1: 0.125, 2: 0.25, 3: 0}
minutes = {0: 120, 1: 120, 2: 120, 3: 0}
change_resistance = {0: 0, 1: 0, 2: 0, 3: 0}
sensors_dict = {0: sensors[2], 1: sensors[1], 2: sensors[3], 3: sensors[0]}
temperature_dict = {0: 0, 1: 0, 2: 0, 3: 0}

for i in change_resistance:
    change_resistance[i] = int(counter_list[i])

for item in connected_list:
    sleep_time = len(connected_list) + 1
    cycle_duration = minutes[item] * (60 / sleep_time) 
    if cycle_duration != 0:
        if change_resistance[item] <= int((1 - cycles_ratio[item]) * cycle_duration):
            GPIO.output(ports[item], GPIO.HIGH)
        elif change_resistance[item] > int((1 - cycles_ratio[item]) * cycle_duration) and change_resistance[item] != int(cycle_duration):
            GPIO.output(ports[item], GPIO.LOW)
        elif change_resistance[item] == int(cycle_duration):
            change_resistance[item] = 1

def createFiles():
    if testing:
        d = {'timestamp': [],'voltage0': [],'voltage1': [],'voltage2': [],'voltage3': [],'resistance0': [],'resistance1': [],'resistance2': [],'resistance3': [], 'CPUtemperature': [], 'temperature0': [], 'temperature1': [], 'temperature2': [], 'temperature3': []}
        pd.DataFrame(d).to_csv(f'./results_combined_testing.csv', index=False)
    else:
        for i in range (4):
            if not exists(f'./results_{i}.csv'): 
                d = {'timestamp': [], 'voltage': [],'resistance': [], 'CPUtemperature': [], 'temperature': []}
                pd.DataFrame(d).to_csv(f'./results_{i}.csv', index=False)
        if not exists(f'./results_combined.csv'): 
            d = {'timestamp': [],'voltage0': [],'voltage1': [],'voltage2': [],'voltage3': [],'resistance0': [],'resistance1': [],'resistance2': [],'resistance3': [], 'CPUtemperature': [], 'temperature0': [], 'temperature1': [], 'temperature2': [], 'temperature3': []}
            pd.DataFrame(d).to_csv(f'./results_combined.csv', index=False)

# def checkBatteries():
#     for i in range (4):
#         sum = 0
#         starttime = time.time()
#         for j in range (8):
#             sum += ads1115.read_voltage(i)['r']
#             time.sleep(0.125 - ((time.time() - starttime)))
#             starttime = time.time()
#         print(f"Port {i}, voltage {sum / 8}")
#         if sum / 8 > 25:
#             connected_list.append(i)
#     if len(connected_list) == 0:
#         print("No batteries connected")
#         quit()
#     print(f"There are {len(connected_list)} batteries connected")

def checkValues():
    global minutes
    global cycles_ratio
    sleep_time = len(connected_list) + 1
    for index in minutes:
        cycle_duration = minutes[index] * (60 / sleep_time)
        if cycles_ratio[index] * cycle_duration != int(cycles_ratio[index] * cycle_duration):
            x = int(round(cycles_ratio[index] * cycle_duration, 0))
            print(x)
            minutes[index] = (x / cycles_ratio[index]) / (60 / sleep_time)
    print(minutes)
    
def runTime():
    while True :
        global change_resistance
        #Set the IIC address
        ads1115.set_addr_ADS1115(0x48)
        #Sets the gain and input voltage range.
        ads1115.set_gain(ADS1115_REG_CONFIG_PGA_4_096V)
        starttime, starttime2 = time.time(), time.time()
        mean_voltage = {}
        for port in range(4):
            sum = 0
            if connected_list.count(port) == 1:
                starttime = time.perf_counter()
                for i in range (8):
                    sum += ads1115.read_voltage(port)['r']
                    time.sleep(0.125 - (time.perf_counter() - starttime)) #metoda zapewnienia stałej prędkości próbkowania
                    starttime = time.perf_counter()
            mean_voltage[port] = sum / 8
        cpu = CPUTemperature()
        temperature = cpu.temperature
        current_resistance = {}
        for port in range(4):
            if len(resistance[port]) > 1:
                current_resistance[port] = resistance[port][GPIO.input(ports[port])]
            else:
                current_resistance[port] = resistance[port][0]

        if not testing:
            for item in connected_list:
                d = {'timestamp': [(datetime.fromtimestamp((starttime2+starttime)/2)).strftime("%m/%d/%Y %H:%M:%S")],'voltage': [mean_voltage[item]],'resistance': [current_resistance[item]], 'CPUtemperature': [temperature], 'temperature': [temperature_dict[item]]}
                pd.DataFrame(d).to_csv(f'./results_{item}.csv', mode='a', header=False, index=False)

            d = {'timestamp': [(datetime.fromtimestamp((starttime2+starttime)/2)).strftime("%m/%d/%Y %H:%M:%S")],'voltage0': [mean_voltage[0]],'voltage1': [mean_voltage[1]],'voltage2': [mean_voltage[2]],'voltage3': [mean_voltage[3]],'resistance0': [current_resistance[0]],'resistance1': [current_resistance[1]],'resistance2': [current_resistance[2]],'resistance3': [current_resistance[3]], 'CPUtemperature': [temperature], 'temperature0': [temperature_dict[0]], 'temperature1': [temperature_dict[1]], 'temperature2': [temperature_dict[2]], 'temperature3': [temperature_dict[3]]}
            pd.DataFrame(d).to_csv('./results_combined.csv', mode='a', header=False, index=False)

        else:
            d = {'timestamp': [(datetime.fromtimestamp((starttime2+starttime)/2)).strftime("%m/%d/%Y %H:%M:%S")],'voltage0': [mean_voltage[0]],'voltage1': [mean_voltage[1]],'voltage2': [mean_voltage[2]],'voltage3': [mean_voltage[3]],'resistance0': [current_resistance[0]],'resistance1': [current_resistance[1]],'resistance2': [current_resistance[2]],'resistance3': [current_resistance[3]], 'CPUtemperature': [temperature], 'temperature0': [temperature_dict[0]], 'temperature1': [temperature_dict[1]], 'temperature2': [temperature_dict[2]], 'temperature3': [temperature_dict[3]]}
            pd.DataFrame(d).to_csv('./results_combined_testing.csv', mode='a', header=False, index=False)

        print(pd.DataFrame(d).to_string(index=False), '\n')
        sleep_time = len(connected_list) + 1
        for item in connected_list:
            cycle_duration = minutes[item] * (60 / sleep_time) 
            if cycle_duration != 0:
                if change_resistance[item] <= int((1 - cycles_ratio[item]) * cycle_duration):
                    GPIO.output(ports[item], GPIO.HIGH)
                elif change_resistance[item] > int((1 - cycles_ratio[item]) * cycle_duration) and change_resistance[item] != int(cycle_duration):
                    GPIO.output(ports[item], GPIO.LOW)
                elif change_resistance[item] == int(cycle_duration):
                    change_resistance[item] = 0

        for i in connected_list:
            change_resistance[i] += 1
        counter = open("counter.txt", "w")
        counter.write(','.join(map(str, list(change_resistance.values()))))
        time.sleep(sleep_time -(time.time()-starttime2) - 0.0009)       #empirical value

def getTemp():
    global temperature_dict
    while True:
        for i in temperature_dict:
            temperature_dict[i] = sensors_dict[i].get_temperature()
            time.sleep(1)

def setup():
    tempThread = threading.Thread(target=getTemp)
    tempThread.start()
    time.sleep(1)
    createFiles()
    # checkBatteries()
    checkValues()
    runTime()
            
if __name__ == "__main__":
    setup()
                                    
# #Made by Juliusz Stefański and fixed by Dawid Komęza & Julian Dworzycki 
