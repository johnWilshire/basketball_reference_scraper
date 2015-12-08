#!/bin/usr/python

# this class is a game
import time
class Game:
    """
    home, home team
    visiting, visiting team
    date, the date of the game.
    """
    def __init__(self, home, visiting, date,game_id):
        self.home = home
        self.visiting = visiting
        self.date = date
        self.game_id = game_id

    def headers(self):
        return '|'.join(['date', 'game_id'])

    def to_str(self):
        return '|'.join([self.date, self.game_id])