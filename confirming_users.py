# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:17:18 2023

@author: User
"""

#moving item from one list to another
#start with a list of unconfirmed users
#and an empty list to hold confirmed users

unconfirmed_users = ['brian','candace','alice','ryan']
confirmed_users = []

#Verify each user until there are no users
#Move each user to the confirmed list
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: "+current_user.title())
    confirmed_users.append(current_user)
    
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())