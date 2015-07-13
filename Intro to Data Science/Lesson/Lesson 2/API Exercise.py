'''
Author: Udacity
Last updated: 12 Jul 2015
Context: API Exercise
'''

import json
import requests

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    
    data = requests.get(url).text
    data = json.loads(data)
    #print type(data)
    print data
    
    artists = data['topartists']
    topArtist = artists['artist'][0]
    topArtistName = topArtist['name']
    print topArtistName

    return topArtistName # return the top artist in Spain

