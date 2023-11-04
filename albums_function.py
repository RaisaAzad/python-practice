# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 14:28:26 2023

@author: User
"""

def make_album(artist_name, album_title, track_number = ''):
    album = {"Name of artist":artist_name, "Name of the album":album_title, "Number of tracks":track_number}
    if track_number:
        album = {"Name of artist":artist_name, "Name of the album":album_title, "Number of tracks":track_number}
    else:
        album = {"Name of artist":artist_name, "Name of the album":album_title}
    return album
musician = make_album("Pinl Floyd", "Wish you were here", "5")
print(musician)
musician = make_album("Maneskin", "Rush")
print(musician)