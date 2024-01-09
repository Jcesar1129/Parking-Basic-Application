from dataclasses import dataclass

# Garage functions and methods.

@dataclass
class Garage:
    cant_max_spaces: int
    vehicles: list
    used_spaces: int = 0

    # Se pueden juntar add_car y add_motorcycle usando isintance(value,class)
    def add_car(self, car):
        if self.used_spaces < self.cant_max_spaces - 1:
            self.vehicles.append(car)
            self.used_spaces += 2
            print("Car added successfully")
        else:
            print("Theres no space for a car in the garage")

    def add_motorcycle(self, moto):
        if self.used_spaces < self.cant_max_spaces:
            self.vehicles.append(moto)
            self.used_spaces += 1
            print("Motorcycle added successfully")
        else:
            print("Theres no space for a motorcycle in the garage")

    def delete_vehicle(self, plate):  # debe quitar 2 si se elemina un carro
        found = False
        if not self.used_spaces:
            print("Theres no vehicles stored yet")
        else:
            for vehicle in self.vehicles:
                if vehicle.plate == plate:
                    found = True
                    self.vehicles.remove(vehicle)
                    print("Vehicle eliminated successfully")
                    self.used_spaces -= 1

    def print_vehicle_info(self, plate):
        print("Information about the vehicle: (If empty none was found under that plate)")
        for vehicle in self.vehicles:
            if vehicle.plate == plate:
                vehicle.to_string()

    def plate_exists(self, plate):
        exists = False
        for vehicle in self.vehicles:
            if vehicle.plate == plate:
                exists = True
        return exists

    def to_string(self):
        if not self.used_spaces:
            print("Theres no stored vehicles.")
        else:
            print("------------ VEHICLE LIST ------------")
            print(f"Current used space: {self.cant_max_spaces - self.used_spaces}")
            print(f"Available spaces:{self.cant_max_spaces - self.used_spaces} ")
            for vehicle in self.vehicles:
                print(f"-{vehicle.model}, plate: {vehicle.plate}")
