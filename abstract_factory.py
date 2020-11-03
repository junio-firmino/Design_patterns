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

class Regionrich(Pizzafactory):
    def createpizzaveg(self):
        return Typevegrich()

    def createpizzacandy(self):
        return Typecandyrich()

    def createpizzatraditional(self):
        return Typetraditionalrich()

class Regionpoor(Pizzafactory):
    def createpizzaveg(self):
        return Typevegpoor()

    def createpizzacandy(self):
        return Typecandypoor()

    def createpizzatraditional(self):
        return Typetraditionalpoor()

class Regionmediun(Pizzafactory):
    def createpizzaveg(self):
        return Typevegmediun()

    def createpizzacandy(self):
        return Typecandymediun()

    def createpizzatraditional(self):
        return Typetraditionalmediun()