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
"""This files main purpose is to define run and its necessary functions.
    All of the game rules are defined here as well"""
# import cards
# import pickle
# from cards import card_val
# import time
import sys
from cards import Deck
from player import Player
from player import to_file
from player import from_file
from time import sleep


def print_slow(string):
    """used to print the text char by char so it is more readble"""
    for count_x in string:
        sys.stdout.write(count_x)
        sys.stdout.flush()
        # time.sleep(0.08)
    return " "


class BlackJackGame:
    """The BlackJackGame class defines rules of the game,
        instructions on how it
    will play, etc."""
    def __init__(self):
        self._deck = Deck(60, 81)
        # cut card should be between 60 and 80
        self._game_state = True

    def run(self):
        """Run is the main function of this program"""
        # Now we are going to start the game
        # create an intial deck
        self._deck = Deck(60, 81)
        # create 7 more decks for a total of 8
        # deck_2 = Deck(60, 81)
        # deck_3 = Deck(60, 81)
        # deck_4 = Deck(60, 81)
        # deck_5 = Deck(60, 81)
        # deck_6 = Deck(60, 81)
        # deck_7 = Deck(60, 81)
        # merge the decks
        deck_1 = Deck(60, 81)
        self._deck.merge_decks(deck_1)
        deck_1 = Deck(60, 81)
        self._deck.merge_decks(deck_1)
        deck_1 = Deck(60, 81)
        self._deck.merge_decks(deck_1)
        deck_1 = Deck(60, 81)
        self._deck.merge_decks(deck_1)
        deck_1 = Deck(60, 81)
        self._deck.merge_decks(deck_1)
        deck_1 = Deck(60, 81)
        self._deck.merge_decks(deck_1)
        deck_1 = Deck(60, 81)
        self._deck.merge_decks(deck_1)
        # shuffle and cut the new "mega" deck, creating the shoe
        self._deck.shuffle()
        self._deck.cut()
        # now lets create peoples hands
        hands_list = []
        duplicate_list = []
        temp_player_list = from_file('Players.pckl') # for first time running comment this line out
        #replace it with this one, run it, then change it back. This is so that the pickle file is 
        #created and formatted properly
        #temp_player_list = []
        num_players = int(input(
            print_slow("How many people would like to play? [1-4]")))
        while num_players > 4 or num_players < 1:
            print_slow(
                "Invalid input. The game can only be played with 1-4 players")
            print()
            num_players = int(input(print_slow(
                "How many people would like to play? [1-4]")))
        print_slow(
            "You would like to play with {} players".format(num_players))
        print()
        iter_players = num_players
        player_list = []
        while iter_players > 0:
            no_match = True
            player_name = input(print_slow("What is your name?"))
            player_email = input(print_slow("What is your email?"))
            for temp_player in temp_player_list:
                if player_email == temp_player.get_email():
                    print_slow("Match found")
                    print()
                    player = temp_player
                    player_list.append(player)
                    no_match = False
                    duplicate_list.append(player)
                    break
            if no_match:
                player = Player(player_name, player_email)
                player_list.append(player)
            iter_players = iter_players - 1
        game_state = True
        while game_state:
            for player in player_list:
                name = player.get_name()
                email = player.get_email()
                bal = player.get_funds()
                print_slow(
                    "Player name is {}, email is {}, and their balence is {}"
                    .format(name, email, bal))
                print()
                player_bet = int(input(print_slow(
                    "How much would you like to bet?")))
                while player_bet > player.get_funds():
                    print_slow("You can not bet that high. Insufficent funds")
                    player_bet = int(input(print_slow(
                        "How much would you like to bet?")))
                player.set_bet(player_bet)
                print()
            hands_list = []
            for player in player_list:
                temp_hand = self._deck.deal(2)
                hands_list.append(temp_hand)
            # Now deal in the dealer
            hands_list.append(self._deck.deal(2))
            # print()
            # Lets go through and tell each person what they have, What the
            # dealer has and ask if they would like to hit,
            # stand, or potentialy split
            hand_iter = 0
            for player in player_list:
                print_slow("{}'s hand is:".format(player.get_name()))
                print()
                list_len = hands_list[hand_iter].__len__()
                size_iter = 0
                hand_val = 0
                val_with_ace = 100
                has_ace = False
                has_ten = False
                has_insure = False
                want_insurance = ""
                will_double = ""
                temp_bet = 0
                while size_iter < list_len:
                    test_string = hands_list[hand_iter][size_iter].__str__()
                    print_slow(test_string)
                    print()
                    hand_val += hands_list[hand_iter][size_iter].__int__()
                    if hands_list[hand_iter][size_iter].__int__() == 1:
                        has_ace = True
                    size_iter += 1
                dealer_string = hands_list[-1][0].__str__()
                print_slow("Dealer has {}".format(dealer_string))
                print()
                # check for insurance requirment
                dealers_card = hands_list[-1][0].__int__()
                if dealers_card in (10, 1):
                    has_ten = True
                else:
                    has_ten = False
                if has_ace and (hand_val + 10) < 21:
                    val_with_ace = hand_val + 10
                will_hit = 'y'
                allow_hit = True
                if has_ten:
                    want_insurance = input(print_slow(
                        "Would you like to purchase insurance? [Y/N]"))
                if want_insurance in ('Y', 'y'):
                    insurance_val = int(input(print_slow(
                        "How much insurance would you like?")))
                    player.set_insure_bet(insurance_val)
                    has_insure = True
                will_double = input(print_slow(
                    "Would you like to double down? [Y/N]"))
                if will_double in ('Y', 'y'):
                    hands_list[hand_iter].extend(self._deck.deal())
                    list_len = hands_list[hand_iter].__len__()
                    size_iter = 0
                    hand_val = 0
                    print_slow("New hand:")
                    print()
                    while size_iter < list_len:
                        test_string = \
                            hands_list[hand_iter][size_iter].__str__()
                        print_slow(test_string)
                        print()
                        hand_val += hands_list[hand_iter][size_iter].__int__()
                        if hands_list[hand_iter][size_iter].__int__() == 1:
                            has_ace = True
                        size_iter += 1
                    allow_hit = False
                    hand_iter += 1
                    temp_bet = player.get_bet()
                    temp_bet += temp_bet
                    player.set_bet(temp_bet)
                while allow_hit:
                    if hand_val < 21 and val_with_ace != 21:
                        will_hit = input(print_slow(
                            "Would you like to hit? [Y/N]"))
                    else:
                        allow_hit = False
                    if will_hit in ('Y', 'y'):
                        hands_list[hand_iter].extend(self._deck.deal())
                        list_len = hands_list[hand_iter].__len__()
                        size_iter = 0
                        hand_val = 0
                        print_slow("New hand:")
                        print()
                        while size_iter < list_len:
                            test_string = \
                                hands_list[hand_iter][size_iter].__str__()
                            print_slow(test_string)
                            print()
                            hand_val += \
                                hands_list[hand_iter][size_iter].__int__()
                            if hands_list[hand_iter][size_iter].__int__() == 1:
                                has_ace = True
                            size_iter += 1
                        if has_ace:
                            val_with_ace = hand_val + 10
                        will_hit = 'n'
                    else:
                        allow_hit = False
                if has_ace:
                    val_with_ace = hand_val + 10
                if val_with_ace < 22:
                    hand_val = val_with_ace
                hand_iter += 1
                player.set_score(hand_val)
                player.set_ace_score(val_with_ace)

                test_bool = True
                print()
            dealer_score = 0
            print_slow("The dealers cards are:")
            print()
            for dealer_hand in hands_list[-1]:
                print_slow(dealer_hand.__str__())
                print()
                dealer_score += dealer_hand.__int__()
            while dealer_score < 17:
                hands_list[-1].extend(self._deck.deal())
                dealer_score = 0
                print()
                print_slow("Dealer hit")
                print()
                for dealer_hand in hands_list[-1]:
                    print_slow(dealer_hand.__str__())
                    print()
                    dealer_score += dealer_hand.__int__()
            print()
            print_slow("New dealer score is: {}".format(dealer_score))
            print()
            print_slow("Final hands are:")
            print()
            for hands in hands_list:
                temp_string = ""
                for x in hands:
                    temp_string = temp_string + x.__str__()
                print_slow(temp_string)
                print()
            print()
            print_slow("Let's see who won")
            print()
            for player in player_list:
                if player.get_score() < 22 and\
                        player.get_score() > dealer_score:
                    print_slow("{} won!".format(player.get_name()))
                    print()
                    player_funds = player.get_funds()
                    player.set_funds(player_funds + player.get_bet())
                    if has_insure and dealer_score == 21:
                        print_slow("Dealer did not have 21."
                                   " Your side bet did not pay off")
                        print()
                        player_funds = player.get_funds()
                        player.set_funds(player_funds -
                                         player.get_insure_bet())
                    print_slow("You now have ${}".format(player.get_funds()))
                    print()
                elif dealer_score > 21 and player.get_score() < 22:
                    print_slow("{} won!".format(player.get_name()))
                    print()
                    player_funds = player.get_funds()
                    player.set_funds(player_funds + player.get_bet())
                    if has_insure and dealer_score == 21:
                        print_slow("Dealer did not have 21."
                                   " Your side bet did not pay off")
                        print()
                        player_funds = player.get_funds()
                        player.set_funds(player_funds -
                                         player.get_insure_bet())
                    print_slow("You now have ${}".format(player.get_funds()))
                    print()
                elif player.get_score() == dealer_score:
                    print_slow("{} it's a bust".format(player.get_name()))
                    print()
                    if has_insure and dealer_score == 21:
                        print_slow("Dealer has 21. Your side bet paid off")
                        print()
                        player_funds = player.get_funds()
                        player.set_funds(player_funds +
                                         player.get_insure_bet())
                    elif has_insure:
                        print_slow("Dealer does not have 21."
                                   " Your side bet did not pay off")
                        print()
                        player_funds = player.get_funds()
                        player.set_funds(player_funds -
                                         player.get_insure_bet())
                    print_slow("You now have ${}".format(player.get_funds()))
                    print()
                else:
                    print_slow("{} lost :(".format(player.get_name()))
                    print()
                    if has_insure and dealer_score == 21:
                        print_slow("Dealer has 21. Your side bet paid off")
                        print()
                        player_funds = player.get_funds()
                        player.set_funds(player_funds +
                                         player.get_insure_bet())
                    elif has_insure:
                        print_slow("Dealer does not have 21."
                                   " Your side bet did not pay off")
                        print()
                        player_funds = player.get_funds()
                        player.set_funds(player_funds -
                                         player.get_insure_bet())
                    player_funds = player.get_funds()
                    player.set_funds(player_funds - player.get_bet())
                    print_slow("You now have ${}".format(player.get_funds()))
                    print()
                    if player.get_funds() == 0:
                        print_slow("An anynomous donar gave you $10,000")
                        print()
                        player.set_funds(10000)
            play_again = input(print_slow(
                "Would you all like to play again? [Y/N]"))
            if play_again in ('Y', 'y'):
                game_state = True
                print()
                print()
                print()
                print("========================"
                      " NEW GAME ========================")
            else:
                game_state = False
                print_slow("Have a great day hope to see you again")
                print()
        for remove_players in temp_player_list:
            for x in player_list:
                if remove_players.get_email() == x.get_email():
                    player_list.remove(x)
        to_file('Players.pckl', player_list + temp_player_list)
