# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 05:34:58 2021

@author: Joseph VonFeldt

Here are a few simple methods of perdicting winners
"""


def moneyline_to_prob(moneyline):
    """
    arguements:
        moneyline - odds given in moneyline form
    returns:
        prob - implicit probability [given expected return of breaking even] 
    """
    if moneyline > 0:
        prob = 100 / (moneyline + 100)
    else: 
        moneyline *= -1
        prob = moneyline / (moneyline + 100)
    return prob


def pick_favorite(team1_moneyline, team2_moneyline):
    """
    Description:
        Returns the probablitiy of the favorite winning at 1.00 and that of
        the underdog winning at 0.00. If the game is a pick 'em, it returns
        0.50 for both teams
    arguements:
        team1_moneyline - odds of team1 winning given in moneyline form
        team2_moneyline - odds of team2 winning given in moneyline form
    returns:
        prob1 - likelihood of team1 winning
        prob2 - likelihood of team2 winning
    """
    pred1 = moneyline_to_prob(team1_moneyline)
    pred2 = moneyline_to_prob(team2_moneyline)
    
    if pred1 > pred2:
        return 1, 0
    elif pred2 > pred1:
        return 0, 1
    else:
        return 0.5, 0.5
    

def pick_underdog(team1_moneyline, team2_moneyline):
    """
    Description:
        Returns the probablitiy of the favorite winning at 0.00 and that of
        the underdog winning at 1.00. If the game is a pick 'em, it returns
        0.50 for both teams
    arguements:
        team1_moneyline - odds of team1 winning given in moneyline form
        team2_moneyline - odds of team2 winning given in moneyline form
    returns:
        prob1 - likelihood of team1 winning
        prob2 - likelihood of team2 winning
    """
    pred1 = moneyline_to_prob(team1_moneyline)
    pred2 = moneyline_to_prob(team2_moneyline)
    
    if pred1 < pred2:
        return 1, 0
    elif pred2 < pred1:
        return 0, 1
    else:
        return 0.5, 0.5
    

def implicit_odds(team1_moneyline, team2_moneyline):
    """
    Description:
        Returns the probablitiy of each team winning given implicit odds
        Note thes probabilities will almost certainly add up to more than one
        and likely will need to be normalized.
    arguements:
        team1_moneyline - odds of team1 winning given in moneyline form
        team2_moneyline - odds of team2 winning given in moneyline form
    returns:
        prob1 - likelihood of team1 winning
        prob2 - likelihood of team2 winning
    """
    pred1 = moneyline_to_prob(team1_moneyline)
    pred2 = moneyline_to_prob(team2_moneyline)
    
    return pred1, pred2
    
