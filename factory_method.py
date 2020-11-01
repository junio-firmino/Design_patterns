from abc import ABC

class Section(ABC):
    def describe(self):
        pass

class Personalsection(Section):
    def describe(self):
        print('Seção criada.')

class Featuresection(Section):
    def describe(self):
        print('Características criadas.')

class Emplooyersection(Section):
    def describe(self):
        print('Empregados contratados.')

class Advertisingsection(Section):
    def describe(self):
        print('Comercial contratado.')