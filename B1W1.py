#1.2

print("Hello World")
#print("Hello World"5)

#Werkt niet omdat er een 5 staat na de "Hello World"

#1.3
#iets dat op het moment relevant is en inkomen genereert zodat ik hier aan hoef de denken

#2.1
str="Hello World"
print(str)


#2.2
str="Hello World"
print(str)
str=str+"!"
print(str)

#2.3
table={"name":"John","age":"25","city":"Amsterdam"}
print("Hi " + table["name"] + " you are " + table["age"] + " years old and you live in " + table["city"] + ", now give me money!")

#2.4
print(table["name"].lower() + table["name"].upper() + table["name"].capitalize())

#2.5
table={"author":"Albert Einstein","quote":"A person who never made a mistake never tried anything new."}
print(table["author"] + " once said: " + "\x1B[3m" + "\"" + table["quote"] + "\"" + "\x1B[0m")

#2.6 ga ik niet maken heb praktisch dat al gedaan in 2.5

#2.7
name="   Koen \tZahir\n Kruijt    "
print(name.strip())
print(name.lstrip())
print(name.rstrip())

#2.8
print(5+3)
print(2*4)
print(16/2)
print(10-2)

#2.9 dit zou moeten werken maar doet het niet
number=54
print("My favorite number is "+str(number))

#2.10 cant see that comments exist in python

#2.11
import this