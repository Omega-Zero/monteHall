# Monte Hall Simulation - Saw a Vsauce video: https://www.youtube.com/watch?v=TVq2ivVpZgQ
# Decided to try and simulate the "problem" and see what happens

import random

def montesimstay(rounds):

    wins = 0
    losses = 0
            
    for currentround in range(rounds): 

        choice = 0

        door1 = False
        door2 = False
        door3 = False
        
        #Chooses winning door
        door = random.randint(1, 3)
        if door == 1:
            door1 = True
        elif door == 2:
            door2 = True
        else:
            door3 = True


        
        #"Eliminate" one door
        choice = random.randint(1, 3)
        if choice == 1:
            if door2 == True:
                door3 = None
            else:
                door2 = None
                
        elif choice == 2:
            if door1 == True:
                door3 = None
            else:
                door1 = None

        else:
            if door1 == True:
                door2 = None
            else:
                door1 = None

        
        #Win check
        if choice == 1 and door1 == True:
            wins = wins + 1
            
        elif choice == 2 and door2 == True:
            wins = wins + 1
        elif choice == 3 and door3 == True:
            wins = wins + 1
        else:
            losses = losses + 1 
        
         

    winpercent = ( wins /(wins+losses) ) * 100    

    print (" Wins: " + str(wins) + " Losses " + str(losses))
    print ("You won " + str(winpercent)+ "% of the time by staying with your choice")


def montesimother(rounds):
    wins = 0
    losses = 0
            
    for currentround in range(rounds): 

        choice = 0

        door1 = False
        door2 = False
        door3 = False
        
        #Chooses winning door
        door = random.randint(1, 3)
        if door == 1:
            door1 = True
        elif door == 2:
            door2 = True
        else:
            door3 = True


        
        #"Eliminate" one door
        choice = random.randint(1, 3)
        if choice == 1:
            if door2 == True:
                door3 = None
            else:
                door2 = None
                
        elif choice == 2:
            if door1 == True:
                door3 = None
            else:
                door1 = None

        else:
            if door1 == True:
                door2 = None
            else:
                door1 = None


        #Change to other door
        if choice == 1 and door2 == None:
            choice = 3
        elif choice == 1 and door3 == None:
            choice = 2
                
        elif choice == 2 and door1 == None:
            choice = 3
        elif choice == 2 and door3 == None:
            choice = 1

        elif choice == 3 and door1 == None:
            choice = 2
        elif choice == 3 and door2 == None:
            choice = 1

        
        #Win check
        if choice == 1 and door1 == True:
            wins = wins + 1
            
        elif choice == 2 and door2 == True:
            wins = wins + 1
        elif choice == 3 and door3 == True:
            wins = wins + 1
        else:
            losses = losses + 1 
        
         

    winpercent = ( wins /(wins+losses) ) * 100    

    print (" Wins: " + str(wins) + " Losses " + str(losses))
    print ("You won " + str(winpercent)+ "% of the time by changing from your original choice")



    

def printmontesimstay(rounds):

    wins = 0
    losses = 0
            
    for currentround in range(rounds): 
        print ("-----round-----", currentround+1)
        choice = 0

        door1 = False
        door2 = False
        door3 = False
        
        #Chooses winning door
        door = random.randint(1, 3)
        if door == 1:
            door1 = True
        elif door == 2:
            door2 = True
        else:
            door3 = True
        print("the winning door is:", door)

        
        #"Eliminate" one door
        choice = random.randint(1, 3)
        print("you chose a random door:", choice, "and stay")
        if choice == 1:
            if door2 == True:
                door3 = None
            else:
                door2 = None
                
        elif choice == 2:
            if door1 == True:
                door3 = None
            else:
                door1 = None

        else:
            if door1 == True:
                door2 = None
            else:
                door1 = None

        
        #Win check
        if choice == 1 and door1 == True:
            wins = wins + 1
            print("you win!")
        elif choice == 2 and door2 == True:
            wins = wins + 1
            print("you win!")
        elif choice == 3 and door3 == True:
            wins = wins + 1
            print("you win!")
        else:
            losses = losses + 1
            print("you lose!")        
        print("current overall | wins:", wins, "losses:", losses)         

    winpercent = ( wins /(wins+losses) ) * 100    
    print("-------------Final Results: Staying With Your Origional Door-------------")
    print ("Wins: " + str(wins) + " Losses " + str(losses))
    print ("You won " + str(winpercent)+ "% of the time by staying with your choice")






def printmontesimother(rounds):
    wins = 0
    losses = 0
            
    for currentround in range(rounds): 
        print ("-----round-----", currentround+1)
        choice = 0

        door1 = False
        door2 = False
        door3 = False
        
        #Chooses winning door
        door = random.randint(1, 3)
        print("the winning door is:",door)
        if door == 1:
            door1 = True
        elif door == 2:
            door2 = True
        else:
            door3 = True


        
        #"Eliminate" one door
        choice = random.randint(1, 3)
        print("you choose door:",  choice)
        if choice == 1:
            if door2 == True:
                door3 = None
            else:
                door2 = None
                
        elif choice == 2:
            if door1 == True:
                door3 = None
            else:
                door1 = None

        else:
            if door1 == True:
                door2 = None
            else:
                door1 = None


        #Change to other door
        if choice == 1 and door2 == None:
            choice = 3
            print("you change door to door:", choice)
        elif choice == 1 and door3 == None:
            choice = 2
            print("you change door to door:", choice)
        elif choice == 2 and door1 == None:
            choice = 3
            print("you change door to door:", choice)
        elif choice == 2 and door3 == None:
            choice = 1
            print("you change door to door:", choice)
        elif choice == 3 and door1 == None:
            choice = 2
            print("you change door to door:", choice)
        elif choice == 3 and door2 == None:
            choice = 1
            print("you change door to door: ", choice)

        
        #Win check
        if choice == 1 and door1 == True:
            wins = wins + 1
            print("you win!")
        elif choice == 2 and door2 == True:
            wins = wins + 1
            print("you win!")
        elif choice == 3 and door3 == True:
            wins = wins + 1
            print("you win!")
        else:
            losses = losses + 1
            print("you lose!")
        print("current overall | wins:", wins, "losses:", losses)

    winpercent = ( wins /(wins+losses) ) * 100    
    print("------------------Final Results: Swithing From Origional Door------------------")
    print ("Wins: " + str(wins) + " Losses " + str(losses))
    print ("You won " + str(winpercent)+ "% of the time by changing from your original choice")





