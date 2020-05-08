#!/usr/bin/env python3

def to_seconds(hours, minutes, seconds):
    return (hours*3600 + minutes*60 + seconds)

print("Welcome in the time converter")

count = "y"

while (count == 'y'):

    hours = int(input("Enter the hours : "))
    minutes = int(input("Enter the minutes : "))
    seconds = int(input("Enter the seconds : "))

    print("The seconds are {}".format(to_seconds(hours, minutes, seconds)))

    count = input("Enter 'y' for continue")

print("Thank you")
