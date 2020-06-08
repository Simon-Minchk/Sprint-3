from random import randint, sample, uniform
import random as random
class Product:
    def __init__(self, name):
        self.name = name
        self.price = randint(5, 100)
        self.weight = randint(5, 100)
        self.flammability = random.uniform(0, 2.5)
        self.identifier = 2
        self.identifier = randint(1000000, 9999999)
    def stealability(self):
        if self.price/self.weight < .5:
            print ("Not so stealable")
        elif 1 > self.price/self.weight >= .5:
            print ("Kinda stealable")
        else:
            print ("Very stealable")
    def explode(self):
        if self.flammability*self.weight < 10:
            print (". . . Fizzzzz")
        elif 10<=self.flammability*self.weight < 50:
            print (". . . Boom!")
        else:
            print (". . . KABOOOOM!")

class BoxingGlove(Product):
    def __init__(self,name):
        super().__init__(name)
        self.weight = 10
    def explode(self):
        print ("its a glove..")
    def punch(self):
        if self.weight < 5:
            print ("Weak")
        elif 5 <= self.weight < 15:
            print ("Hey that hurt!")
        else:
            print ("Ouch!")