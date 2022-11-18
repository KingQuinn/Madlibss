# string concatenation [aka join strings together]
#creating a string that wants to say 'subscribe to___'
#youtuber = 'king deejah' #some youtuber

# a fews of doing that
#print('subscribe to', youtuber)

name = input("input your code name:")
city = input("input city of choice:")
event = input("input event of choice e.g wedding:")
famous_person = input("input famous person:")
age = input("input any age:")
nationality = input("input any nationality:")
weapon = input("input weapon:")
car = input("input vehicle model:")
brand = input("input designer brand:")

madlib = f"Welcome agent {name}\n There has been a recent increase in crime rate in the old city of {city}, our sources believe the {event} of {famous_person} has something to do with it.\n considering this is a code black, your mission is to eliminate {famous_person} with immediate effect\n Your aliase is a {age} years old {nationality} girl called Quinn, you have been equipped with a/an {weapon} a/an {car} and a special ops {brand} suit.\n mission is to be completed in less than 48hrs, starting NOW.\n Thank you and goodluck agent {name}"

print(madlib)