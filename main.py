import json
import sys

from input import INPUT

from employee import Employee
from vehicle import Vehicle
from manager import WorkloadManager

def run(vehicles_to_process):
    """
    Calculate total amount of parking fees for each vehicle
    assigned to the appropriate employee
    """
    employee_A = Employee('A', 0.11)
    employee_B = Employee('B', 0.15)


    # process vehicle data
    vehicles = [
        Vehicle(vehicle_data['licencePlate'], vehicle_data['size'], vehicle_data['fuel'])
        for vehicle_data in vehicles_to_process
    ]

    # sort according to total amount paid for parking, ascending
    sorted_vehicles = sorted(vehicles, key=lambda v: v.calculate_total_parking_cost())
    vehicles_count = len(sorted_vehicles)

    # assign to processing employee
    # where workload is split equally
    # and maximising profit of the parking system
    # (vehicle paid fees - employee fees)
    for idx in range(0, int(vehicles_count/2)):
        sorted_vehicles[idx].assign_to_employee(employee_B)
    for idx in range(int(vehicles_count/2), vehicles_count):
        sorted_vehicles[idx].assign_to_employee(employee_A)

    for v in sorted_vehicles:
        print(v.to_json())

run(INPUT)

