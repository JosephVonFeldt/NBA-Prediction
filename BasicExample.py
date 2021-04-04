# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 07:02:57 2021

@author: Joseph VonFeldt


Quick early example
"""
import pandas as pd
import matplotlib.pyplot as plt
import SimplyOddsBased as SO
import Scores as s

df = pd.read_csv("data\\cleannba2016.csv")



funs = [SO.pick_favorite, SO.pick_underdog, SO.implicit_odds]
funNames = ['Favs', "Unders", "Implicit"]


def row_to_SOpredictions(row, fun):
    """
    Arguements:
        row - row from df containting ML1 and ML2
        fun - SO function that predicts result of game
    Returns:
        predictions - tuple with predictions for t1 and t2
    """
    return fun(row[2], row[3])

for i in range(3):
    df[funNames[i]] = df.apply(lambda x: row_to_SOpredictions(x,funs[i]), axis=1)


for name in funNames:
    plt.plot(s.bet_score_games_detailed(df[["ML1", "ML2"]].values, df[name], df["Winner"])[2], label = name)
    
    
plt.legend()
    
plt.show()




for name in funNames:
    plt.plot(s.score_games_detailed(df[name], df["Winner"])[2], label = name)
    
plt.legend()
    
plt.show()