#!/bin/usr/python


import requests
from bs4 import BeautifulSoup
import re
from game import Game
from player import Player
from event import Event
import sys

def main():
    url = 'http://www.basketball-reference.com/boxscores/pbp/201510270GSW.html'
    getGameSummaryFromPBP(url)
    return 0


def getGameSummaryFromPBP(url):
    summary = dict()
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'lxml')
    # make game object for this game
    (visiting, home, date) = re.split(' at | Play-By-Play, ', soup.h1.text)
    game = Game(visiting=visiting, home= home, date=date)
    print game.home, game.visiting, game.date
    divs = soup.find_all('div', {"class": 'clear_both width100'})
    table = divs[0].find_all('table')[-1]
    quater = '0'
    for tr in table.find_all('tr'):
        tds = tr.find_all('td')
        if 'id' in tr.attrs:
            quater = tr.attrs['id'][-1]
        if len(tds) == 6:
            time = tds[0].text
            print type(tds[1].string), type(tds[5].string)
            if type(tds[5].string) == type(None):
                team = game.home
                print "home"
                event_data = tds[5]
            else:
                team = game.visiting
                event_data = tds[1]
                print "visiting"
            # currently it only looks for point-score events
            if re.search('[\d]-pt',event_data.text):
                
                players = event_data.find_all('a')
                print "len players", len(players)
                print players[0].text
    return summary




if __name__ == '__main__':
    main()