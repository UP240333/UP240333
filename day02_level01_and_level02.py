#Day 2:30 Days of python programming
first_name= input("Escribe tu Primer Nombre: ")
last_name= input("Escribe Tu Apellido: ")
full_name= input("Escribe tu nombre completo: ")
country= input("Escribe el nombre de un país: ")
city= input("Escribe el nombre de una ciudad: ")
age= input("Escribe tu edad: ")
year= input("Escribe el año en que naciste: ")
is_married= True
is_true= False
is_light= True
a,b,c= (7,8,9)
print()

print(first_name)
print(last_name)
print(full_name)
print(country)
print(city)
print(age)
print(year)
print(is_married)
print(is_true)
print(is_light)
print(a,b,c)
#2
print()

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))
print(type(a,b,c))
#3
print()

print(len(first_name)>len(last_name))
print(len(first_name)==len(last_name))

#4 0peraciones 
import math

num_one=5
num_two=4
total= num_one + num_two
diff= num_two - num_one
product= num_two*num_one
division= num_one/num_two
remainder=num_two%num_one
exp=num_one^num_two
floor_division=num_one//num_two
#The radius of a circle is 30 meters
radius=30
area_of_circle=math.pi*(radius**2)
print("El área del circulo es ", area_of_circle)
circum_of_circle=2*math.pi*(radius**2)
print("La circunferencia del circulo es", circum_of_circle)
#Toma el radio como entrada del usuario y calcula el área
radius=float(input("Ingresa el radio del círculo: "))
area_of_circle=math.pi*(radius**2)
print("El área del circulo es", area_of_circle)
