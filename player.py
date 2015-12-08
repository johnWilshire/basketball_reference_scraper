#!/bin/usr/python

# this is a class representing a basketball player

class Player:
    """
    web page is the players web page on basketball refrence
    event list is a list of events that the player is involved in
    """
    def __init__(self, short_name, player_id, web_page=''):
        self.short_name = short_name
        self.player_id = player_id
        self.web_page = web_page
        self.event_list = list()
        self.assist_list = list()


    def add_to_events(self, event):
        self.event_list.append(event)

    def add_to_assists(self, event):
        self.assist_list.append(event)
