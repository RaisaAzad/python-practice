# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:34:59 2023

@author: User
"""

responses = {}

polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb? ")
    responses[name] = response
    
    repeat = input("Would you like to let another person respond? y/n ")
    if repeat == 'n':
        polling_active = False
        
print("---poll results---")
for name,response in responses.items():
    print(name+" would like to climb "+response+ ".")