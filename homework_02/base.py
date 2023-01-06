from abc import ABC
from . import exceptions


class Vehicle(ABC):

    def __init__(self, weight = 1200, fuel = 50, fuel_consumption = 20):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance):
        fuel_require = distance * self.fuel_consumption
        if self.fuel >= fuel_require:
            self.fuel -= fuel_require
        else:
            raise exceptions.NotEnoughFuel


