#Level 2
#1._Lo siguiente es una lista de 10 estudiantes
ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Ordenar la lista
ages.sort()
print("Edades ordenadas: ",ages)
#Edad mínima y edad máxima
min_age= min(ages)
max_age= max(ages)
print("Edad mínima: ", min_age)
print("Edad máxima: ", max_age)
#Agregar otra vez min y max a la lista
ages.extend([min_age, max_age])
print("Lista con min y max agregados", ages)
#Mediana
ages.sort()
n=len(ages)
if n % 2 == 0:
    median = (ages[n//2 - 1]+ ages [n//2])/2
else:
    median=ages[n//2]
    print("Mediana: ", median)

#Promedio media
average= sum(ages) / len(ages)
print("Promedio: ", average)
#Rango
age_rango=max(ages)-min(ages)
print("Rango de edades: ", age_rango)
#Comparar valores absolutos
print("abs(min - average):", abs(min_age-average))
print("abs(max - average):", abs(max_age - average))
#Lista de países
countries=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
#Países del medio
n= len(countries)
if n % 2 == 0:
    middle_countries = countries[n//2 - 1 : n//2 + 1]
else:
    middle_countries = [countries[n//2]]
print("Países del medio: ", middle_countries)
#Dividir listas en dos mitades 
mid= (n + 1) // 2
primera_mitad=countries[:mid]
segunda_mitad=countries[mid:]
print("Primera mitad: ", primera_mitad)
print("Segunda mitad: ", segunda_mitad)
# Desempaquetar los tres primeros y el resto como países escandinavos
primero, segundo, tercero, *scandic_countries=countries
print("Primeros tres países: ", primero, segundo, tercero)
print("Países escadinavos: ", scandic_countries)

