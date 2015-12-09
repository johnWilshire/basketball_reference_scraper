#!/bin/usr/python

# class aggregating the player class
import re
from player import Player

class Players:
    def __init__(self):
        self.players = dict()
        self.events = 0

    def getPlayer(self, bio_tag):
        self.events += 1
        player_id = self.extract_player_id(bio_tag)
        if player_id in self.players:
            return self.players[player_id]
        else:
            name = bio_tag.text
            player = Player(name,player_id)
            self.players[player_id] = player
            return player


    def extract_player_id(self,bio_tag):
        return re.search('/players/./(.*)\.html',bio_tag['href']).group(1)

    def dump_players(self, file):
        headers = True
        for player_id in self.players:
            for event in self.players[player_id].event_list:
                if headers:
                    headers = False
                    file.write(event.headers()+'\n')
                file.write(event.to_str()+'\n')

