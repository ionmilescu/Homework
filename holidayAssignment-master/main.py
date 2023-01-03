from data_access.cars_access import add_car, get_car, remove_car
from data_access.customers_access import add_customer, get_customer, remove_customer
from data_access.reservations_access import add_reservation, get_reservations_for_car, get_reservations_for_date, remove_reservation

car = {
    "make": make,
    "model": model,
    "vin": vin,
    "plate": plate,
    "color": color,
    "year": year
}
add_car(car)


make = input("Enter the make of the car: ")
model = input("Enter the model of the car: ")
vin = input("Enter the VIN of the car: ")
plate = input("Enter the plate number of the car: ")
color = input("Enter the color of the car: ")
year = input("Enter the year of production of the car: ")