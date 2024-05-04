import random
print("Hello, welcome to This Amazing game!")
playing = input("Do want to play?\n(answer in no/yes)\n")
if(playing.lower()=="no") : print("Have a nice day!")
else:
    print("Let's play :)")
    def calcluates(a,b):
        if(a==1) :
            if(b==2): return -1
            elif (b==3):return 1
        elif(a==2) :
            if(b==3): return -1
            elif (b==1):return 1
        else:
            if(b==1): return -1
            elif (b==2):return 1
        return 0
    score = 0
    while True:
        
        print('''   ROCK    PAPER   Scissors
    1        2       3   
        ''')
        from random import randint
        x = input('''(If you wanna quit this game enter q otherwise) )
Enter any one of them : ''')
        if(x=="q"): break
        else : x = int(x)
        if(x<1 or x>3):
            raise ValueError("This number is not lies betwwen 1 and 3")
        y = random.randrange(1,3)
        if(y==1): com = "Rock"
        elif (y==2):com = "Paper"
        else : com = "Scissors"
        print(f"Computer choose {com} ")
        cal = calcluates(x,y)
        if(cal==1): 
            print("YOU WON!\n\n")
            score+=1
        elif(cal==-1): print("YOU LOST!\n\n")
        else : print("DRAW!\n\n")
        print("____________________________________________________\n\n")
    print("\nYour final score is ",score)
    