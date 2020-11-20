class Subject:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def notifyall(self,*args,**kwargs):
        for observer in self.observers:
            observer.notify(self,*args,**kwargs)

class Observer1:
    def __init__(self,sub):
        Subject.register(self,sub)

    def notify(self,sub,*args):
        print(type(self).__name__,':get', args, 'from', sub)

class Observer2:
    def __init__(self, sub):
        subject.register(self)

    def notify(self, sub, *args):
        print(type(self).__name__,':get', args, 'from', sub)

bc = Subject()
ob1 = Observer1(oi)
ob2 = Observer2(loi)
bc.notifyall('vamos ver')