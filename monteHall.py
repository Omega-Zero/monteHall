# Monte Hall Simulation
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
    return 0





