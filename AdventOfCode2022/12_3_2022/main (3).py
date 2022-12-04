elf = open("compartment.text", "r").read().splitlines()

#print(elf)

#find the one letter that each compartment shares

#Lowercase item types a through z have priorities 1 through 26.
#Uppercase item types A through Z have priorities 27 through 52.
##

#the only item type that appears in the first and second compartment of the first sack is m


specialLetters = []
'''
cutinHalf = []
compOneAndTwo = []
for i in range(0, len(elf)):
  compLen = len(elf[i])
  compLenHalf = int(compLen / 2)

  cutInHalfComp = elf[i][0:compLenHalf]
  secondHalfComp = elf[i][compLenHalf:compLen]
  #print(cutInHalfComp, "   ", secondHalfComp)
  compOneAndTwo.append([cutInHalfComp, secondHalfComp])

for i in (range(0, len(compOneAndTwo))):
  #then iterate through compartments 1 and 2
  
    print(compOneAndTwo[i][0], "  ", compOneAndTwo[i][1])
    count = 0
    while count < len(compOneAndTwo[i][0]):
      if compOneAndTwo[i][0][count] in compOneAndTwo[i][1]:  
        #print("Special letter:" + compOneAndTwo [i][0][count])
        specialLetters.append(compOneAndTwo[i][0][count])
        break
      count +=1
      
# print(compOneAndTwo)
'''

#print(elf)
#print(specialLetters)
#print(elf)

#this one finds the common letter between every 3 garbgled letters
groupsOfThree = []
allThrees = []

count = 1
for i in range(0, len(elf)):
  
  
  
  groupsOfThree.append(elf[i])
  
  #print(groupsOfThree)
  if count == 3:
    
    allThrees.append(groupsOfThree)
    
    groupsOfThree = []
    count = 1
  else:  
    count +=1


for i in range(0, len(allThrees)):

  count = 0
  while count < len(allThrees[i][0]):
      if allThrees[i][0][count] in allThrees[i][1]:  
          if allThrees[i][0][count] in allThrees[i][2]:
        #print("Special letter:" + compOneAndTwo [i][0][count])
            
            specialLetters.append(allThrees[i][0][count])
            break     
      count +=1

print(specialLetters)
  

#print(allThrees)
#print(groupsOfThree)
specialNumbers = []

for i in range(0, len(specialLetters)):
  if specialLetters[i].islower():
    number = ord(specialLetters[i]) -96
    print(specialLetters[i] + " == ", number)
    specialNumbers.append(number)
  elif specialLetters[i].isupper():
    number = ord(specialLetters[i]) - 38 #subtract from asci to get the right range
    print(specialLetters[i] + " == ", number)
    specialNumbers.append(number)

print(specialNumbers)
print(sum(specialNumbers))
