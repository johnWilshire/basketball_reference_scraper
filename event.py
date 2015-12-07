#!/bin/usr/python

# this class is an event in a play by play
# see the 6 column rows of http://www.basketball-reference.com/boxscores/pbp/201510270GSW.html

class Event:
    """
    game, the game object that this event refers to
    time, the time in game of this event
    player the primary player in this event
    eventType, 3-pt shot, 2-pt shot, free throw ect.
    shot, true if the shot was successful, false if miss
    score, the current score of the game at the time of this event
    assistPlayer, the assisting player
    """

    def __init__(self,game, time, quater, team, player,event_type, score, assist_player=None):
        self.game = game
        self.time = time
        self.quater = quater
        self.player = player
        self.score = score
        self.event_type = event_type
        self.assist_player = assist_player
