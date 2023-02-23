#!/usr/bin/env python3
# Ethan Jones
# CPSC 386-04
# 2022-03-28
# ejonest@csu.fullerton.edu
# @ejonest
#
# Lab 05-00
#
# This is a black jack game with the rules laid out in the rubric
#
"""This module defines the cards class, deck class,
    and functions used within"""
from collections import namedtuple
from random import randrange
from random import shuffle
from math import floor


Card = namedtuple('Card', ['rank', 'suit'])


def format_output(base_card):
    """Function to format output of a card. Used to adjust Card.__str__"""
    return f"{base_card.rank} of {base_card.suit}'s "


Card.__str__ = format_output


class Deck:
    """Deck class creates a deck of 52 cards and defines functions to use with
        the deck. For a deck to be made it needs to be passes a min and max
        value for the cut card."""
    ranks = ["Ace"] + [str(x) for x in range(2, 11)] + \
        "Jack Queen King".split()
    suits = "Clubs Heart Spades Diamonds".split()
    values = list(range(1, 11)) + [10, 10, 10]
    value_dict = dict(zip(ranks, values))

    def __init__(self, cut_min, cut_max):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
        self.cut_position = randrange(cut_min, cut_max)

    def __getitem__(self, position):
        return self._cards[position]

    def __len__(self):
        return len(self._cards)

    def merge_decks(self, other_deck):
        """Merge_decks is a function that allows a passed deck to be merged
            into the deck"""
        self._cards = self._cards + other_deck.get_cards()

    def shuffle(self, times_shuffle=1):
        """Shuffle shuffles the deck(s)"""
        for _ in range(times_shuffle):
            shuffle(self._cards)

    def cut(self):
        """Cut defines a function to cut hte deck"""
        round_num = floor(len(self._cards) * 2)
        half = (len(self._cards) // 2) + randrange(-round_num, round_num)
        tophalf = self._cards[:half]
        bottomhalf = self._cards[half:]
        self._cards = bottomhalf + tophalf

    def deal(self, cards_dealt=1):
        """Defines a function to deal out a given amount of cards"""
        return [self._cards.pop() for _ in range(cards_dealt)]

    def needs_shuffle(self):
        """Checks if a suffle of the cards is needed
            based on the cut_position"""
        return len(self._cards) <= self.cut_position

    def get_rank(self):
        """Function to return the rank of a card"""
        return self.ranks

    def get_cards(self):
        """Function to get all of the cards ina  deck"""
        return self._cards


def card_val(card):
    """Function that returns the value of a cards rank"""
    return Deck.value_dict[card.rank]


Card.value = card_val
Card.__int__ = card_val


def card_rank(card):
    """Returns the rank of a card"""
    return card.rank
