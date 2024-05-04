import random
def roll():
    roll = random.randrange(1,6)
    return roll

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")
    
max_score = 50
player_scores = []
# player_scores 

for i in range(players):
    total_score = 0
    player_score = 0
    print("Chance for player",i+1,"\n")
    while total_score<=max_score:
        temp = input("If you wants to pass the chance just type q\nIf you wants to roll the dice type y!\n\n")
        temp = temp.lower()
        if temp=='q' : break
        if temp=='y':
            player_score = roll()
            if player_score==1 : 
                print("Roll = ",player_score,"\nOh shit dice shows one you loss all your points\n\n")
                total_score = 0
                break
            else : 
                print("Roll = ",player_score)
                total_score+= player_score
                print("Your total score now",total_score,"\n\n")
        else: print("Invalid input!\n\n")
    player_scores.append(total_score)

print("Player scores!\n",player_scores)
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
if max_score == 0: 
    print("Draw!!")
else : print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)
