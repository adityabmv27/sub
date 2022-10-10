from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

conn = create_engine('mysql+pymysql://root:aditya9499@localhost/game')

df = pd.read_sql("select * from statistics;", conn)
players = []
wins = []
loss = []
for player,player2 in df.iteritems():

    players.append(player)
for (index, row) in df.iterrows():
    for item in row:
        if len(wins) == len(players):
            loss.append(item)
        else:
            wins.append(item)

width = 0.2
bar1 = np.arange(len(players))
bar2 = [i+width for i  in bar1]
plt.bar(bar1,wins,width,label="Wins")
plt.bar(bar2,loss,width,label="Losses")
plt.xlabel("Players")
plt.ylabel("Number of Wins/Loss")
plt.title("Game Statictics")
plt.xticks(bar1+(width/2),players)
plt.legend()
plt.show()