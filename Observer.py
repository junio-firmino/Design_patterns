class subject:
    def __init__(self):
        self.observers = []

    def register (self, observer):
        self.observers.append(observer)

    def notifyall(self,*args,**kwargs):
        for observer in self.observers:
            observer.notify(self,*args,**kwargs)