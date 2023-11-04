# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 18:33:49 2023

@author: User
"""

def build_profile(fname, lname, **user_info):
    profile={}
    profile['first name']=fname
    profile['last name']=lname
    for key, value in user_info.items():
        profile[key]=value
    return profile
user_profile = build_profile("albert", "einstein", field = 'physics', location = 'princeton')
print(user_profile)