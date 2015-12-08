#!/bin/usr/python

# this class is an event in a play by play
# see the 6 column rows of http://www.basketball-reference.com/boxscores/pbp/201510270GSW.html

class Event:
    """
    game, the game object that this event refers to
    time, the time in game of this event
    player the primary player in this event
    eventType, 3-pt shot, 2-pt shot, free throw ect.
    makes_shot, true if the shot was successful, false if miss
    score, the current score of the players team at the time of this event
    score_diff, the score difference -n means that they are behind by n points
    assistPlayer, the assisting player
    distance, distance in feet that the shot was made
    """

    def __init__(self,game, time, quater, team, player,event_type, makes_shot, distance, score,score_diff, assist_player=None):
        self.game = game
        self.time = time
        self.quater = quater
        self.team = team
        self.player = player
        self.score = score
        self.score_diff = score_diff
        self.event_type = event_type
        self.makes_shot = str(makes_shot)
        self.distance = str(distance)
        self.assist_player = assist_player

    def headers(self):
       return self.game.headers() + '|' + '|'.join(['team','quater','time','score','score_diff', 'event_type','makes_shot', 'distance', 'player.short_name','player.player_id'])
    def to_str(self):
        return self.game.to_str() + '|' + '|'.join([self.team,self.quater,self.time,self.score,self.score_diff, self.event_type,self.makes_shot, self.distance, self.player.short_name, self.player.player_id])