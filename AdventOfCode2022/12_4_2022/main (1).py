elf = open("ID.txt", "r").read().splitlines()
#print(elf)

id = []
nestedID = []
for i in range(0, len(elf)):  
  for j in range(0, len(elf[i])):
    if elf[i][j] == ",":
      comma = elf[i].index(",")
      id.append(elf[i][0:comma])
      id.append(elf[i][comma:len(elf[i])])
                
      nestedID.append(id)
      id = []
#print(nestedID)

#use greater than/equal to comparison
#2nd id in each nest is always two-digit except for 3 length lists
count = 0
for i in range(0, len(nestedID)):
   

  if len(nestedID[i][0])== 3:
    pair1Number1 = int(nestedID[i][0][0:1])
    pair1Number2 = int(nestedID[i][0][2:3])

  
    print(pair1Number1, "--",pair1Number2)

  elif len(nestedID[i][0]) == 4:
    pair1Number1 = int(nestedID[i][0][0:1])
    pair1Number2 = int(nestedID[i][0][2:4])
    print(pair1Number1, "--",pair1Number2)
  elif len(nestedID[i][0]) == 5:
     pair1Number1 = int(nestedID[i][0][0:2])
     pair1Number2 = int(nestedID[i][0][3:5])
     print(pair1Number1, "--",pair1Number2)
  else:
    print("What")


  
  
  if len(nestedID[i][1]) == 4:
     # pair2Number2 = 
    pair2Number1 = int(nestedID[i][1][1:2])
    pair2Number2 = int(nestedID[i][1][3:4])

    print(pair2Number1, "--",pair2Number2)
    #dont forget to conver to int
  elif len(nestedID[i][1]) == 5:
    pair2Number1 = int(nestedID[i][1][1:2])
    pair2Number2 = int(nestedID[i][1][3:5])
    print(pair2Number1, "--",pair2Number2)
      
  elif len(nestedID[i][1]) == 6:
     pair2Number1 = int(nestedID[i][1][1:3])
     pair2Number2 = int(nestedID[i][1][4:6])
     print(pair2Number1, "--",pair2Number2)
  else:
     print("What")

  #solves for overlap of any kind v
    
  if pair1Number1 >= pair2Number1:
    if pair1Number1<=pair2Number2:
      count+=1
      print("overlaps")
    else:
      print("no")
  elif pair2Number1 >= pair1Number1:
     if pair2Number1 <=pair1Number2:
       count+=1
       print("OVERLAPS")
     else:
       print("nnno")
  else:
    print("no overlaps")

#this below solves for complete overlap v
    
'''
  if pair1Number1 < pair2Number1:
    if pair1Number2 >= pair2Number2:
      count +=1
      print(pair1Number1,"<= ", pair2Number1)
      print(pair1Number2, ">=", pair2Number2)
  
    else:
      print("no")
  elif pair1Number1 == pair2Number1:
    
      print("first nums are euqal")
    
      count+=1    
    
  elif pair2Number1 < pair1Number1:
    if pair2Number2 >=pair1Number2:
      print(pair2Number1,"<= ", pair1Number1)
      print(pair2Number2, ">=", pair1Number2)
      count+=1
    else:
      print("no!")
  else:
    print("either does not cover range")
    
print(count)
    
    
  #for j in range(0, len(nestedID[i])):
'''
print(count)