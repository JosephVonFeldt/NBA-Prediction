# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 06:50:39 2021

@author: Joseph VonFeldt
"""

from ELO import ELO
import pandas as pd

def measure_ELO(df_TrainingGames):
    """
    Arguments:
        DF_TrainingGames - Pandas DF of TrainingGames
                           Must include Team1, Team2, and Winner Columns
    Returns:
        ELOs - Dictionary containing instances of ELO for each team.
               {Teamname: ELO}
    """
    ELOs = dict()
    for row in df_TrainingGames.itertuples(index=False):
        team1 = row[0]
        team2 = row[1]
        winner = row[4]
        if team1 not in ELOs:
            ELOs[team1] = ELO()
        if team2 not in ELOs:
            ELOs[team2] = ELO()
        ELOs[team1].match(ELOs[team2],1 if winner == 1 else 0 )
    return ELOs


def predict_from_ELO(team1, team2):
    """
    Arguments:
        team1 - instance of ELO for team1
        team2 - instance of ELO for team2
    Returns:
        pred1 - likelihood of team1 winning
        pred2 - likelihood of team2 winning
    """
    pred1 = team1.expected(team2)
    pred2 = team2.expected(team1)
    return pred1, pred2