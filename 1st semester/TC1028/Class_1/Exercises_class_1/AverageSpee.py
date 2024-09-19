#Exercise 2

#Write an algorithm that shows the average speed of a car given the distance traveled in kilometers and the time that it took to travel that distance in hours.


print("This program takes a given a traveled distance and time of travel")
distance = float (input('Input the distance the car travelled in kilometers: '))
time = float (input('Input the time that the car took to travel the given distance in hours: '))
speed = distance/time
print (f"Average speed {speed}km/h")

