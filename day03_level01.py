Entero=19
floatd=1.67
número_complejo=7+6j
#4._Script para base,altura de un triangulo y calcular su area
base=float(input("Ingrese una base: "))
height=float(input("Ingrese una altura: "))
area_triangulo=base*height/2
print("El área del triangulo es: ",area_triangulo)
#5._Script para perimetro de un triangulo 


a=float(input("Ingrese el lado a: "))
b=float(input("Ingrese el lado b: "))
c=float(input("Ingrese el lado c: "))
perimetro_triangulo=(a+b+c)
print("El perimetro del triangulo es: ",perimetro_triangulo)
#6._Script para sacar la área y périmetro de un rectangulo
largo=float(input("Ingrese el largo del rectángulo: "))
ancho=float(input("Ingrese el ancho del rectángulo: "))
area_rectángulo=largo*ancho/2
print("El area del rectángulo es: ", area_rectángulo)
perimetro_rectángulo=largo+largo+ancho+ancho
print("El perimetro del rectángulo: ",perimetro_rectángulo)
#7._Script para obtener el area del circulo
import math
radio=float(input("Ingrese el radio del circulo: "))
area_circulo=math.pi*(radio**2)
print("EL área del circulo es: ",area_circulo)
#8._Ecuacion de la recta 2x-2
pendiente1 = 2
interseccion_x = 2 / 2  # Cuando y = 0, x = 1
interseccion_y = -2     # Cuando x = 0, y = -2
print("Pendiente:", pendiente1)
print("Intersección con el eje x:", interseccion_x)
print("Intersección con el eje y:", interseccion_y)
#9._Pendiente y distancia euclidiana entre dos puntos
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente2 = (y2 - y1) / (x2 - x1)
distancia = ((x2 - x1) * 2 + (y2 - y1) * 2) ** 0.5
print("Pendiente entre los puntos:", pendiente2)
print("Distancia euclidiana:", distancia)
#10._Comparar pendientes
print("Las pendientes son iguales?",pendiente1==pendiente2)
#11._- Calcular el valor de y para diferentes valores de x y determinar cuándo y es 0
valores_x=[-3,-2,0,1]
for x in valores_x:
    y=x**2+6*x+9
    print("Cuando x={x}, y={y}")
#12._Falsa comparación 
texto_1=len("python")
texto_2=len("dragon")
print("La longitud de python es: ",texto_1)
print("La longitud de dragon es: ",texto_2)
print(len("python") < len("dragon"))
#13._Operador and para verificar si "on" esta las dos palabras
print("on" in "python" and "on" in "dragon")
#14._Verificar si la palabra 'jargon' está en la oración dada.
print("jargon" in "I hope this course is not full of jargon")
#15._Afirmación falsa:No hay 'on' en "dragon" y "Python".
print("on" in "python" and "on" in "dragon")
#16._Encuentra la longitud del texto "python", conviértelo a un número flotante y luego a una cadena.
longitud_py=len("python")
valor_flotante= float(longitud_py) #Así se convierte a flotante
Valor_string= str(longitud_py) #Así se convierte a cadena 
print(valor_flotante)
print(Valor_string)
#17._ Verificar si un número es par
numero = int(input("Ingresa un número para verificar si es par: "))
print(numero % 2 == 0)

#18._ Verificar división entera
print(7 // 3 == int(2.7))

#19._ Verificar tipos
print(type('10') == type(10))

#20._ Verificar conversión de cadena
try:
    print(int('9.8') == 10)
except ValueError:
    print("No se puede convertir '9.8' a entero directamente.")

#21._ Calcular salario
horas = float(input("Ingresa las horas trabajadas: "))
tarifa = float(input("Ingresa la tarifa por hora: "))
salario = horas * tarifa
print("Tu ingreso semanal es", int(salario))

#22._ Calcular segundos vividos
años = int(input("Ingresa el número de años que has vivido: "))
segundos = años * 365 * 24 * 60 * 60
print(f"Has vivido {segundos} segundos.")

#23._ Mostrar tabla
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")








