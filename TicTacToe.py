
#This file is the master for a tictactoe trainer
#It contains code for the game, a player who plays
#randomly, associated caches, and a trained strategy

#This program represents a 3 x 3 tictactoe board by
#the digits 1 through 9, labelled left to right then
#top to bottom (the bottom left corner is 7, etc). 
#A game consists of ordered lists of moves for player 1 ('X')
#and player 2 ('O'). A game state consists of either
#a subgame with the moves in cardinal order, or a
#9-tuple of ternary digits with 0 = 'blank', 1 = 'X',
#and 2 = 'O'.


import random


#Initializes new game
#def New_Game():
#    gstate = [0,0,0,0,0,0,0,0,0]
#    xmoves = []
#    omoves = []
#    return gstate, xmoves, omoves

#Checks for game winner; returns '1' or '2' for decisive
#game, '3' for a drawn game, and '0' for incomplete game
def Winner_Is(gstate):

    xwins = [(0,1,2),(0,4,8),(0,3,6), (1,4,7),
                (2,4,6), (2,5,8), (3,4,5), (6,7,8)]
    owins = xwins
    
    
    for place in range(9):
        if gstate[place] == 0:
            for tuple in xwins:
                if tuple.count(place) > 0:
                    if tuple in xwins: xwins.remove(tuple)
                    if tuple in owins: owins.remove(tuple)
                    
                    
        elif gstate[place] == 1:
            for tuple in owins:
                if tuple.count(place) > 0:
                    if tuple in owins: owins.remove(tuple)
                    
        else:
            for tuple in xwins:
                if tuple.count(place) > 0:
                    if tuple in xwins: xwins.remove(tuple)
    
    if len(xwins) == 1:
        winner = 1
    elif len(owins) == 1:
        winner = 2
    elif gstate.count(0) == 0:
        #This indicates a draw
        winner = 3
    else:
        winner = 0
    
    return winner

#Makes a random move given a list of moves and gamestate
def Random_Move(gstate,moves):
    blank_space = []
    for place in range(9):
        if gstate[place] == 0:
            blank_space.append(place)
            
    move = random.choice(blank_space)
    print(move)
    moves.append(move)
    
    
    return move, moves


#Plays a game between two random players
def Play_Random_Game():
    gstate = [0,0,0,0,0,0,0,0,0]
    xmoves = []
    omoves = []
    winner = 0
    turn = 0
    while winner == 0:
        print(gstate)
        if turn %2 == 0:
            next_move = Random_Move(gstate,xmoves)
            move = next_move[0]
            xmoves = next_move[1]
            gstate[move] = 1
            turn = turn + 1
            winner = Winner_Is(gstate)
        else:
            next_move = Random_Move(gstate,omoves)
            move = next_move[0]
            omoves = next_move[1]
            gstate[move] = 2
            turn = turn + 1
            winner = Winner_Is(gstate)
    print(winner,xmoves,omoves)        
    return winner, xmoves, omoves
            