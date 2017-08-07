# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:26:59 2015

@author: jack.gang
"""

import time    
import pandas as pd
from enum import Enum

start = time.clock()

# returns a boolean
def hasRoyalFlush(cards):
    if hasStraightFlush(cards) and (max([i[0] for i in cards]) == 14):
        return True
    else:
        return False

# returns highest card of straight flush
def hasStraightFlush(cards):
    if hasFlush(cards) and hasStraight(cards):
        return max([i[0] for i in cards])
    else:
        return False
    
# returns list in form of [card, kicker]
def hasFourOfAKind(cards):
    cardValues = pd.Series([i[0] for i in cards])
    counts = cardValues.value_counts()
    if counts[counts == 4].empty:
        return False
    else:
        return [counts[counts==4].index[0], counts[counts!=4].index[0]]

# returns list in form of [triple card, double card]
def hasFullHouse(cards):
    cardValues = pd.Series([i[0] for i in cards])
    counts = cardValues.value_counts()
    if counts[counts == 3].empty:
        return False
    elif counts[counts == 2].empty:
        return False
    else:
        return [counts[counts==3].index[0], counts[counts==2].index[0]]
        
# returns list of cards in descending order
def hasFlush(cards):
    cardSuits = pd.Series([i[1] for i in cards])
    counts = cardSuits.value_counts()
    if counts[counts == 5].empty:
        return False
    else:
        return sorted(pd.Series([i[0] for i in cards]), reverse=True)
    
# returns highest card of straight
def hasStraight(cards):
    cardValues = sorted([i[0] for i in cards])
    for i in range(1, 5):
        if (int(cardValues[i]) - int(cardValues[i-1])) != 1:
            if (cardValues[i] == 14) and (int(cardValues[i]) - int(cardValues[i-1])) != 9:
                return False
            if cardValues[i] != 14:
                return False           
    if (int(cardValues[i]) - int(cardValues[i-1])) == 1:
        return cardValues[4]
    else:
        return cardValues[3]   
        
# returns list in form of [card, kicker 1, kicker 2]
def hasThreeOfAKind(cards):
    cardValues = pd.Series([i[0] for i in cards])
    counts = cardValues.value_counts()
    if counts[counts == 3].empty:
        return False
    else:
        return [counts[counts==3].index[0], sorted(counts[counts!=3].index, reverse=True)[0], sorted(counts[counts!=3].index, reverse=True)[1]]
    
# returns list in form of [high card, low card, kicker]
def hasTwoPairs(cards):
    cardValues = pd.Series([i[0] for i in cards])
    counts = cardValues.value_counts()
    if counts[counts == 2].empty or len(counts[counts == 2]) < 2:
        return False
    else:
        cardOne = counts[counts==2].index[0]
        cardTwo = counts[counts==2].index[1]
        if cardOne > cardTwo:
            return [cardOne, cardTwo, counts[counts!=2].index[0]]
        else:
            return [cardTwo, cardOne, counts[counts!=2].index[0]]
        
# returns list in form of [card, kicker 1, kicker 2, kicker 3]
def hasOnePair(cards):
    cardValues = pd.Series([i[0] for i in cards])
    counts = cardValues.value_counts()
    if len(counts[counts == 2]) != 1:
        return False
    else:
        return [counts[counts==2].index[0], sorted(counts[counts!=2].index, reverse=True)[0], sorted(counts[counts!=2].index, reverse=True)[1], sorted(counts[counts!=2].index, reverse=True)[2]]
    
# enum for hand ranks
class handRank(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10
    
# compares two hands and returns True if player 1 wins
def compareHands(cardsOne, cardsTwo):    
    oneRank = assignRank(cardsOne)
    twoRank = assignRank(cardsTwo)
#    print(oneRank, twoRank)
    if oneRank.value > twoRank.value:
        return True
    elif oneRank.value < twoRank.value:
        return False
    else:
        if oneRank == handRank.ROYAL_FLUSH:
            return True
        elif oneRank == handRank.STRAIGHT_FLUSH:
            return hasStraightFlush(cardsOne) >= hasStraightFlush(cardsTwo)
        elif oneRank == handRank.FOUR_OF_A_KIND:
            if hasFourOfAKind(cardsOne)[0] > hasFourOfAKind(cardsTwo)[0]:
                return True
            elif hasFourOfAKind(cardsOne)[0] == hasFourOfAKind(cardsTwo)[0]:
                return hasFourOfAKind(cardsOne)[1] >= hasFourOfAKind(cardsTwo)[1]
            else:
                return False
        elif oneRank == handRank.FULL_HOUSE:
            if hasFullHouse(cardsOne)[0] > hasFullHouse(cardsTwo)[0]:
                return True
            elif hasFullHouse(cardsOne)[0] == hasFullHouse(cardsTwo)[0]:
                return hasFullHouse(cardsOne)[1] >= hasFullHouse(cardsTwo)[1]
            else:
                return False
        elif oneRank == handRank.FLUSH:
            for i in range(0, len(hasFlush(cardsOne))):
                if hasFlush(cardsOne)[i] > hasFlush(cardsTwo)[i]:
                    return True
                elif hasFlush(cardsOne)[i] < hasFlush(cardsTwo)[i]:
                    return False
            return True
        elif oneRank == handRank.STRAIGHT:
            return hasStraight(cardsOne) >= hasStraight(cardsTwo)
        elif oneRank == handRank.THREE_OF_A_KIND:
            for i in range(0, len(hasThreeOfAKind(cardsOne))):
                if hasThreeOfAKind(cardsOne)[i] > hasThreeOfAKind(cardsTwo)[i]:
                    return True
                elif hasThreeOfAKind(cardsOne)[i] < hasThreeOfAKind(cardsTwo)[i]:
                    return False
            return True
        elif oneRank == handRank.TWO_PAIRS:
            for i in range(0, len(hasTwoPairs(cardsOne))):
                if hasTwoPairs(cardsOne)[i] > hasTwoPairs(cardsTwo)[i]:
                    return True
                elif hasTwoPairs(cardsOne)[i] < hasTwoPairs(cardsTwo)[i]:
                    return False
            return True
        elif oneRank == handRank.ONE_PAIR:
            for i in range(0, len(hasOnePair(cardsOne))):
                if hasOnePair(cardsOne)[i] > hasOnePair(cardsTwo)[i]:
                    return True
                elif hasOnePair(cardsOne)[i] < hasOnePair(cardsTwo)[i]:
                    return False
            return True
        else:
            cardsOne = sorted(cardsOne, reverse=True)
            cardsTwo = sorted(cardsTwo, reverse=True)
            for i in range(0, len(cardsOne)):
                if cardsOne[i] > cardsTwo[i]:
                    return True
                elif cardsOne[i] < cardsTwo[i]:
                    return False
            return True

# assign a handRank to a set of cards
def assignRank(cards):
    cardRank = 0
    if hasRoyalFlush(cards):
        cardRank = handRank.ROYAL_FLUSH
    elif hasStraightFlush(cards):
        cardRank = handRank.STRAIGHT_FLUSH
    elif hasFourOfAKind(cards):
        cardRank = handRank.FOUR_OF_A_KIND
    elif hasFullHouse(cards):
        cardRank = handRank.FULL_HOUSE
    elif hasFlush(cards):
        cardRank = handRank.FLUSH
    elif hasStraight(cards):
        cardRank = handRank.STRAIGHT
    elif hasThreeOfAKind(cards):
        cardRank = handRank.THREE_OF_A_KIND
    elif hasTwoPairs(cards):
        cardRank = handRank.TWO_PAIRS
    elif hasOnePair(cards):
        cardRank = handRank.ONE_PAIR
    else:
        cardRank = handRank.HIGH_CARD
    
    return cardRank
    
# converts cards to numerical format
def convertCards(cards):
    newCards = []
    for card in cards:
        if card[0] == 'T':
            value = 10
        elif card[0] == 'J':
            value = 11
        elif card[0] == 'Q':
            value = 12
        elif card[0] == 'K':
            value = 13
        elif card[0] == 'A':
            value = 14
        else:
            value = int(card[0])
        suit = card[1]
        newCards.append((value, suit))
    return newCards

# MAIN

answer = 0
f = open('p054_poker.txt', 'r')
for line in f:
    cardsOne = line.split()[:5]
    cardsOneNew = convertCards(cardsOne)
    
    cardsTwo = line.split()[5:]
    cardsTwoNew = convertCards(cardsTwo)
    
    if compareHands(cardsOneNew, cardsTwoNew):
#        print(cardsOneNew, cardsTwoNew)
        answer += 1   
f.close()
    
elapsed = time.clock() - start

print("{} found in {} seconds".format(answer,elapsed))
