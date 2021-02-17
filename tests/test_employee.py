from unittest import TestCase

from employee import Employee


class TestEmployee(TestCase):
    def test_correctly_initialised(self):
        employee = Employee('A', 0.15)
        self.assertEqual('A', employee.name)
        self.assertEqual(0.15, employee.rate)
        self.assertEqual([], employee.vehicles_to_process)


    def test_to_string(self):
        employee = Employee('A', 0.15)
        self.assertEqual("A", str(employee))

        employee = Employee('Employee B', 0.15)
        self.assertEqual("Employee B", str(employee))


    def test_calculate_pay(self):
        employee = Employee('A', 0.10)
        self.assertEqual(
            10.001, # (10.01 * 0.10) + 10.01
            employee.calculate_pay(100.01)
        )
