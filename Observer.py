class Subject:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def notifyall(self, *args, **kwargs):
        for observer in self.observers:
            observer.notify(self, *args, **kwargs)


class Observer1:
    def __init__(self, bc):
        bc.register(self)

    def notify(self, bc, *args):
        print(type(self).__name__, ':get', args, 'from', bc)


class Observer2:
    def __init__(self, bc):
        bc.register(self)

    def notify(self, bc, *args):
        print(type(self).__name__, ':get', args, 'from', bc)


bc = Subject()
ob1 = Observer1(bc)
ob2 = Observer2(bc)
bc.notifyall('vamos ver')
