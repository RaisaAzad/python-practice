# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 22:14:31 2023

@author: User
"""

def my_func(fname,lname):
    full_name = fname + ' '+ lname
    return full_name.title()
my_name = my_func("Emily", "Hudsson")
print(my_name)