# make sure that you are have setwd()'d yourself to the right place
library(ggplot2)
shots <- read.csv("data/basketball_shots_curry.csv",sep = '|')
curry <- shots[shots$player.player_id == 'curryst01',]
curry3ptr <- curry[curry$event_type == '3-pt',]
table(curry$makes_shot)
all3ptrs <- shots[shots$event_type == '3-pt',]
# it is weird there are some 3-ptrs that occur at 0 and 10 feet
qplot(curry3ptr$distance,fill=as.factor(curry3ptr$makes_shot), main = "curry")
qplot(all3ptrs$distance,fill=as.factor(all3ptrs$makes_shot))
qplot(shots$distance,fill=as.factor(shots$makes_shot),main="all shots")

# we have this many players
length(table(shots$player.player_id))
