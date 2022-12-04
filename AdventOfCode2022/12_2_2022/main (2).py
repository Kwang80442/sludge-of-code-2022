

elfGame = open("game.text")
elfGame2 = open("game.text", "r").read().splitlines()

#print(elfGame2)

#read = elfGame.read()
#print(read[1])
group1 = []
group2 = []
count2 = 1
x = 4
'''
you lose is 1 point
you win is 6 points
you draw is 3 points
'''

'''
opponent:
A is rock
B is paper
C is scissors

you:
X for rock
Y for paper
Z for scissors

beats '''

yourPointsRound = 0;
opponentPointsRound = 0;
sumPoints = 0;



for i in range(0, len(elfGame2)):
  #print(elfGame2[i])
  
  if elfGame2[i][2] == "X":
    # if you chose rock, you should lose, so if you haven't, you should chose a losing symbol from oppponent
    if elfGame2[i][0] == "A":
      # this is a tie ---- > turn decision to scissors -- scissors is 3 points ---> add 3 and 0 (losing point)
      yourPointsRound += 3 + 0
      
    elif elfGame2[i][0] == "B":
      # rock vs paper
      #rock loses
      #stick with rock
      yourPointsRound += 1 + 0
    elif elfGame2[i][0] == "C":
      # rocck vs paper
      # rock wins
      # stick with rock
      yourPointsRound += 2 + 0
    else:
      print("oopsy daisy")
    
  elif elfGame2[i][2] == "Y":
  # if you chose paper, you shuold draw, and if you haven't, choose the same symbol as opponent
     if elfGame2[i][0] == "A":
       # paper vs rock
       # choose rock
       # add draw points
       yourPointsRound += 1 + 3
     elif elfGame2[i][0] == "B":
       # paper vs paper
       yourPointsRound += 2 + 3
     elif elfGame2[i][0] == "C":
       # paper vs scissorrs
       #choose scissors
       yourPointsRound += 3 + 3
     else:
       print("oopsy daisy")
      
  elif elfGame2[i][2] == "Z":
    # if you chose scissors, you should win, and if you haven't, choose a winning symbol
      if elfGame2[i][0] == "A":
        # scissors vs rock
        # chose paper
        # add win point
        yourPointsRound += 2 + 6
      elif elfGame2[i][0] == "B":
        # scissors vs paper
        #keep scissors
        yourPointsRound += 3 + 6
      elif elfGame2[i][0] == "C":
        # scissors vs scissors
        # cose rock
        yourPointsRound += 1 + 6


# this one is for normal game
'''
  if elfGame2[i][2] == "X":
    yourPointsRound +=1
    
  
    yourPointsRound += 0
  elif elfGame2[i][2] == "Y":
    yourPointsRound +=2
   
  elif elfGame2[i][2] == "Z":
    yourPointsRound +=3

  

  if elfGame2[i][2] == "X" and elfGame2[i][0] == "A":
    
    print("tie")
    yourPointsRound +=3;
    opponentPointsRound +=3;
  elif elfGame2[i][2] == "Y" and elfGame2[i][0] == "B":
    print("Tie")
    yourPointsRound +=3;
    opponentPointsRound +=3;
  elif elfGame2[i][2] == "Z" and elfGame2[i][0] == "C":
    print("Tie")
    yourPointsRound +=3;
    opponentPointsRound +=3

  elif elfGame2[i][2] == "X" and elfGame2[i][0] == "B":
      print("rock does not beat paper")
      yourPointsRound += 0
      opponentPointsRound += 6
  elif elfGame2[i][2] == "X" and elfGame2[i][0] == "C":
      print("rock beats scissors")
      yourPointsRound += 6
      opponentPointsRound +=0
      
  elif elfGame2[i][2] == "Y" and elfGame2[i][0] == "A":
      print("Paper beats rock") 
      yourPointsRound += 6
      opponentPointsRound +=1
  elif elfGame2[i][2] == "Y" and elfGame2[i][0] == "C":
      print("Paper does not beat scissors  ")
      yourPointsRound +=0
      opponentPointsRound +=6
  elif elfGame2[i][2] == "Z" and elfGame2[i][0] == "A":
      yourPointsRound +=0
      opponentPointsRound+=6
      print("Scissors do not beat rock")
    
  elif elfGame2[i][2] == "Z" and elfGame2[i][0] == "B":
      
      yourPointsRound+=6
      print("Scissors beat paper")
  else:
    print("You did something wrong")

'''
print(yourPointsRound)
