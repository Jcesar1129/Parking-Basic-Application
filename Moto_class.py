from dataclasses import dataclass
from Auto_class import Auto

# Specific class for the motorcycle vehicles.
@dataclass
class Motorcycle(Auto):
    sidecar: bool
    cant_helmets: int = 0

    def to_string(self):
        print("-------------- MOTORCYCLE INFORMATION --------------")
        print(f"Plate: {self.plate}")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

        if self.sidecar:
            print("--->The motorcycle has a side car available<---")
        else:
            print("--->A sidecar is not available<---")

        if self.marchamo:
            print("--->Marchamo has been paid<---")
        else:
            print("--->Marchamo needs to be paid<---")
