import random
def getword():
    words=['rat','same','warm','lovable','kind','honesty','beautiful','meaningful','gentle','possessive','generous','relation','photography','image']
    return random.choice(words).upper()
import time
name = input("What is your name? ")
game=1
w=0
f=0
games=0
while game==1:
    games+=1
    print("Hello, " + name, "Time to play hangman!")
    time.sleep(1)
    print("Start guessing...")
    time.sleep(0.5)
    word =getword()
    guesses = ''
    turns = 10
    while turns > 0:         
        failed = 0             
        for char in word:      
            if char in guesses:    
                print(char,end=" ")    
            else:
                print ("*",end=" ")    
                failed += 1    
        if failed == 0:
            w+=1
            print ("\nYou won")
            break              
        guess = input("guess a character:")
        guess=guess.upper()
        guesses += guess                    
        if guess not in word:  
     
         
            turns -= 1        
     
        
            print ("Wrong")    
     
        
            print("You have", + turns, 'more guesses') 
     
        
            if turns == 0:           
        
                f+=1
                print("You Loose")
                print("The correct answer is ",word)
    game1=input("Do you want to play another game. Say yes or No")
    game1=game1.upper()
    if game1=='YES':
        game=1
    else:
        game=0
print("--------GAME SUMMARY--------------")        
print("No of games playes= ",games)
print("No of wins= ",w)
print("No of loses= ",f) 
