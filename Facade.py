class Gerenciamentoevento:
    def __init__(self):
        print('Vamos conversar sobre o que foi executado do evento até o momento?.')
        self.hotelier = None
        self.musician = None
        self.florist = None
        self.buffet = None

    def organization_initial(self):
        self.hotelier = Hotelier()
        self.hotelier.bookhotel()

    def organization_presentation(self):
        self.florist = Florist()
        self.florist.setflowerrequirements()

    def organization_musicians(self):
        self.musician = Musician()
        self.musician.setmusictype()

    def organization_buffet(self):
        self.buffet = Buffet()
        self.buffet.setbuffet()


class Hotelier:
    @staticmethod
    def bookhotel():
        print('Reservas dos quartos providencidos!.')


class Florist:
    @staticmethod
    def setflowerrequirements():
        print('Tipos de flores e aromas providenciados!.')


class Musician:
    @staticmethod
    def setmusictype():
        print('Musicos e repertórios escolhidos e providenciados!.')


class Buffet:
    @staticmethod
    def setbuffet():
        print('Tipos de aperitivos, comidas e doces escolhidos e providenciados!')


class Interface:
    def __init__(self):
        print('Vamos organizar o casamento?')

    @staticmethod
    def askinterface(escolha):
        ge = Gerenciamentoevento()
        if escolha == 'Hotel':
            ge.organization_initial()
        elif escolha == 'Flores':
            ge.organization_presentation()
        elif escolha == 'Musical':
            ge.organization_musicians()
        elif escolha == 'Buffet':
            ge.organization_buffet()
        else:
            ge.organization_initial()
            ge.organization_presentation()
            ge.organization_musicians()
            ge.organization_buffet()


if __name__ == '__main__':
    x = input('Qual parte da organização do casamento o Senhor quer acompanhar?.').title()
    inter = Interface()
    inter.askinterface(x)
