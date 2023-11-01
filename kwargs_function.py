# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 22:30:19 2023

@author: User
"""

def my_function(**kids):
    print("Her last name is "+ kids["lname"])
    print("Her first name is "+ kids["fname"])
    
my_function(fname = "Rachel", mname = "Karen", lname = "Green")