# Snake Water and Gun Game
'''
1 for snake
-1 for water 
0 for gun
'''
import random

computer = random.choice([-1,0,1])
youstr = input('''
    s for snake 
    w for water
    g for gun 
    
    Enter your choice between s/w/g :''')

youDict = {"s":1, "w": -1, "g": 0}
revDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

print(f"You Choose {revDict[you]}\nComputer Choose {revDict[computer]}")

if(computer == you):
    print("its a draw")
    
else:
    if(computer == -1 and you == 1):
        print("you win")

    elif(computer == -1 and you == 0):
        print("you lose")    

    elif(computer == 1 and you == -1):
        print("you lose")
        
    elif(computer == 1 and you == 0):
        print("you win")  
        
    elif(computer == 0 and you == 1):
        print("you lose") 
        
    elif(computer == 0 and you == -1):
        print("you win")       

    else:
        print("something went wrong")     