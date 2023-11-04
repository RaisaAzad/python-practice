# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 18:47:46 2023

@author: User
"""

def make_cars(manufacturer, model_name, **car_info):
    car_profile = {}
    car_profile['Name of manufacturer']= manufacturer
    car_profile['Model']=model_name
    for key,value in car_info.items():
        car_profile[key]=value
    return car_profile
car = make_cars('subaru', 'outback', color = 'blue', tow_package = True)
print(car)