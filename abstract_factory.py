from abc import ABC, abstractmethod


class Pizzafactory(ABC):            #Fábrica
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

class Vegpizza(ABC):
    @abstractmethod
    def descricion(self):
        pass

class Typevegrich(Vegpizza):
    def descricion(self):
        print('Massa vegana a base dos melhores ingredientes.')

class Typevegpoor(Vegpizza):
    def descricion(self):
        print('Massa vegana a base de ingredientes reaproveitados.')

class Typevegmediun(Vegpizza):
    def descricion(self):
        print('Massa vegana a base de ingredientes de 2 linha.')

class Candypizza(ABC):
    def descricion(self):
        pass

class Typecandyrich(Candypizza):
    def descricion(self):
        print('Massa para pizza doce a base dos melhores ingredientes.')



if __name__ == '__main__':
    ff = Regionrich()
    ff.createpizzaveg()