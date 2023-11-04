# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 13:41:30 2023

@author: User
"""

def my_function(fname, lname, mname = ''):
    if mname:
        full_name = fname+" "+mname+" "+lname
    else:
        full_name = fname+" "+lname
    return full_name.title()
name = (my_function("Emily", "Hudson"))
print(name)
name = (my_function("Rachel", "Green", "Karen"))
print(name)