# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 23:51:14 2023

@author: User
"""

def make_shirt(size = 'large',text = 'i love Python'):
    print("\nThe shirt you ordered is of size "+size.title())
    print("And it says- "+text)
    
make_shirt('small', 'Just do it')
make_shirt()