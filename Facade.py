class Gerenciamentoevento():
    def __init__(self):
        print('Vamos conversar sobre o evento?.')

    def organization_initial(self):
        self.hotelier = Hotelier()
        self.hotelier.bookhotel()

        self.florist = Florist()
        self.florist.setflowerrequirements()

    def organization_musicians(self):
        self


