class Gerenciamentoevento():
    def __init__(self):
        print('Vamos conversar sobre o evento?.')

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


