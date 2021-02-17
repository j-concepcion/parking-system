import json

from typing import Dict
from typing import Union

from employee import Employee
from fuel import Fuel

SML = 'small'
LRG = 'large'

class Vehicle:
    def __init__(
        self,
        licence_plate: str,
        size: Union[SML, LRG],
        fuel: Dict[str, Union[int, float]],
    ) -> None:
        self.licence_plate = licence_plate
        self.size = size
        self.full_capacity = fuel.get("capacity")
        self.fuel = Fuel(fuel.get("level"))
        self.employee = None

    def __str__(self) -> str:
        return self.licence_plate

    def to_json(self):
        return json.dumps({
            "licencePlate": self.licence_plate,
            "employee": str(self.employee),
            "fuelAdded": str(round(self.fuel_added, 2)),
            "price": str(round(self.calculate_total_parking_cost(), 2))
        })

    @property
    def parking_fee(self) -> int:
        "Returns a flat-rate value according to vehicle size"
        if self.size == SML:
            return 25
        if self.size == LRG:
            return 35

    @property
    def needs_refueling(self) -> bool:
        "Returns true when fuel level is 10% or less"
        return self.fuel.fuel_percentage <= 10.0

    @property
    def fuel_added(self) -> Union[int, float]:
        return self.calculate_fuel_topup_liters() if self.needs_refueling else 0

    def calculate_fuel_topup_liters(self) -> float:
        "Calculate how much fuel (per litre) is needed to reach full capacity"
        return (1-self.fuel.current_level) * self.full_capacity


    def calculate_total_parking_cost(self) -> Union[int, float]:
        "Calculates total of the parking fee and fuel amount when refilled to full capacity"

        if self.needs_refueling:
            return self.parking_fee + (
                self.calculate_fuel_topup_liters() * self.fuel.price_per_litre
            )
        else:
            return self.parking_fee

    def assign_to_employee(self, employee: Employee) -> None:
        self.employee = employee

