# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 16:28:42 2023

@author: User
"""

players = ['charles','martin','michael','florence','eli','renee']

print("The first three players in the list are: ")
for player in players[:3]:
    print(player.title())
    
print("The three players in the middle of the list are: ")
for player in players[1:4]:
    print(player.title())
    
print("The last three players in the list are: ")
for player in players[3:6]:
    print(player.title())