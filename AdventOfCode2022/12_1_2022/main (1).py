##elf
''' this code is not very opotomized
since I haven't used python for a very long time
but still decided to use this language over java
and just wanted to do the first day for fun
you could probably simplify some for loops
I just have a ton because I was worried that overlapping
the nesting, stripping the \n, and converting to int in
just one or two for loops would cause problems
did this for 2 star lol
I numbered each grouping of calories 
too extra work but /shrug'''

numbers = open("elves.text")
numberList = []
numberListStrip = []
newNumbers = [x[:-1] for x in numbers]
elfAndSums = {}

for i in newNumbers:
  
  numberListStrip.append(i)
  
  if i == "":
    numberList.append(numberListStrip)
    eachNumberList = []


group2 = []
nested = []
intgroup2 = []

for i in numberListStrip:
  group2.append(i)
  
  
  if i == '':    
    for j in range(0, len(group2)-1):
  
      if group2[j] == "":
         group2.remove("")
        
      intgroup2.append(int(group2[j]))
      
    nested.append(intgroup2)
    
    group2 = []
    intgroup2=[]
    
elfNumAndSum = {}

count = 1
eachSum = 0

for i in range(0, len(nested)):
  
    eachSum =sum(nested[i])
  
    elfNumAndSum[count] = eachSum   
    
    count +=1

print(nested)
count2 = 1



for i in elfNumAndSum:
  print(count2, elfNumAndSum[count2])

  count2 +=1
  
a = dict(sorted(elfNumAndSum.items(), key=lambda item: item[1]))

print(a)