#!/usr/bin/env python
# coding: utf-8

# In[1]:


board =['' for x in range(10)]


# In[2]:


def insertLetter(letter,pos):
    board[pos]=letter


# In[3]:


def printBoard(board):
    print("   |    |   ")
    print("  "+board[1]+" |"+board[2]+"   | "+board[3])
    print("   |    |   ")
    print("------------")
    print("   |    |   ")
    print(" "+board[4]+"  |"+board[5]+"   | "+board[6])
    print("   |    |   ")
    print("------------")
    print("   |    |   ")
    print(" "+board[7]+"  |"+board[8]+"   | "+board[9])
    print("   |    |   ")
   

    


# In[4]:


def spaceIsFree(pos):
    return board[pos]==' '


# In[5]:


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
    


# In[6]:


def isWinner(b,l):
    return ((b[1]== l and b[2]== l and b[3]== l) or
            (b[4]== l and b[5]== l and b[6]== l) or 
            (b[7]== l and b[8]== l and b[9]== l) or 
            (b[1]== l and b[5]== l and b[9]== l) or
            (b[7]== l and b[5]== l and b[3]== l) or
            (b[1]== l and b[4]== l and b[7]== l) or
            (b[5]== l and b[2]== l and b[8]== l) or
            (b[6]== l and b[9]== l and b[3]== l))
    


# In[7]:


def playerMove(board):
     run =True
     while run:
         move = input("Enter position to input 'X'(1-9):")
         
         try:
             move= int(move)
             if move > 0 and move < 10:
                 if spaceIsFree(move):
                     run = False
                     insertLetter('X',move)
                 else:
                     print("Sorry, this space has already been occupied")
             else:
                 print("Enter a valid character ")
                 
             
         except:
            print("Please enter a number. " )


# In[8]:


def computerMove(board):
    
    possibleMoves = [x for x , letter  in enumerate(board) if letter ==' ' and x!=0]
    
    move = 0
    
    for let in ['O','X']:
        for i in possibleMoves:
            boardcopy=board[:]
            boardcopy[i]=let
            if isWinner(boardcopy,let):
                move =i
                return move
            
    cornersOpen=[]
    
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if (len(cornersOpen) > 0):
        move = selectRandom(cornersOpen)
        return move
    
    if 5 in possibleMoves:
        move= 5
        return move
    
    
    edgesOpen=[]
    
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if (len(edgesOpen) > 0):
        move = selectRandom(edgesOpen)
        return move
    
    if 5 in possibleMoves:
        move= 5
        return move


# In[9]:


def selectRandom(li):
    
    import random 
    randommove = random.randrange(0,len(li))
    
    move = li[randommove]
    
    return move


# In[10]:


def main():
    
    print("Welcome to the game !")
    print(printBoard(board))
    
    while (not isBoardFull(board)):
        if (not isWinner(board,'O')):
            playerMove(board)
            printBoard(board)
        else:
            print("Sorry!You lose " )
            break
        
        if (not isWinner(board,'X')):
            move  =computerMove(board)
            if move ==0:
                print(" " )
            else:
                insertLetter('O',move)
                print("Computer placed a move on position : ",move)
            
                printBoard(board)
        else:
            print("Yay! You won!")
            break
        
        
    if isBoardFull(board):
        print("Tie game ")
  


# In[ ]:


while True:

        if((input("Do you want to play?(Y/N) : "))=='Y'):
            board=[' ' for  i in range(10)]
            print("------------------------------")
            main()
        else:
            break
    


# In[ ]:




