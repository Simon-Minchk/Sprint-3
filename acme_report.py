#!/usr/bin/env python
from acme import Product
from random import randint, sample, uniform
import random as random

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
productlist = []
product = []
average_price = ()
average_weight = ()
average_flammability = ()

def generate_products(num_products=30):
    for num_products in range(num_products):
        name = random.choice(ADJECTIVES ) + ' ' + random.choice(NOUNS)
        product = Product(name)
        productlist.append(name)
        average_price = average_price + product.price()
    return print('average_price')


def inventory_report(products=1):
    for products in range(products):
        generate_products()
    return productlist

#if __name__ == '__main__':
    #inventory_report(generate_products())


