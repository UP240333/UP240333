#1._Concatena la cadena 'Thirty', 'Days', 'Of', 'Python' en una sola cadena: 'Thirty Days Of Python'.
print(" ".join(["Thirty", "Days","Of", "Python"]))

#2._Concatena la cadena 'Coding', 'For', 'All' en una sola cadena: 'Coding For All'.
print(" ".join(["Coding","For", "All"]))
#3._Declara una variable llamada company y asígnale el valor inicial "Coding For All".
company="Coding For All"
#4._Imprime la variable company usando print().
print(company)          
#5._Imprime la longitud de la cadena company usando el método len() y print()
print(len(company))   
#6._Cambia todos los caracteres a mayúsculas utilizando el método upper(). 
upper_company=company.upper()  
print("Mayúsculas",upper_company)
#7._Cambia todos los caracteres a minúsculas utilizando el método lower().
lower_company=company.lower()
print("Minúsculas",lower_company)
#8._Utiliza los métodos capitalize(), title(), swapcase() para dar formato al valor de la cadena "Coding For All".
print(company.capitalize())   #Capitalize()
print(company.title())        #Title()
print(company.swapcase())     #swapcase()
#9._Recorta (extrae) la primera palabra de la cadena "Coding For All".
print(company[7:])
#10._Verifica si la cadena "Coding For All" contiene la palabra "Coding" utilizando el método index(), find() u otros métodos.
posición=company.index("Coding")   #Buscar coding con index
print("La palabara Coding se encuentra en la posición" ,posición)
posiciónf=company.find("Coding")   #Buscar coding con find
print("La palabara Coding se encuentra en la posición" ,posiciónf)
#11._Reemplazar la palabra "Coding" en la cadena "Coding For All" por "Python".
company_new=company.replace("Coding","Python" )
print(company_new)
#12._ Cambiar "Python for Everyone" a "Python for All" usando el método replace() u otros métodos.
new_text="Python for everyone"
text_new=new_text.replace("Python for everyone","Python for all")
print(text_new)
#13._- Dividir la cadena "Coding For All" usando el espacio como separador (split()).
espacio=company.split(",")
print(espacio)
#14._- Dividir la cadena "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" usando la coma como separador.
cadena= "Facebook Google Microsoft Apple IBM Oracle Amazon" 
coma=cadena.split(" ") 
print(coma)
#15._- Determinar qué carácter está en el índice 0 de la cadena "Coding For All".
ubiby="Coding for all"[0]
print(ubiby)
#16._- Obtener el último índice de la cadena "Coding For All".
lastubi="Coding for all"[13]
print(lastubi)
#17._- Determinar qué carácter está en el índice 10 de la cadena "Coding For All".
medio="Coding for all"[9]
print(medio)
#18._- Crear un acrónimo o una abreviación para "Python For Everyone".
def create_acronym(phrase):
    return " ".join(word[0].upper()for word in phrase.split())
acronimo=create_acronym("Python For Everyone")
print(acronimo)
#19._- Crear un acrónimo o una abreviación para "Coding For All".
acronimo2=create_acronym("Coding For All")
print(acronimo2)
#20._- Usar index() para determinar la posición de la primera ocurrencia de "C" en "Coding For All".
index_c="Coding for all".index("C")
print(index_c)
#21._Determinar la posición de la primera ocurrencia de 'F' en "Coding For All"
index_f="Coding for all".index("f")
print(index_f)
#22._Determinar la posición de la última ocurrencia de 'l' en "Coding For All People"
last_L="Coding for all people"
find_L=last_L.rfind("l")
print(find_L)
#23._ Encontrar la primera ocurrencia de 'because' en la oración dada
busca_bec="You cannot end a sentence with because because because is a conjunction".index("because")
print(busca_bec)
#24._Encontrar la última ocurrencia de 'because' en la oración dada
las_bec="You cannot end a sentence with because because because is a conjunction".rindex("because")
print(las_bec)
#25._Extraer la frase 'because because because'
because="You cannot end a sentence with because because because is a conjunction"
extraer=because[31:54]
print(extraer)
#26._Verificar si "Coding For All" comienza con 'Coding'
print(company.startswith("Coding"))
#27._Verificar si "Coding For All" termina con 'coding'
print(company.endswith("Coding"))
#28._- Eliminar los espacios en blanco al inicio y al final de la cadena dada:
spacewhite=" '  Coding for all    ' ".strip()
print(spacewhite)
#29._ ¿Cuál de las siguientes variables devuelve True con isidentifier()?
daysp="30DaysOfPython".isidentifier()
tpy="thirty_days_of_python".isidentifier()
print(daysp)
print(tpy)
#30._Unir la lista con hash y espacio
lista=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
gato=' # '.join(lista)
print(gato)
#31._Separar oraciones con secuencia de linea escape
print("I am enjoying this challenge.\nI just wonder what is next.")
#32._Separar con tabulaciones
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")
#33._Formatear string con radio y área
radius=10
area=3.14*radius**2
mensaje="The area of a circle with radius {} is {} meters square".format(radius,area)
#34._Formatear operaciones
print(mensaje)
a, b=8, 6
print("{}+{}={}".format(a, b, a+b))
print("{}-{}={}".format(a, b, a-b))
print("{}*{}={}".format(a, b, a*b))
print("{}/{}={}".format(a, b, a/b))
print("{}%{}={}".format(a, b, a%b))
print("{}//{}={}".format(a, b, a//b))
print("{}**{}={}".format(a, b, a**b))










