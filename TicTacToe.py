#!/usr/bin/env python
# coding: utf-8

# In[54]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print("-----")
    print(board[4]+'|'+board[5]+'|'+board[6])
    print("-----")
    print(board[1]+'|'+board[2]+'|'+board[3])
    
  


# In[55]:



#COPY AND PASTE POSITION_CHOICE BECAUSE OF SIMILARITIES

def player_input():
    
    marker = ''
    
    while not (marker== 'X' or marker== 'O'):
        
        marker =input("Player 1: Would you like to play as X or O? ").upper()
        
        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')


# In[56]:


def place_marker(board, marker, position):
    
    #LOOKS LIKE IT TAKES THE 0 POSITION OF BOARD AND EQUATS THAT TO MARKER
    board[position] = marker


# In[57]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[58]:


place_marker(test_board,'$',8)
display_board(test_board)


# In[59]:


def win_check(board, mark):
    
    #WIN TIC TAC TOE
    
    #ALL ROWS, AND CHECK TO SEE IF ALL SHARE SAME MARKER
       return ((board[1] == mark and board [2] == mark and board [3] == mark) or
        (board[4] == mark and board [5] == mark and board [6] == mark) or
        (board[7] == mark and board [8] == mark and board [9] == mark) or
    
    #ALL COLUMNS 
        (board[1] == mark and board [4] == mark and board [7] == mark) or
        (board[2] == mark and board [5] == mark and board [8] == mark) or
        (board[3] == mark and board [6] == mark and board [9] == mark) or
    
    #TWO DIAGNOLS 
        (board[1] == mark and board [5] == mark and board [9] == mark) or
        (board[3] == mark and board [5] == mark and board [7] == mark))
            
        


# In[60]:


display_board(test_board)
win_check(test_board, 'X')


# In[61]:


import random

def choose_first():
    
    #COIN FLIP TO SEE WHO GOES FIRST 
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# In[62]:


def space_check(board, position):
    
    #RETURN IS A BOOLEAN UNLESS OTHERWISE NOTED
    return board[position] == ' '


# In[63]:


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
        
        #BOARD IS FULL IF WE RETURN TRUE
    return True
    


# In[64]:


def player_choice(board):
    
    #GOOD PLACE TO START AS NOTHING IS HAPPENING AT POSITION 0
    position = 0
    
    #CALL SPACE CHEECK TO SEE IF SPACE IS AVAILABLE 
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9)'))
        
    return position


# In[67]:


def replay():
    
    choice = 'wrong'
    
    while choice not in ['Yes', 'No']:
        
        choice=input("Would you like to play again? (Yes or No) ")
        
        if choice not in ['Yes','No']:
            print ("Sorry, I don't understand, please choose Yes or No ")
            
    if choice == "Yes":
        return True
    else:
        return False


# In[68]:


#WHILE LOOP TO KEEP RUNNING THE GAME
print("Welcome to Tic Tac Toe")

while True: 

    #PLAY GAME
    
    
    #SET EVERYTHING UP (BOARD, WHO'S FIRST, CHOOSE MARKERS X,O)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Ready to play? Y or N? ')
    
    if play_game == 'Y':
        game_on= True
    else:
        game_on=False
    
    #GAME PLAY
    
    while game_on:
        
         #PLAYER ONE TURN
        
        if turn == 'Player 1':
            
            #SHOW BOARD
            display_board(the_board)
            
            #CHOOSE A POSITION
            position = player_choice(the_board)
            
            #PLACE THE MARKER ON THE POSITION
            place_marker(the_board, player1_marker, position)
            
            #CHECK IF WON
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print ('Player One has won!!!')
                game_on=False
            
            #CHECK IF THERE IS A TIE
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print ('The game has ended in a TIE!')
                    break
             #NO TIE OR WIN? THEN NEXT PLAYERS TURN       
                else: 
                    turn = 'Player 2'
            
            #PLAYER TWO TURN
        else:
            
            #SHOW BOARD
            display_board(the_board)
            
            #CHOOSE A POSITION
            position = player_choice(the_board)
            
            #PLACE THE MARKER ON THE POSITION
            place_marker(the_board, player2_marker, position)
            
            #CHECK IF WON
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print ('Player Two has won!!!')
                game_on=False
            
            #CHECK IF THERE IS A TIE
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print ('The game has ended in a TIE!')
                    break
             #NO TIE OR WIN? THEN NEXT PLAYERS TURN       
                else: 
                    turn = 'Player 1'

    
    if not replay():
        break

#BREAK OUT OF THE WHILE LOOP ON REPLAY


# In[ ]:





# In[ ]:




