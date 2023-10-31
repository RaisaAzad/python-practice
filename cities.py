# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:58:09 2023

@author: User
"""

prompt = "\nEnter cities you have visited: "
prompt += "\nEnter 'quit' when you are finished"

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I would love to go to "+ city.title())