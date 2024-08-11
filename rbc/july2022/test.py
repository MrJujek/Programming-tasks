import time
from w1thermsensor import W1ThermSensor
from gpiozero import CPUTemperature
sensors = W1ThermSensor().get_available_sensors()
print(sensors)
#print(sensors[3].get_temperature())
print("\n")
while True:
    starttime = time.time()
    for sensor in sensors:
        starttime = time.time()
        print(f"Sensor {sensor.id} has a temperature of {sensor.get_temperature()} degrees Celsius")
#        print(time.time() - starttime)
#    print(time.time() - starttime)
    print("\n")
    cpu = CPUTemperature()
    temperature = cpu.temperature
    print(f"CPU has a temperature of {temperature} degrees Celsius")
    print("\n\n")
    time.sleep(1)

