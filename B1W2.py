#3.1
names=["Koen","Zahir","Kruijt"]
for name in names:
	print(name)
 
#3.2
for name in names:
	print("Hi "+name)
 
#3.3
transportModes=["car","bike","bus","train"]
for types in transportModes:
	print("I would like to own a "+types)

#3.4
people=["mama","papa","zus","opa","oma","tante","oom"]
for person in people:
 	print(person.capitalize() + " is invited to dinner")
  
#3.5
print(people[0]+" can't come to dinner")
people[0]="vriend"
for person in people:
 	print(person.capitalize() + " is invited to dinner")

#3.6
print("I found a bigger table")
people.append("vriendin")
people.insert(0,"schoonmoeder")
people.insert(3,"schoonvader")

for person in people:
 	print(person.capitalize() + " is invited to dinner")
  
#for 3.9 copy the people list
people39=people[:]
  
#3.7
print("I can only invite two people")
while len(people)>2:
 	print(people.pop() + " can't come to dinner")

for person in people:
 	print(person.capitalize() + " is invited to dinner")

for i in range(len(people)):
 	del people[i-1]
print(people)

#3.8
places=["Amsterdam","New York","Tokyo","London","Paris"]
print(places)
print(sorted(places))
print(places)
print(sorted(places,reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)


#3.9
print("there were " + str(len(people39)) + " people invited to dinner at one point (see comment to figure where the copy was made)")

#3.10 every function really???

# sort, sorted, reverse, remove, pop, del, insert, append, len

thingsIWant = ["new phone","money","toys","RTX 4090","friends","a boyfriend"]

def printThings():
	want="i want a "
	for thing in thingsIWant:
		want=want + thing + ", "
	print(want)
 
printThings()

print("i already have a friend so remove that from the list")
thingsIWant.remove("friends")
printThings()

print("i want a helicopter so add that to the list")
thingsIWant.append("helicopter")

print("i want a porche really bad so add it to the front of the list")
thingsIWant.insert(0,"porche")
printThings()

thingMyFriendGotMe=thingsIWant.pop(5)
print("my friend got me a " + thingMyFriendGotMe + " so removed that from the list")

print("time to do sorts wich are boring so i will not make up a bs reason to do them")
print("sort")
thingsIWant.sort()
printThings()
print("reverse sort")
thingsIWant.sort(reverse=True)
printThings()
thingsIWant.reverse()
print("reverse")
printThings()

print("there are " + str(len(thingsIWant)) + " things on my list")


#3.11
print("so i need to get an index error here goes nothing")
listNumbers=[1,2,3,4,5]
#print(listNumbers["pain"]) #<-- causes error which is disabled for now because i want to see the rest of the code in working order

#4.1
#please look at all work before this i will not do this

#4.2
#check 4.1

#4.3
for i in range(1,21):
	print(i)
 
#4.4
#for i in range(1,1000001): print(i) #<-- this is a lot of numbers and to prevent console spam i will not print them all

#4.5
listWithMillionNumbers=list(range(1,1000001))
print("the min is " + str(min(listWithMillionNumbers)) + ", the max is " + str(max(listWithMillionNumbers)))

from time import time
intialTime=time()
sumOfMillionNumbers=sum(listWithMillionNumbers)
finalTime=time()



print("python took " + str(finalTime-intialTime) + " seconds to sum 1 million numbers, which btw was " + str(sumOfMillionNumbers))
ptime=finalTime-intialTime

import numpy as np

#npList=np.array(listWithMillionNumbers)
npList=np.arange(1,1000001,1,dtype=np.int64)

intialTime=time()
npSum=np.sum(npList)
finalTime=time()

print("numpy took " + str(finalTime-intialTime) + " seconds to sum 1 million numbers, which btw was " + str(npSum))
nptime=finalTime-intialTime

#print("numpy was " + str(ptime/nptime) + " times faster than python")

#4.6
odds=list(range(1,21,2))
for odd in odds:
	print(odd)
 
#4.7
threeMultiples=list(range(3,31,3))
for threeMultiple in threeMultiples:
	print(threeMultiple)
 
#4.8
oneTen=list(range(1,11))
cubeList=[]
for number in oneTen:
	cubeList.append(number**3)


for cube in cubeList:
	print(cube)
	
#4.9
cubeList=[number**3 for number in range(1,11)]

#4.10
#using copied list from 3.9
print("the first three items in the list are: " + str(people39[:3]))
print("three items from the middle of the list are: " + str(people39[3:6]))
print("the last three items in the list are: " + str(people39[-3:]))

#4.11
myPizza=["pepperoni","cheese","hawaiian"]
friendPizza=myPizza[:]
friendPizza.append("meat lovers")
myPizza.append("veggie")
print("my favorite pizzas are:")
print(myPizza)
print("my friends favorite pizzas are:")
print(friendPizza)

#5.1
thing="car"
print("is thing == 'car'? I predict True.")
print(thing=="car")
print("thing is not equal to 'bike' so i predict False")
print(thing=="bike")

#5.2
#nee

#5.3 Gebruik hiervoor alsjeblieft lists of dictionarys
alienColor="green"
if alienColor=="green":
	print("you just earned 5 points")
 
#5.4
if alienColor=="green":
	print("you just earned 5 points")
else:
	print("you just earned 10 points")


#5.5
if alienColor=="green":
	print("you just earned 5 points")
elif alienColor=="yellow":
	print("you just earned 10 points")
elif alienColor=="red":
	print("you just earned 15 points")
	
#5.6
import random

age=random.randint(0,100)
if age<2:
	print("you are a baby")
elif age<4:
	print("you are a toddler")
elif age<13:
	print("you are a kid")
elif age<20:
	print("you are a teenager")
elif age<65:
	print("you are an adult")
else:
	print("you are an elder")
	
#5.7
fruits=["apple","banana","orange","pear","grape","watermelon","pineapple","strawberry","kiwi","mango"]
favFruits=["apple","banana","orange"]
for fruit in fruits:
	if fruit in favFruits:
		print("you really like " + fruit)

#5.11
ordinals=[str(i)+"th" for i in range(1,10)]
ordinals[0]="1st"
ordinals[1]="2nd"
ordinals[2]="3rd"
for ordinal in ordinals:
	print(ordinal)

#5.12
#echt niet dit is letterlijk "kijk mij ik ben beter omdat ik spaties gebruik" en ik steun dit niet

#5.13
#zie antwoord van H1


