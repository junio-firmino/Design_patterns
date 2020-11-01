from abc import ABC, abstractmethod


class Section(ABC):
    @abstractmethod
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


class Profile(ABC):
    def __init__(self):
        self.sections = []
        self.createprofile()

    @abstractmethod
    def createprofile(self):
        pass

    @abstractmethod
    def secoescreate(self):
        pass

    def getsections(self):
        return self.sections

    def addsections(self, escolha):
        self.sections.append(escolha)


class Acougue(Profile):
    def createprofile(self):
        self.addsections(Personalsection())
        self.addsections(Featuresection())

    def secoescreate(self):
        return Personalsection().describe(), Featuresection().describe()


class Padaria(Profile):
    def createprofile(self):
        self.addsections(Emplooyersection())
        self.addsections(Advertisingsection())

    def secoescreate(self):
        return Emplooyersection().describe(), Advertisingsection().describe()


if __name__ == '__main__':
    profile_type = input('Qual seção você prefere?')
    profile = eval(profile_type.title())()
    print('Criando seção...', type(profile).__name__)
    profile.secoescreate()
    print('Profile has ', profile.getsections())
