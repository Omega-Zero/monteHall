# Monte Hall Simulation
import random



def montesimstay(rounds):

    wins = 0
    losses = 0
    
    door1 = False
    door2 = False
    door3 = False

    choice = 0    
         
    for currentRound in range(rounds): 

        #Chooses wining door
        if door1 == False:
            if random.randint(0, 1) == 1:
                door1 = True
        elif door2 == False:
            if random.randint(0, 1) == 1:
                door1 = True
        else:
             door3 = True


        choice = random.randint(1, 3)

        print (" Wins: " + str(wins) + " Losses " + str(losses) )



def montesimother(rounds):
    return 0





