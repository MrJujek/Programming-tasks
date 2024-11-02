class Car:
    def __init__(self, plate_number, color, type):
        self.plate_number = plate_number
        self.color = color
        self.type = type
        self.parked = False

    def park_in(self, parking):
        if self.parked == True:
            print(f'Already parked')
        else:
            if parking.add(self) == False:
                print(f'Cannot park, no free slots')
            else:
                self.parked = True

    def park_out(self, parking):
        if self.parked == True:
            self.parked = False
            parking.remove(self)

class Parking:
    def __init__(self):
        self.slots = 5
        self.free_slots = 5
        self.money = 0
        self.plate_numbers = {"normal": [], "truck": [], "motorbike": []}

    def add(self, vehicle: Car) -> bool:
        if self.free_slots > 0:
            self.free_slots -= 1
            # self.plate_numbers[vehicle.type].append(vehicle.plate_number)
            
            if not vehicle.plate_number in self.plate_numbers[vehicle.type]:
                self.plate_numbers[vehicle.type].append(vehicle.plate_number)

            return True
        else:
            return False
    
    def remove(self, vehicle: Car):
        if vehicle.plate_number in self.plate_numbers[vehicle.type]:
            # self.plate_numbers[vehicle.type].remove(vehicle.plate_number)
            self.free_slots += 1

            match vehicle.type:
                case "motorbike":
                    self.money += 5
                case "normal":
                    self.money += 10
                case "truck":
                    self.money += 30
            
            return True
        else:
            return False      

    def count_slots(self):
        print(f'Taken slots: {self.slots - self.free_slots}, free slots: {self.free_slots}')

    def count_money(self):
        print(f'Earned money: {self.money}')

    def show_cars(self):
        print(f'{self.plate_numbers}')
    
    def show_trucks(self):
        print(f'{self.plate_numbers["truck"]}')


def test():
    normal1 = Car("A1", "white", "normal")
    normal2 = Car("A2", "white", "normal")
    truck1 = Car("B1", "white", "truck")
    truck2 = Car("B2", "white", "truck")
    motorbike1 = Car("C1", "white", "motorbike")
    motorbike2 = Car("C2", "white", "motorbike")
    parking = Parking()

    # 1
    normal1.park_in(parking)
    # 2
    normal2.park_in(parking)
    # 3
    truck1.park_in(parking)
    # 4
    normal2.park_out(parking)
    # 5
    parking.count_slots()
    # 6
    normal2.park_in(parking)
    # 7
    truck2.park_in(parking)
    # 8
    motorbike1.park_in(parking)
    # 9
    parking.count_slots()
    parking.count_money()
    # 10
    motorbike2.park_in(parking)
    # 11
    normal1.park_out(parking)
    # 12
    motorbike2.park_in(parking)
    # 13
    parking.count_slots()
    parking.count_money()
    # 14
    normal1.park_out(parking)
    normal2.park_out(parking)
    truck1.park_out(parking)
    truck2.park_out(parking)
    motorbike1.park_out(parking)
    motorbike2.park_out(parking)
    # 15
    parking.count_slots()
    parking.count_money()
    # 16
    parking.show_cars()
    # 17
    parking.show_trucks()

test()