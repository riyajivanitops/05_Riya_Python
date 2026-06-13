from datetime import datetime

f = open('information.txt', 'w')

stu = int(input("how many student: "))

for i in range(stu):
    timestamp = datetime.now()
    id = int(input("enter the id: "))
    name = input("enter the name: ")
    city = input("enter the city: ")
    f.write(f"\n Time: {timestamp} \n ID: {id} \n Name: {name} \n City: {city}  ")

