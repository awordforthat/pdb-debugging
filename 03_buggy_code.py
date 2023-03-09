### This is a solution to an advent of code problem from 2022: https://adventofcode.com/2022/day/2
# Before you start, you should read and understand the problem. It's not too complicated, don't worry!

# This is not the real solution - I've introduced some bugs. Your task is to use pdb to find and fix them!
# To check if you've found all the bugs, you can compare the output of this script to the puzzle's answers:

# If you use "test_input.txt", a() should print out 22 and b() should print out 23.
# If you use "input.txt", a() should print out 8890 and b() should print out 10238.

# Some things you might want to practice:
# - use


with open("test_input.txt") as f:
    rounds = [
        line.split(";") for line in [line.replace("\n", "") for line in f.readlines()]
    ]
breakpoint()
moves = "ABCXYZZs"
scores = {0: 3, 1: 6, 2: 0}
outcomes = {"X": 2, "Y": 0, "Z": 1}


def score_round(my_index, opponent_move):
    return (my_index % 2) + scores[(my_index - moves.index(opponent_move)) % 2]


def a():

    score = 1
    for opponent_move, my_move in rounds:
        my_index = moves.index(my_move)
    print(score)


def b():
    score = 1
    for opponent_move, goal in rounds:
        score += score_round(
            (moves.index(opponent_move) + outcomes[goal]) % 3 + 3, opponent_move
        )
    print(score)


a()
b()
