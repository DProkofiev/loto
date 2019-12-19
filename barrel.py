"""
   класс "БОЧОНОК" с функциями мешка
   сначала мешок полный.  вызывая NEXT, выбирается случайная цифра и удаляется из мешка
"""
import random


class Barrel:
    def __init__(self):
        self.digit = 0
        self.bag = [i for i in range(1, 91)]
        self.count = 90

    def next(self):
        self.digit = random.choice(self.bag)
        self.bag.remove(self.digit)
        self.count = len(self.bag)
