from dataclasses import dataclass
from Auto_class import Auto

# Specific class for the car vehicles.

@dataclass
class Car(Auto):
    polarized_windows: bool
    polarized_color: str = None

    def to_string(self):

        print("-------------- CAR INFORMATION -------------- ")
        print(f"Plate: {self.plate}")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        if self.polarized_windows:
            print(f"Polarized windows: {self.polarized_color}")

        if self.marchamo:
            print("--->Marchamo has been paid<---")
        else:
            print("--->Marchamo needs to be paid<---")
