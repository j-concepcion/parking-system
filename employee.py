
class Employee:
    def __init__(self, name: str, rate: float) -> None:
        self.name = name
        self.rate = rate

    def __str__(self) -> str:
        return self.name

    def calculate_pay(self, price: float ) -> float:
        "Calculates employee's comission"
        return self.rate * price

