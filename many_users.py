# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:47:34 2023

@author: User
"""

users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',},
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())