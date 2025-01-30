# Greet a user based on the time of day
import datetime

name = input("Enter your name: ")
hour = datetime.datetime.now().hour

if hour < 12:
    greeting = "Good morning"
elif 12 <= hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

print(f"{greeting}, {name}!")
