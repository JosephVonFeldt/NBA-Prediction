# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:59:27 2021

@author: Joseph VonFeldt
"""
import implicit_odds from SimpleOddsBased.py



def calculateBiasesSimple(df, knownBiases={}, iterations=1):
    """
    arguements:
        df - Dataframe of games to detect biases on
        knownBiases - dict of biases of oddsmakers
        iterations - number of iterations of of calculation
    returns:
        knownBiases - updated( or new) biases of oddsmakers
    """
    for i in range(iterations):
        expected={}
        actual={}
        for k in range(df.shape[0]):
            team1 = df[k,0]#this should be generalized for multiple df arrangements
            team2 = df[k,1]
            moneyline1 = df[k,2]
            moneyline2 = df[k,3]
            winner = df[k,4]
            if team1 not in expected:
                expected[team1] = 0
                actual[team1] = 0
            if team2 not in expected:
                expected[team2] = 0
                actual[team2] = 0
            if team1 not in knownBiases:
                knownBiases[team1] = 1
            if team2 not in knownBiases:
                knownBiases[team2] = 1
                
            expected1, expected2 = implicit_odds(moneyline1,moneyline2)
            expected1 /= knownBiases[team1]
            expected2 /= knownBiases[team2]
            tot = expected1 + expected2
            expected1, expected2 = expected1/tot, expected2/tot
            expected[team1] += expected1
            expected[team2] +==expected2
            if winner == 1:
                actual[team1] += 1
            else:
                actual[team2] += 1
        for key in knownBiases:
            knownBiases[key] *= expected[key]/actual[key]
    return knownBiases
    