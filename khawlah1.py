#!/usr/bin/env python3
# Author : khawlah
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        # Add score member variable to store each player's score
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.updateScore(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        # Play 5 rounds
        for round in range(5):
            print(f"Round {round}:")
            self.play_round()
        # Based on player's score - take decision who win
        if(self.p1.score > self.p2.score):
            print('Player P1 wins')
        else:
            if(self.p1.score < self.p2.score):
                print('Player P2 wins')
            else:
                print('Game ends with Tie')
        print("Game over!")

    def updateScore(self, move1, move2):
        if(beats(move1, move2)):
            print('Player 1 wins this round')
            self.p1.score = self.p1.score + 1
        else:
            if(beats(move2, move1)):
                print('Player 2 wins this round')
                self.p2.score = self.p2.score + 1
            else:
                print('Tie')
        print('\tPlayer 1 score = '+str(self.p1.score))
        print('\tPlayer 2 score = '+str(self.p2.score))


# 1- Generate a subclass "RandomPlayer" from the superclass "Player"
class RandomPlayer(Player):
    def __init__(self):
        super(RandomPlayer, self).__init__()
    # Return 'rock' or 'scissors' or 'paper' at random

    def move(self):
        # Generate random numbers between 1 and 3
        randNum = random.randint(1, 3)
        if(randNum == 1):
            return 'rock'
        else:
            if(randNum == 2):
                return 'scissors'
            else:
                if(randNum == 3):
                    return 'paper'
                # Code musn't reach here as rand integer will be either 1-3
                else:
                    return None


# 2- Generate a subclass "HumanPlayer " from the superclass "Player"
class HumanPlayer(Player):
    def __init__(self):
        super(HumanPlayer, self).__init__()

    # Read the move from the input
    def move(self):
        # Get the user input
        humanMove = input('Enter your move \n\t rock or scissors or paper : ')
        # Validate the user input
        cond1 = humanMove == 'rock'
        cond2 = humanMove == 'scissors'
        cond3 = humanMove == 'paper'
        while(not(cond1 or cond2 or cond3)):
            message = 'Enter your move \n\t Only rock or scissors or paper : '
            humanMove = input(message)
            cond1 = humanMove == 'rock'
            cond2 = humanMove == 'scissors'
            cond3 = humanMove == 'paper'
        return humanMove


# 3- Generate a subclass "HumanPlayer " from the superclass "Player"
class ReflectPlayer(Player):
    def __init__(self):
        super(ReflectPlayer, self).__init__()
        self.learntMove = 'rock'  # Initially let the learnt move is rock

    # The move will be same as learnt move
    def move(self):
        ''' It will be rock in 1st round &
            same as other player last move afterwards
        '''
        return self.learntMove

    # Set the learnt move to the other player last move
    def learn(self, myMove, otherLastMove):
        self.learntMove = otherLastMove


# 4- Generate a subclass "CyclePlayer " from the superclass "Player"
class CyclePlayer(Player):
    def __init__(self):
        super(CyclePlayer, self).__init__()
        self.learntMove = 'scissors'  # Initially let the learnt move is rock

    # The move will be same as learnt move
    def move(self):
        if(self.learntMove == 'rock'):
            return 'paper'
        if(self.learntMove == 'paper'):
            return 'scissors'
        if(self.learntMove == 'scissors'):
            return 'rock'

    # Set the learnt move to the my last move
    def learn(self, myMove, otherLastMove):
        self.learntMove = myMove


if __name__ == '__main__':
    # First make a game against always rock player
    print("*************************************")
    print("\t Game against Always rock Player")
    game1 = Game(HumanPlayer(), Player())
    game1.play_game()
    # Then make a game against RandomPlayer
    print("*************************************")
    print("\t Game against RandomPlayer")
    game1 = Game(HumanPlayer(), RandomPlayer())
    game1.play_game()
    # Then make a game against ReflectPlayer
    print("*************************************")
    print("\t Game against Reflect Player")
    game2 = Game(HumanPlayer(), ReflectPlayer())
    game2.play_game()
    # Finally make a game against CyclePlayer
    print("*************************************")
    print("\t Game against Cycle Player")
    game3 = Game(HumanPlayer(), CyclePlayer())
    game3.play_game()
