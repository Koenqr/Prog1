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
