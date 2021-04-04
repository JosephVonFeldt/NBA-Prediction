# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 04:48:48 2021

@author: Joseph VonFeldt

This is used to score the accuracy of predictions made by various models.
"""






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
    if result:
        score = prob1 - prob2
    elif result == 2:
        score = prob2 - prob1
    else:
        raise ValueError("result must be either 1 or 2")
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
        result - Either 1 or 2 signifying the true outcome
    returns:
        total_score - higher is better; negative indicates worse than random
        score_list - scores for each individual game
    """
    assert (len(prediction_list) == len(results_list))
    
    scores_list = []
    
    num_of_games = len(prediction_list)
    
    for i in range(num_of_games):
        prediction, result  = prediction_list[i], results_list[i]
        pred1 = prediction[0]
        pred2 = prediction[1]
        
        game_score = score(pred1, pred2, result)
        scores_list.append(game_score)
        
    total_score = sum(scores_list)   
    
    return total_score, scores_list

