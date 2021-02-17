from unittest import TestCase

from employee import Employee
from fuel import Fuel
from vehicle import Vehicle


class TestVehicle(TestCase):
    def test_required_values(self):
        with self.assertRaises(TypeError):
            Vehicle('A')

        with self.assertRaises(TypeError):
            Vehicle('A', 'small')

        with self.assertRaises(AttributeError):
            Vehicle('A', 'small', 123)

        with self.assertRaises(AttributeError):
            Vehicle('A', 'small', 'test')

    def test_correctly_initialised(self):
        vehicle = Vehicle("A", "small", {"capacity": 70, "level": 0.10})
        self.assertEqual("A", vehicle.licence_plate)
        self.assertEqual("small", vehicle.size)
        self.assertEqual(70, vehicle.full_capacity)
        self.assertTrue(isinstance(vehicle.fuel, Fuel))
        self.assertIsNone(vehicle.employee)

    def test_to_string(self):
        vehicle = Vehicle("A", "small", {"capacity": 70, "level": 0.10})
        self.assertEqual("A", str(vehicle))

        vehicle = Vehicle("Vehicle B", "large", {"capacity": 70, "level": 0.10})
        self.assertEqual("Vehicle B", str(vehicle))

    def test_parking_fee(self):
        vehicle = Vehicle("A", "small", {"capacity": 70, "level": 0.10})
        self.assertEqual(25, vehicle.parking_fee)

        vehicle = Vehicle("B", "large", {"capacity": 70, "level": 0.15})
        self.assertEqual(35, vehicle.parking_fee)

    def test_needs_refueling(self):
        vehicle = Vehicle("A", "small", {"capacity": 70, "level": 0.10})
        self.assertTrue(vehicle.needs_refueling)

        vehicle = Vehicle("A", "small", {"capacity": 70, "level": 0.03})
        self.assertTrue(vehicle.needs_refueling)

        vehicle = Vehicle("B", "large", {"capacity": 70, "level": 0.15})
        self.assertFalse(vehicle.needs_refueling)

    def test_fuel_added(self):
        vehicle = Vehicle("A", "small", {"capacity": 70, "level": 0.10})
        self.assertEqual(
            63, # 90% to reach full capacity
            vehicle.fuel_added,
        )

        vehicle = Vehicle("A", "small", {"capacity": 70, "level": 0.01})
        self.assertEqual(
            69.3, # 99% to reach full capacity
            vehicle.fuel_added
        )

        vehicle = Vehicle("B", "large", {"capacity": 70, "level": 0.40})
        self.assertEqual(0, vehicle.fuel_added) # didn't need refueling

    def test_calculate_fuel_topup_liters(self):
        vehicle = Vehicle("A", "small", {"capacity": 70, "level": 0.10})
        self.assertEqual(
            63,  # 90% to reach full capacity
            vehicle.calculate_fuel_topup_liters(),
        )

        vehicle = Vehicle("A", "small", {"capacity": 70, "level": 0.01})
        self.assertEqual(
            69.3,  # 99% to reach full capacity
            vehicle.calculate_fuel_topup_liters()
        )

        vehicle = Vehicle("B", "large", {"capacity": 70, "level": 0.40})
        self.assertEqual(
            42,
            vehicle.calculate_fuel_topup_liters()
        )

    def test_calculate_total_parking_cost(self):
        vehicle = Vehicle("A", "small", {"capacity": 70, "level": 0.10})
        self.assertEqual(
            135.25, # refueled 63 liters (*1.75) + parking fee
            vehicle.calculate_total_parking_cost(),
        )

        vehicle = Vehicle("A", "large", {"capacity": 70, "level": 0.01})
        self.assertEqual(
            156.27499999999998, # refueled 69.3 liters (*1.75) + parking fee
            vehicle.calculate_total_parking_cost()
        )

        vehicle = Vehicle("B", "large", {"capacity": 70, "level": 0.40})
        self.assertEqual(
            35, # didn't need refueling, so just the parking fee
            vehicle.calculate_total_parking_cost()
        )

    def test_assign_to_employee(self):
        vehicle = Vehicle("A", "small", {"capacity": 70, "level": 0.10})
        employee = Employee('A', 0.15)

        vehicle.assign_to_employee(employee)
        self.assertEqual(employee, vehicle.employee)
