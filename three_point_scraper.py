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
    pbp_url_to_game(url)
    return 0

# takes a url for a games play by play and extracts information from it
def pbp_url_to_game(url):
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
            if type(tds[5].string) == type(None):
                event_data = tds[5]
                score = tds[3].text.split('-')
                score_diff = str(int(score[1]) - int(score[0]))
                score = score[1]
                team = game.home
            else:
                team = game.visiting
                score = re.sub('\s','',tds[3].text)
                score = score.split('-')
                score_diff = str(int(score[0]) - int(score[1]))
                score = score[0]
                event_data = tds[1]
            # currently it only looks for point-score events
            match = re.search('[\d]-pt',event_data.text)
            if match:
                points = match.group()
                makes = re.search('makes|misses',event_data.text)
                player = event_data.find_all('a')[0]
                #event = Event(game,time,quater,players[0],points,score,score_diff)
                #game.add_to_events(event)

                row =  ["q"+quater, time,score,score_diff, points,makes.group(), player.text]
                print '|'.join(row)
    return summary




if __name__ == '__main__':
    main()