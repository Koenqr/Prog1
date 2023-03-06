#opdracht 1 voor datum checken

from datetime import datetime as dt


data=[
	{"name":"Jan","birthdate":dt.strptime("2018-12-12","%Y-%m-%d")},
	{"name":"Piet","birthdate":dt.strptime("2015-11-08","%Y-%m-%d")},
	{"name":"Klaas","birthdate":dt.strptime("2014-05-05","%Y-%m-%d")}
]

today=dt.today()

try:
	custom=dt.strptime(input("leave empty for current date or enter a date in the format YYYY-MM-DD: "),"%Y-%m-%d")
	today=dt.date(custom.year,custom.month,custom.day)
except ValueError:
	print("invalid date, using current date")

bd=False

for birthdate in data:
	if birthdate["birthdate"].month==today.month and birthdate["birthdate"].day==today.day:
		print(birthdate["name"]+" has a birthday today")
		bd=True


if not bd:
	print("no birthdays today")
 
months=("january","february","march","april","may","june","july","august","september","october","november","december")
 
#check for everymonth

for month in months:
	bd=False
	for birthdate in data:
		if birthdate["birthdate"].month==months.index(month)+1:
			print(birthdate["name"]+" has a birthday in "+month+" on the "+str(birthdate["birthdate"].day))
			bd=True
	if not bd:
		print("no birthdays in "+month)