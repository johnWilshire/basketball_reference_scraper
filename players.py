#!/bin/usr/python

# class aggregating the player class

from player import Player
class Players:
    def __int__(self):
        self.players = dict()

    def getPlayer(self, bio_tag):
        player_id = self.extract_player_id(bio_tag)
        if player_id in self.players:
            return self.players[player_id]
        else:
            name = bio_tag.text
            player = Player(name,player_id)
            self.players[player_id] = player
            return player


    def extract_player_id(self,bio_tag):
        return bio_tag

    def dump_players(self):
        for player_id in self.players:
            print self.players[player_id].to_str()

