# makes sure that you are have setwd()'d yourself to the right place
shots <- read.csv("basketball_shots.csv",sep = '|')
curry <- shots[shots$player.player_id == 'curryst01',]
curry3ptr <- curry[curry$event_type == '3-pt',]
table(curry$makes_shot)
all3ptrs <- shots[shots$event_type == '3-pt',]
library(ggplot2)
qplot(curry3ptr$distance,fill=as.factor(curry3ptr$makes_shot), main = "curry")
qplot(all3ptrs$distance,fill=as.factor(all3ptrs$makes_shot))
qplot(shots$distance,fill=as.factor(shots$makes_shot),main="all shots")
