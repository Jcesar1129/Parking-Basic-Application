from dataclasses import dataclass


# Class from which the vehicles will get the general characteristics
@dataclass
class Auto:
    plate: str
    brand: str
    model: str
    year: str
    marchamo: bool

    def to_string(self):
        pass
