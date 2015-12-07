#!/bin/usr/python

# this class is a game

class Game:
    """
    home, home team
    visiting, visiting team
    date, the date of the game.
    """
    def __init__(self, home, visiting, date):
        self.home = home
        self.visiting = visiting
        self.date = date
        self.events = list()
        self.players = list()

    def add_to_events(self, event):
        self.events.append(event)

    def add_to_players(self, player):
        self.events.append(player)