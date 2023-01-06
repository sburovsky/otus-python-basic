"""
создайте класс `Plane`, наследник `Vehicle`
"""
from .base import Vehicle
from .exceptions import CargoOverload

class Plane(Vehicle):
    cargo = 0
    max_cargo = None

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, added_cargo):
        sum_cargo = self.cargo + added_cargo
        if self.max_cargo >= sum_cargo:
            self.cargo = sum_cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        prev_cargo = self.cargo
        self.cargo = 0
        return prev_cargo

