from sys import stdin

from lark import Lark, LarkError

import numpy as np

import math
import itertools

l = stdin.read().split("\n\n")

p1_deck = [int(x) for x in l[0].split("\n")[1:]]
p2_deck = [int(x) for x in l[1].split("\n")[1:]]


def get_score(deck):
    return sum([i * card for i, card in enumerate(deck[::-1], start=1)])


def Combat(start_deck_1, start_deck_2):

    deck_1 = start_deck_1.copy()
    deck_2 = start_deck_2.copy()
    
    round = 1

    while len(deck_1) > 0 and len(deck_2) > 0:

        print("-- Round", round, "--")
        print("Player 1's deck:", ", ".join(str(card) for card in deck_1))
        print("Player 2's deck:", ", ".join(str(card) for card in deck_2))

        top_1, top_2 = deck_1.pop(0), deck_2.pop(0)

        print("Player 1 plays:", top_1)
        print("Player 2 plays:", top_2)

        if top_1 > top_2:
            print("Player 1 wins the round!")
            deck_1.extend((top_1, top_2))

        else:
            print("Player 2 wins the round!")
            deck_2.extend((top_2, top_1))

        print()
        round += 1

    print("== Post-game results ==")
    print("Player 1's deck:", ", ".join(str(card) for card in deck_1))
    print("Player 2's deck:", ", ".join(str(card) for card in deck_2))

    winning = deck_1 if len(deck_1) > 0 else deck_2
    score = get_score(winning)

    return score


def Recursive_Combat(start_deck_1, start_deck_2):

    game = 1

    def _Recursive_Combat(deck_1, deck_2):

        nonlocal game

        previous_round_starts = set()

        current_game = game
        game += 1

        current_round = 1

        print("== Game", current_game, "==\n")

        while len(deck_1) > 0 and len(deck_2) > 0:

            print("-- Round", current_round, "(Game", str(current_game) + ") --")

            start_representation = ",".join(str(x) for x in deck_1) + "/" + ",".join(str(x) for x in deck_2)
            if start_representation in previous_round_starts:

                print("Game", current_game, "is known; Player 1 wins round", str(current_round) + "!")
                print("\n... anyway, back to round", str(current_game - 1) + "!")

                return True, False

            previous_round_starts.add(start_representation)

            print("Player 1's deck:", ", ".join(str(card) for card in deck_1))
            print("Player 2's deck:", ", ".join(str(card) for card in deck_2))

            card_1, card_2 = deck_1.pop(0), deck_2.pop(0)

            print("Player 1 plays:", card_1)
            print("Player 2 plays:", card_2)

            if len(deck_1) >= card_1 and len(deck_2) >= card_2:
                
                a_win, b_win = _Recursive_Combat(deck_1.copy()[:card_1], deck_2.copy()[:card_2])

                if a_win:
                    
                    print("Player 1 wins round", current_round, "of game", str(current_game) + "!\n")
                    deck_1.append(card_1)
                    deck_1.append(card_2)

                else:
                    print("Player 2 wins round", current_round, "of game", str(current_game) + "!\n")
                    deck_2.append(card_2)
                    deck_2.append(card_1)

            elif card_1 > card_2:
                print("Player 1 wins round", current_round, "of game", str(current_game) + "!\n")
                deck_1.append(card_1)
                deck_1.append(card_2)


            else:
                print("Player 2 wins round", current_round, "of game", str(current_game) + "!\n")
                deck_2.append(card_2)
                deck_2.append(card_1)

            current_round += 1

        winning_player = "1" if len(deck_1) > 0 else "2"
        print("The winner of game", current_game, "is player", winning_player + "!")

        if current_game != 1:
            print("\n... anyway, back to round", str(current_game - 1) + "!")

        return deck_1, deck_2


    res_1, res_2 = _Recursive_Combat(start_deck_1.copy(), start_deck_2.copy())

    print("\n== Post-game results ==")
    print("Player 1's deck:", ", ".join(str(card) for card in res_1))
    print("Player 2's deck:", ", ".join(str(card) for card in res_2))
    
    score = get_score(res_1 if len(res_1) > 0 else res_2)

    return score

score_1 = Combat(p1_deck, p2_deck)
score_2 = Recursive_Combat(p1_deck, p2_deck)

print("Part One, Combat:", score_1)
print("Part Two, Recursive Combat:", score_2)
