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
"""This file defines the player class, writing,
    and reading from a pickle file"""
import pickle


class Player:
    """Player class defines the player and all of its functions"""
    # pylint gives "too many instance attributes" but
    # all are needed so disregard
    def __init__(self, name, email, funds=10000):
        self._name = name
        self._email = email
        self._funds = funds
        self._score = 0
        self._score_ace = 0
        self._has_ace = False
        self._bet = 0
        self._insure_bet = 0

    def get_name(self):
        """Returns players name"""
        return self._name

    def get_email(self):
        """Returns players email"""
        return self._email

    def get_funds(self):
        """Returns players funds"""
        return self._funds

    def set_funds(self, balance):
        """Sets the players funds"""
        self._funds = balance

    def get_score(self):
        """Returns the players score"""
        return self._score

    def set_score(self, score):
        """Sets the players score"""
        self._score = score

    def get_ace_score(self):
        """Returns the players score with an ace"""
        return self._score_ace

    def set_ace_score(self, score):
        """Sets the score with a value of ace"""
        self._score_ace = score

    def set_bet(self, bet):
        """Sets the players bet"""
        self._bet = bet

    def get_bet(self):
        """Returns the players bet"""
        return self._bet

    def set_insure_bet(self, bet):
        """Sets the players insurance bet"""
        self._insure_bet = bet

    def get_insure_bet(self):
        """Returns the players insurace side bet"""
        return self._insure_bet


def to_file(pickle_file, players):
    """Defines writing to a file using pickle"""
    with open(pickle_file, 'wb') as file_handle:
        pickle.dump(players, file_handle, pickle.HIGHEST_PROTOCOL)


def from_file(pickle_file):
    """Defines getting information from a file using pickle"""
    with open(pickle_file, 'rb') as file_handle:
        players = pickle.load(file_handle)
    return players
