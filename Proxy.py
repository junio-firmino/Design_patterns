class Actor:
    def __init__(self,nm):
        if nm == 'True':
            self.occuped = True  # Retorna  OCUPADO
        else:
            self.occuped = False  # Retorna DISPONÍVEL

    def occupied(self):
        #self.occuped = True
        print(type(self).__name__,'está ocupado com novo filme.')

    def available(self):
        #self.occuped = False
        print(type(self).__name__,'está disponível para novos trabalhos.')

    def getstatus(self):
        return self.occuped

class Agent:
    def __init__(self):
        self.sd = None

    def work(self):
        es = input("False ou True? ").title()
        self.actor = Actor(es)
        if self.actor.getstatus():
            self.actor.occupied()
        else:
            self.actor.available()

if __name__ == '__main__':
    r=Agent()
    r.work()
