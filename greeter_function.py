# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 14:03:59 2023

@author: User
"""

def my_function(fname,lname):
    full_name = fname+' '+lname
    return full_name.title()
while True:
    print("\nPlease tell me your name: ")
    print("\nEnter 'q' at anytime to quit: ")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    name = my_function(f_name, l_name)
    print("\nHello "+name+"!")
    
    