#6.1
me={"name":"Koen","age":18,"city":"Delft"}
for key,value in me.items():
	print(key + ": " + str(value))
 
#6.3
prgrammingConcepts={"if":"if statements are used to check if a condition is true or false","for":"for loops are used to iterate over a list","while":"while loops are used to repeat a block of code while a condition is true"}
for key,value in prgrammingConcepts.items():
	print(key + ": " + value)

#6.4
#letterlijk al gedaan

#6.5
river={"nile":"egypt","amazon":"brazil","mississippi":"america"}
for key,value in river.items():
	print("The " + key + " runs through " + value)

for key in river.keys():
	print(key)

for value in river.values():
	print(value)

#6.6
favoriteLanguages={"jen":"python","sarah":"c","edward":"ruby","phil":"python"}
people=["jen","sarah","edward","phil","koen"]
for person in people:
	if person in favoriteLanguages.keys():
		print(person + " thank you for taking the poll")
	else:
		print(person + " please take the poll")
  
#6.7
people=[{"name":"Koen","age":18,"city":"Delft"},{"name":"Jen","age":20,"city":"Amsterdam"},{"name":"Sarah","age":19,"city":"Rotterdam"}]
for person in people:
	for key,value in person.items():
		print(key + ": " + str(value))
	print("\n")

#6.11
cities={"Amsterdam":
		{"country":"Netherlands","population":800000,
	 	"fact":"Amsterdam is the capital of the Netherlands"},
	"Rotterdam":
		{"country":"Netherlands",
		 "population":600000,
		 "fact":"Rotterdam is the second largest city of the Netherlands"},
	"Delft":
		{"country":"Netherlands",
		 "population":100000,
		 "fact":"Delft is the city where the famous painter Vermeer was born"}
	}

def printShit(t): #selfrefrencing function to print shit
	for key,value in t.items():
		if type(value) is dict or type(value) is list:
			print(key + ":")
			printShit(value)
		else:
			print(key + ": " + str(value))

printShit(cities)

#6.12
#check 6.11 ik vind dat het al prima is


#7.2
people=input("How many people are in your dinner group? ")
if int(people) > 8:
	print("You have to wait for a table")
else:
	print("Your table is ready")
	
#7.3
inputNumber=input("Enter a number: ")

if int(inputNumber) % 10 == 0:
	print("The number is a multiple of 10")
else:
	print("The number is not a multiple of 10")
 
#7.4
while True:
	topping=input("Enter a topping for your pizza: ")
	if topping == "quit":
		break
	else:
		print("I will add " + topping + " to your pizza")

#7.5
age=input("Enter your age: ")
pricesPerAgeGroup={"baby":0,"child":10,"adult":15}
AgeGroup=[3,12]

for i in range(0,len(AgeGroup)):
	if int(age) <= AgeGroup[i]:
		print("Your ticket will cost " + str(pricesPerAgeGroup[list(pricesPerAgeGroup.keys())[i]]))
		break

#7.6
#nee

#7.7
#while True:
#    print("cope")

#7.8
orders=["blt","tuna","ham","cheese","egg","bacon"]
finishedOrders=[]
for order in orders:
	print("I made your " + order + " sandwich")
	finishedOrders.append(order)
	orders.remove(order)

print("All orders are finished")

#7.9
orders=["blt","tuna","ham","cheese","egg","bacon","pastrami","pastrami","pastrami"]

def pastramiYN(order):
	if order!="pastrami":
		return True

orders=filter(pastramiYN,orders)


#8.1
def displayMessage():
	print("I am learning nothing")
 
#8.2
def printBook(title):
	print("My favorite book is " + title)
  
  
#8.3
def makeShirt(size,message):
	print("The shirt is size " + size + " and has the message " + message)
 
 
#8.4
def makeShirt(size="large",message="I love Python"):
	print("The shirt is size " + size + " and has the message " + message)
 
#8.5
def printCities(city,country):
	print(city + " is in " + country)
 
#8.6
def cityCountry(city,country):
	return city + ", " + country

places=[["Amsterdam","Netherlands"],["Rotterdam","Netherlands"],["Delft","Netherlands"]]

for place in places:
	print(cityCountry(place[0],place[1]))

#8.7
def makeAlbum(artist,album,songs=None):
	album={"artist":artist,"album":album}
	if songs:
		album["songs"]=songs
	return album

#8.8
while True:
	artist=input("Enter the name of an artist: ")
	if artist == "quit":
		break
	album=input("Enter the name of an album: ")
	if album == "quit":
		break
	songs=input("Enter the number of songs: ")
	if songs == "quit":
		break
	print(makeAlbum(artist,album,songs))
 
#8.9
magiciansList=["Harry Houdini","David Blaine","David Copperfield"]

def printMagicians(magicians):
	for magician in magicians:
		print(magician)
  
#8.10
def makeGreat(magicians):
	for i in range(0,len(magicians)):
		magicians[i]="The Great " + magicians[i]
	return magicians

#8.11
#already done??


#8.15

from lib import printList as pl

listToPrint=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
pl(listToPrint)

#8.16
#nee