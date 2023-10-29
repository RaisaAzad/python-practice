# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 11:23:23 2023

@author: User
"""

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]='ducati'
print(motorcycles)
print(motorcycles[1].title())
motorcycles.append('honda')
print(motorcycles)
#del motorcycles[3]
popped_motorcycle = motorcycles.pop(3)
print(motorcycles)
print(popped_motorcycle)
print("My first motorcycle is "+popped_motorcycle.title())
motorcycles.remove('ducati')
print(motorcycles)

motorcycles.append('ducati')
motorcycles.append('honda')
motorcycles.sort()
print(motorcycles)
motorcycles.reverse()
print(motorcycles)
print(len(motorcycles))