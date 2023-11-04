# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 13:47:34 2023

@author: User
"""

def build_person(fname,lname):
    person ={"first" : fname, "last" : lname}
    return person
musician = build_person('Jimi', 'Hendrix')
print(musician)