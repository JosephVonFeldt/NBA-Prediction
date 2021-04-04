# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 04:48:48 2021

@author: Joseph VonFeldt

This is used to score the accuracy of predictions made by various models.
It rewards confidently predicting well and punishes confidently predicting
incorrectly.
"""

from SimplyOddsBased import moneyline_to_prob




def normalize_prediction(pred1, pred2):
    """
    Arguements:
        pred1 - predicted liklihood of first result
        pred2 - predicted liklihood of second result
    returns:
        prob1 - implicit probability of first outcome
        prob2 - implicit probability of second outcome
    """
    
    predSum = pred1+pred2
    prob1 = pred1/predSum
    prob2 = pred2/predSum
    return prob1,  prob2


def score(pred1, pred2, result):
    """
    Arguements:
        pred1 - predicted liklihood of first result
        pred2 - predicted liklihood of second result
        result - Either 1 or 2 signifying the true outcome
    returns:
        score - higher is better
    """
    
    prob1, prob2 = normalize_prediction(pred1, pred2)
    if result == 1:
        score = prob1 - prob2
    elif result == 2:
        score = prob2 - prob1
    else:
        raise ValueError("result must be either 1 or 2")
    if score < 0: 
        score *= 2
    return score

def score_games(prediction_list, results_list):
    """
    Arguements:
        prediction_list - list of tuples of the form (prediction1, prediction2)
        result_list - list of 1's and 2's indicating the final result
        result - Either 1 or 2 signifying the true outcome
    returns:
        total_score - higher is better; negative indicates worse than random
    """
    assert (len(prediction_list) == len(results_list))
    
    total_score = 0
    
    num_of_games = len(prediction_list)
    
    for i in range(num_of_games):
        prediction, result  = prediction_list[i], results_list[i]
        pred1 = prediction[0]
        pred2 = prediction[1]
        
        game_score = score(pred1, pred2, result)
        total_score += game_score
        
        
    return total_score



def score_games_detailed(prediction_list, results_list):
    """
    Arguements:
        prediction_list - list of tuples of the form (prediction1, prediction2)
        result_list - list of 1's and 2's indicating the final result
    returns:
        total_score - higher is better; negative indicates worse than random
        score_list - scores for each individual game
        running_total_list - total of scores_list up to 
                             and including current index
    """
    assert (len(prediction_list) == len(results_list))
    
    scores_list = []
    running_total_list = []
    total_score = 0
    
    num_of_games = len(prediction_list)
    
    for i in range(num_of_games):
        prediction, result  = prediction_list[i], results_list[i]
        pred1 = prediction[0]
        pred2 = prediction[1]
        
        game_score = score(pred1, pred2, result)
        total_score += game_score
        running_total_list.append(total_score)
        scores_list.append(game_score)
    
    return total_score, scores_list, running_total_list



##### May move this function when refactoring
def moneyline_to_return(moneyline, wager):
    """
    Arguements:
        moneyline - odds given in as moneyline
        wager - amount wagered
    returns:
        roi - return on investment [including initial wager]
    """
    multiplier  = 1 + moneyline_to_prob(moneyline)
    return wager * multiplier


def bet_score(team1_moneyline, team2_moneyline, pred1, pred2, result):
    """
    Arguements:
        team1_moneyline - odds of team1 winning given in moneyline form
        team2_moneyline - odds of team2 winning given in moneyline form
        pred1 - predicted liklihood of first result
        pred2 - predicted liklihood of second result
        result - Either 1 or 2 signifying the true outcome
    returns:
        score - higher is better
    """
    
    prob1, prob2 = normalize_prediction(pred1, pred2) #might rename these later
    score = 0
    if prob1 > prob2:
        score -= prob1-prob2
        if result == 1:
            score += moneyline_to_return(team1_moneyline, prob1-prob2)
    if prob2 > prob1:
        score -= prob2-prob1
        if result == 2:
            score += moneyline_to_return(team2_moneyline, prob2-prob1)
    return score


def bet_score_games(moneyline_list, prediction_list, results_list):
    """
    Arguements:
        moneyline_list - list of tuples of the form (moneyline1, moneyline2)
        prediction_list - list of tuples of the form (prediction1, prediction2)
        result_list - list of 1's and 2's indicating the final result
    returns:
        total_score - higher is better; negative indicates worse than random
    """
    assert (len(prediction_list) == len(results_list))
    assert (len(moneyline_list) == len(results_list))
    
    total_score = 0
    
    num_of_games = len(prediction_list)
    
    for i in range(num_of_games):
        moneyline = moneyline_list[i]
        moneyline1 = moneyline[0]
        moneyline2 = moneyline[1]
        prediction = prediction_list[i]
        pred1 = prediction[0]
        pred2 = prediction[1]
        result = results_list[i]
        
        game_score = bet_score(moneyline1, moneyline2, pred1, pred2, result)
        total_score += game_score
        
        
    return total_score


def bet_score_games_detailed(moneyline_list, prediction_list, results_list):
    """
    Arguements:
        moneyline_list - list of tuples of the form (moneyline1, moneyline2)
        prediction_list - list of tuples of the form (prediction1, prediction2)
        result_list - list of 1's and 2's indicating the final result
    returns:
        total_score - higher is better; negative indicates worse than random
        score_list - scores for each individual game
        running_total_list - total of scores_list up to 
                             and including current index
    """
    assert (len(prediction_list) == len(results_list))
    assert (len(moneyline_list) == len(results_list))
    
    total_score = 0
    scores_list = []
    running_total_list = []
    
    num_of_games = len(prediction_list)
    
    for i in range(num_of_games):
        moneyline = moneyline_list[i]
        moneyline1 = moneyline[0]
        moneyline2 = moneyline[1]
        prediction = prediction_list[i]
        pred1 = prediction[0]
        pred2 = prediction[1]
        result = results_list[i]
        
        game_score = bet_score(moneyline1, moneyline2, pred1, pred2, result)
        total_score += game_score
        running_total_list.append(total_score)
        scores_list.append(game_score)
        
        
    return total_score, scores_list, running_total_list












