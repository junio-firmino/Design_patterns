from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def som(self):
        pass

class Cao(Animal):
    def som(self):
        print("Au, Au!!")

class Gato(Animal):
    def som(self):
        print("Miau, miau!!!")

class Factoryanimal:
    # def __init__(self,escolha):
    #     self.escolha = escolha

    def make_som(self,escolha):
        # return eval(escolha)().som()
        if escolha == 'Gato':
            return Gato().som()
        else:
            return Cao().som()


if __name__ == '__main__':
    ff = Factoryanimal()
    animal = input('Qual animal é a sua preferêcia?').title()
    ff.make_som(animal)