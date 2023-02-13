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
