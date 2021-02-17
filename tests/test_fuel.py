from unittest import TestCase

from fuel import Fuel

class TestFuel(TestCase):
    def test_correctly_initialised(self):
        fuel = Fuel(0.55)
        self.assertEqual(0.55, fuel.current_level)
        self.assertEqual(1.75, fuel.price_per_litre)

    def test_to_string(self):
        fuel = Fuel(0.55)
        self.assertEqual("55%", str(fuel))

        fuel = Fuel(0.06)
        self.assertEqual("6%", str(fuel))

        fuel = Fuel(1.0)
        self.assertEqual("100%", str(fuel))

    def test_fuel_percentage(self):
        fuel = Fuel(0.1)
        self.assertEqual(10.0, fuel.fuel_percentage)

        fuel = Fuel(0.023)
        self.assertEqual(2.3, fuel.fuel_percentage)



