#9.1

class restaurant():
	def __init__(self, name, cuisine):
		self.name = name
		self.cuisine = cuisine
		self.number_served = 0 #9.4

	def describe_restaurant(self):
		print("The restaurant's name is " + self.name.title() + ".")
		print("The restaurant's cuisine is " + self.cuisine.title() + ".")

	def open_restaurant(self):
		print("The restaurant is open.")
	
	def set_number_served(self, number_served): #9.4
		self.number_served = number_served
	
	def increment_number_served(self, number_served=1):
		self.number_served += number_served
  
  
#9.2

restaurant1 = restaurant('kfc', 'chicken')
restaurant2 = restaurant('mcdonalds', 'burgers')
restaurant3 = restaurant('taco bell', 'tacos')


restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

#9.4
restaurant94 = restaurant('ruif', 'eetcafe')

restaurant94.set_number_served(10)
print("The restaurant has served " + str(restaurant94.number_served) + " people.")
restaurant94.increment_number_served()
print("The restaurant has served " + str(restaurant94.number_served) + " people.")



#9.6
class iceCreamStand(restaurant):
	def __init__(self, name, cuisine):
		super().__init__(name, cuisine)
		self.flavors = ['chocolate', 'vanilla', 'strawberry']
		
	def show_flavors(self):
		print("The flavors are:")
		for flavor in self.flavors:
			print(flavor.title())
   
iceCreamStand1 = iceCreamStand('het bolletje', 'ijs')
iceCreamStand1.show_flavors()


#9.9


#car class
class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
#electric car class + battery class

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")  
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    
    def upgrade_battery(self): #HERE IS THE UPGRADE METHOD
        """Upgrade the battery if possible."""
        if self.battery_size >= 85:
            self.battery_size = 85
        else:
            print("The battery is already upgraded.")
    
        
class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


#9.10
from restaurant import restaurant

restaurant1 = restaurant('kfc', 'chicken')
restaurant1.open_restaurant()

#9.13
#nee

#9.14
class die():
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll_die(self):
        import random
        print(random.randint(1, self.sides))
        
die1 = die()
for i in range(10):
    die1.roll_die()


#9.15
#refrence datetime & time modules from PyAlarm.py (STACK)


#10.5 to 10.12

#10.5

#import filesystem, check if file exists, if not create it then start storing answers in it until user enters 'quit'

import os

filename = 'poll.txt'

if os.path.exists(filename):
    print("enter responses")
else:
    open(filename, 'w')
    print("file created, enter responses")
    
while True:
    f=open(filename, 'a')
    i=input("why do you like programming? ")
    if i == 'quit':
        f.close()
        break
    f.write(i+"\n")
    
    
#10.6
print("enter two numbers to add")
i1=input("first number: ")
i2=input("second number: ")

try :
    i1=int(i1)
    i2=int(i2)
except ValueError:
    print("please enter a number with numbers not letters")
else:
    print(i1+i2)

    
    
#10.7
while True:
    i1=input("first number: ")
    if i1 == 'quit': break
    i2=input("second number: ")
    if i2 == 'quit': break
    
    try :
        i1=int(i1)
        i2=int(i2)
    except ValueError:
        print("please enter a number with numbers not letters")
    else:
        print(i1+i2)

    
#10.8
open('cats.txt', 'w').write("cat1\ncat2\ncat3")
open('dogs.txt', 'w').write("dog1\ndog2\ndog3")

def print_file(filename):
    try:
        f=open(filename, 'r')
    except FileNotFoundError:
        print("file not found")
    else:
        for line in f:
            print(line)
        f.close()

print_file('cats.txt')
print_file('dogs.txt')


#10.9
#just remove the print statement in the except block......


#10.10
def countString(filename, string, encoding='utf-8'):
    try:
        f=open(filename, 'r', encoding=encoding)
    except FileNotFoundError:
        print("file not found")
    except UnicodeDecodeError:
        print("file is not in "+encoding+" encoding, try another encoding")
    else:
        count=0
        for line in f:
            count+=line.lower().count(string)
        print("the string "+string+" is found "+str(count)+" times in the file "+filename)
        f.close()
        
        
countString('book.txt', 'the')

#10.11
import json
file="fav_number.json"

i=input("what is your favorite number? ")

#import seperate_file.py and def as function
with open(file, 'w') as f:
    json.dump(i, f)


with open(file) as f:
    fav_number=json.load(f)
    print("your favorite number is "+str(fav_number))
        
        
        
#10.12


#zie 10-11

#11.1

import unittest
import cityFunctions as cf

class testCityNames(unittest.TestCase):

    def test_cityName(self): #will fail due to 11.2
        expect="Amsterdam, Netherlands"
        inputData=["amsterdam","netherlands"]
        
        output=cf.formatCityName(*inputData)
        
        self.assertEqual(output,expect)
        
        
    def test_cityWithPopulation(self): #11.2
        expect="Amsterdam, Netherlands - 1000000"
        inputData=["amsterdam","netherlands",1000000]
        
        output=cf.formatCityName(*inputData)
        
        self.assertEqual(output,expect)
        
        
unittest.main()

