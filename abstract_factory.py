from abc import ABC, abstractmethod


'''Pizza Factory'''


class Pizzafactory(ABC):
    def __init__(self):
        self.optionpizzaveg()
        self.optionpizzacandy()
        self.optionpizzatraditional()

    @abstractmethod
    def optionpizzaveg(self):
        pass

    @abstractmethod
    def optionpizzacandy(self):
        pass

    @abstractmethod
    def optionpizzatraditional(self):
        pass


''' Lojas nas Regiões '''


class Regionrich(Pizzafactory):
    def optionpizzaveg(self):
        return Typevegrich().descricion()

    def optionpizzacandy(self):
        return Typecandyrich().descricion()

    def optionpizzatraditional(self):
        return Typetraditionalrich().descricion()


class Regionpoor(Pizzafactory):
    def optionpizzaveg(self):
        return Typevegpoor().descricion()

    def optionpizzacandy(self):
        return Typecandypoor().descricion()

    def optionpizzatraditional(self):
        return Typetraditionalpoor().descricion()


class Regionmediun(Pizzafactory):
    def optionpizzaveg(self):
        return Typevegmediun().descricion()

    def optionpizzacandy(self):
        return Typecandymediun().descricion()

    def optionpizzatraditional(self):
        return Typetraditionalmediun().descricion()


'''Tipos de pizzas'''


class Vegpizza(ABC):
    @abstractmethod
    def descricion(self):
        pass


class Typevegrich(Vegpizza):
    def descricion(self):
        print('Massa VEGANA a base dos melhores ingredientes, Público classe A.')


class Typevegpoor(Vegpizza):
    def descricion(self):
        print('Massa VEGANA a base de ingredientes reaproveitados, Público classe C.')


class Typevegmediun(Vegpizza):
    def descricion(self):
        print('Massa VEGANA a base de ingredientes de 2 linha, Público em GERAL.')


class Candypizza(ABC):
    def descricion(self):
        pass


class Typecandyrich(Candypizza):
    def descricion(self):
        print('Massa DOCE a base dos melhores ingredientes, Público classe A.')


class Typecandypoor(Candypizza):
    def descricion(self):
        print('Massa DOCE a base de produtos reaproveitados, Público classe C.')


class Typecandymediun(Candypizza):
    def descricion(self):
        print('Massa DOCE a base de produtos de 2 linha, Público em GERAL.')


class Traditional(ABC):
    @abstractmethod
    def descricion(self):
        pass


class Typetraditionalrich(Traditional):
    def descricion(self):
        print('Massa TRADICIONAL a base dos melhores ingredientes, Público classe A.')


class Typetraditionalpoor(Traditional):
    def descricion(self):
        print('Massa TRADICIONAL a base de ingredientes reaproveitados, Público classe C.')


class Typetraditionalmediun(Traditional):
    def descricion(self):
        print('Massa TRADICIONAL a base de ingredientes de 2 linha, Público em GERAL.')


if __name__ == '__main__':
    tipos_escolhas = input('Qual a zona da região você mora? ').title()
    if tipos_escolhas == 'Rica':
        rr = Regionrich()
    elif tipos_escolhas == 'Pobre':
        pp = Regionpoor()
    else:
        mm = Regionmediun()
