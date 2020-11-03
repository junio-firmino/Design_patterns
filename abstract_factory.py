from abc import ABC, abstractmethod


class Pizzafactory(ABC):
    @abstractmethod
    def createpizzaveg(self):
        pass

    @abstractmethod
    def createpizzacandy(self):
        pass

    @abstractmethod
    def createpizzatraditional(self):
        pass