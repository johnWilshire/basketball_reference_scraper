# basketball_reference_scraper

a web scraper for http://www.basketball-reference.com/

Scrapes score attempt events (2-pt, 3-pt) for all games played by a player given a player url.
This includes events that the specified player was not a part of.

It is our plan to use this dataset to examine streaks in sports using dynamic Bradley Terry modeling.

###py/*
Contains the scraper so far and class files.

###R/* 
Contains some dataset loading and basic analysis scripts.