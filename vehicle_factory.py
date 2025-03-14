"""
Vehicle Factory Module
Implements an abstract factory pattern for creating vehicles with US and EU specifications.
"""

import logging
from abc import ABC, abstractmethod

# Logging setup
logging.basicConfig(level=logging.INFO)


class Vehicle(ABC):
    """Abstract class for all vehicles"""

    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        """Abstract method for starting the engine"""


class Car(Vehicle):
    """Car class"""

    def start_engine(self) -> None:
        logging.info(
            "%s %s (%s Spec): Engine started", self.make, self.model, self.spec
        )


class Motorcycle(Vehicle):
    """Motorcycle class"""

    def start_engine(self) -> None:
        logging.info(
            "%s %s (%s Spec): Engine started", self.make, self.model, self.spec
        )


class VehicleFactory(ABC):
    """Abstract factory for creating vehicles"""

    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        """Creates a car"""

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        """Creates a motorcycle"""


class USVehicleFactory(VehicleFactory):
    """Factory for US vehicles"""

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "US")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "US")


class EUVehicleFactory(VehicleFactory):
    """Factory for EU vehicles"""

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "EU")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "EU")


# Factory usage
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

us_car = us_factory.create_car("Ford", "Mustang")
us_car.start_engine()

eu_motorcycle = eu_factory.create_motorcycle("BMW", "R1250GS")
eu_motorcycle.start_engine()
