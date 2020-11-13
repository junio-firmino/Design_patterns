class Actor:
    def __init__(self):
        self.occuped = False

    def occupied(self):
        self.occuped = True
        print(type().__name__,'está ocupado com novo filme.')

    def available(self):
        self.occuped = False
        print(type().__name__,'está disponível para novos trabalhos.')

    def getstatus(self):
        return self.occuped

    
