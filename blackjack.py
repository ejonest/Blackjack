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
"""This file pulls eveything together and is the one that will be run using
./blackjack.py in the terminal"""
import game

if __name__ == "__main__":
    GAME = game.BlackJackGame()
    GAME.run()
