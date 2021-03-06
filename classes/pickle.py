import abc
from classes.vegetable import Vegetable


class Pickle(Vegetable):
    @abc.abstractmethod
    def grow(self, number=0):
        self.grow += number

    def __init__(self) -> None:
        super().__init__('pickle')