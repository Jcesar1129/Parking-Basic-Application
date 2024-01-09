from Car_class import Car
from Moto_class import Motorcycle
from Parking_class import Garage
import os
import time

# Application menu's


def clear_console():
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')


def case_add_car():
    polarized_color = None
    plate = input("Type the car's plate: ")
    brand = input("Type the car's brand: ")
    model = input("Type the car's model: ")
    year = input("Type the car's year: ")
    marchamo = input("Is the marchamo up to date? (y/n) ")
    if marchamo == "y" or marchamo == "Y":
        marchamo = True
    else:
        marchamo = False
    polarized_windows = input("Are the windows polarized? (y/n)")
    if polarized_windows == "y" or polarized_windows == "Y":
        polarized_windows = True
        polarized_color = input("Which color?")
    else:
        polarized_windows = False

    car = Car(plate, brand, model, year, marchamo, polarized_windows, polarized_color)
    return car


def case_add_motorcycle():
    print("-------- ADDING A MOTORCYCLE --------\n")
    plate = input("Type the motorcycle's plate: ")
    brand = input("Type the motorcycle's brand: ")
    model = input("Type the motorcycle's model: ")
    year = input("Type the motorcycle's year: ")
    helmets = int(input("How many helmets are available? "))
    sidecar = input("Does the motorcycle has a sidecar? (y/n) ")
    if sidecar == "y" or "Y":
        sidecar = True
    else:
        sidecar = False
    marchamo = input("Is the marchamo up to date? (y/n) ")
    if marchamo == "y" or marchamo == "Y":
        marchamo = True
    else:
        marchamo = False

    moto = Motorcycle(plate, brand, model, year, marchamo, sidecar, helmets)
    return moto


def menu():

    flag = False
    try:
        print("---------- Welcome to the garage management app ----------")
        slots = int(input("Type the amount of slots available: "))

        if slots > 0:
            garage = Garage(slots, [])
            print("Garage created successfully, now loading the UI")
            clear_console()
        else:
            print("Invalid number, please try again")
            flag = True
    except ValueError:
        print("Invalid input")
        flag = True

    while not flag:
        print('''
        ---------- Main Menu ----------
        1. Register a new vehicle 
        2. Remove a vehicle
        3. Print a vehicle information
        4. Print all stored vehicles
        5. Leave (Current information will not be saved)
        ''')
        selected_case = input("Select an action: ")

        if selected_case == "1":
            os.system("cls")
            print('''
            1. Register a car
            2. Register a motorcycle
            3. Go back
            ''')
            op = input("Select an action: ")
            if op == "1":
                car = case_add_car()
                if garage.plate_exists(car.plate):
                    print("Theres a car with that plate already stored")
                    garage.print_vehicle_info(car.plate)
                else:
                    garage.add_car(car)
            elif op == "2":
                garage.add_motorcycle(case_add_motorcycle())
            else:
                print("Invalid option, please try again")
                clear_console()
            clear_console()
        elif selected_case == "2":
            plate = input("Type the plate of the vehicle that's being removed: ")
            garage.delete_vehicle(plate)
            clear_console()
        elif selected_case == "3":
            plate = input("Type the plate of the vehicle: ")
            garage.print_vehicle_info(plate)
            clear_console()
        elif selected_case == "4":
            garage.to_string()
            clear_console()
        elif selected_case == "5":
            print("Thank you for your preference!")
            flag = True
        else:
            print("Invalid option, please try again")
            clear_console()
