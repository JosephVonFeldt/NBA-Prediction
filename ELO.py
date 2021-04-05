# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 06:10:03 2021

@author: Joseph VonFeldt
"""

class ELO:
    def __init__(self, rating=1500, k=40,gamesPlayed=0):
        self.rating=rating
        self.k=k
        self.gamesPlayed=gamesPlayed
        
        
    def expected(self, other):
        """
        arguments:
            other - instance of ELO
        
        returns:
            exp - expected value of outcome 
                       1 for a win,
                       0.5 for a draw,
                       0 for a loss
        """
        rating_diff = other.rating - self.rating
        exp = 1/(1+10**(rating_diff/400))
        return exp
    
    def update(self, score, exp):
        """
        arguments:
            score - outcome of a match 
                       1 for a win,
                       0.5 for a draw,
                       0 for a loss
            exp - expected outcome of match
        
        returns:
            updated self.rating
        """
        change = self.k * (score - exp)
        self.rating += change
        self.gamesPlayed +=1
        if self.gamesPlayed > 20:
            self.k = 20 if self.gamesPlayed < 40 else 10
        return self.rating
    
    def match(self, other, result):
        """
        arguments:
            result - outcome of a match 
                       1 for a win,
                       0.5 for a draw,
                       0 for a loss
            other - [instance of ELO] for opponent
        
        returns:
            
        """
        expected_self = self.expected(other)
        expected_other = other.expected(self)
        self.update(result, expected_self)
        other.update(1-result,expected_other)
        
        
    def __lt__(self, other):
        """
        returns: self.rating < other.rating
            
        """
        return self.rating < other.rating
    
    def __le__(self, other):
        """
        returns: self.rating <= other.rating
            
        """
        return self.rating <= other.rating
    
    def __eq__(self, other):
        """
        returns: self.rating == other.rating
            
        """
        return self.rating == other.rating
    
    def __gt__(self, other):
        """
        returns: self.rating > other.rating
            
        """
        return self.rating > other.rating
    
    def __ge__(self, other):
        """
        returns: self.rating >= other.rating
            
        """
        return self.rating >= other.rating
    
    def __ne__(self, other):
        """
        returns: self.rating != other.rating
            
        """
        return self.rating != other.rating
    
    def __repr__(self):
        return f"Rating: {self.rating}, K:{self.k}"
        
    
        
        
        
        
        
        
        
        
        
        
        