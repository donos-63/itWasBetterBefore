import abc

def Vegetable(ABC):

    @abc.abstractmethod
    def printtype(self):
        print(self.name)
    
    @abc.abstractmethod
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod 
    def grow(self, number=0):
        pass