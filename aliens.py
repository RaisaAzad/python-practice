# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:37:34 2023

@author: User
"""

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

del alien_0['points']
print(alien_0)

