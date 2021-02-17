class Fuel:
    def __init__(self, level: float) -> None:
        self.current_level = level
        self.price_per_litre = 1.75

    def __str__(self) -> str:
        return "{0:.0f}%".format(self.fuel_percentage)

    @property
    def fuel_percentage(self) -> float:
        return self.current_level * 100
