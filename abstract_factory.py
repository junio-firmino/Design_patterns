from abc import ABC, abstractmethod


class Pizzafactory(ABC):
    def __init__(self):
        self.createpizzaveg()
        self.createpizzacandy()

    @abstractmethod
    def createpizzaveg(self):
        pass

    @abstractmethod
    def createpizzacandy(self):
        pass

    @abstractmethod
    def createpizzatraditional(self):
        pass

class Regionrich(Pizzafactory):         #Lojas nas regiões
    def createpizzaveg(self):
        return Typevegrich().descricion()

    def createpizzacandy(self):
        return Typecandyrich().descricion()

    def createpizzatraditional(self):
        return Typetraditionalrich()

class Regionpoor(Pizzafactory):
    def createpizzaveg(self):
        return Typevegpoor().descricion()

    def createpizzacandy(self):
        return Typecandypoor().descricion()

    def createpizzatraditional(self):
        return Typetraditionalpoor()

class Regionmediun(Pizzafactory):
    def createpizzaveg(self):
        return Typevegmediun().descricion()

    def createpizzacandy(self):
        return Typecandymediun().descricion()

    def createpizzatraditional(self):
        return Typetraditionalmediun()

class Vegpizza(ABC):
    @abstractmethod
    def descricion(self):
        pass

class Typevegrich(Vegpizza):
    def descricion(self):
        print('Massa VEGANA a base dos melhores ingredientes.')

class Typevegpoor(Vegpizza):
    def descricion(self):
        print('Massa VEGANA a base de ingredientes reaproveitados.')

class Typevegmediun(Vegpizza):
    def descricion(self):
        print('Massa VEGANA a base de ingredientes de 2 linha.')

class Candypizza(ABC):
    def descricion(self):
        pass

class Typecandyrich(Candypizza):
    def descricion(self):
        print('Massa DOCE a base dos melhores ingredientes.')

class Typecandypoor(Candypizza):
    def descricion(self):
        print('Massa DOCE a base de produtos reaproveitados.')

class Typecandymediun(Candypizza):
    def descricion(self):
        print('Massa DOCE a base de produtos de 2 linha.')









if __name__ == '__main__':
    ff = Regionrich()
