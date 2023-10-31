# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:45:02 2023

@author: User
"""

current_num = 0
while current_num < 10:
    current_num += 1
    if current_num % 2 == 0:
        continue
    print(current_num)