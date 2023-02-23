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