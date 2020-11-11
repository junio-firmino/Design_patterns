class Gerenciamentoevento:
    def __init__(self):
        print('Vamos conversar sobre o que foi executado do evento até o momento?.')

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
    def bookhotel(self):
        print('Reservas dos quartos providencidos!.')


class Florist:
    def setflowerrequirements(self):
        print('Tipos de flores e aromas providenciados!.')


class Musician:
    def setmusictype(self):
        print('Musicos e repertórios escolhidos e providenciados!.')


class Buffet:
    def setbuffet(self):
        print('Tipos de aperitivos, comidas e doces escolhidos e providenciados!')


class Interface:
    def __init__(self):
        print('Vamos organizar o casamento?')

    def askinterface(self,x):
        ge = Gerenciamentoevento()
        if x == 'Hotel':
            ge.organization_initial()
        elif x == 'Flores':
            ge.organization_presentation()
        elif x == 'Musical':
            ge.organization_musicians()
        elif x == 'Buffet':
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
