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