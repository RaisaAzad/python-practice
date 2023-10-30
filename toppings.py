# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:24:58 2023

@author: User
"""

requested_toppings = ['mushrooms', 'extra cheese']


for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
        
print("\nFinished making your pizza!")