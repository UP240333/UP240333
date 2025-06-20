#1._Declara una lista vacía 
vacio=[]
#2._- Declara una lista con más de 5 elementos
fiveelements=["diego", "angel", "amaury", "balón", "celular"]
#3._Obtén la longitud de tu lista
print(len(fiveelements))
#4. Obtener el primer, el elemento del medio y el último de la lista:
primeroE=fiveelements[0]
medio=len(fiveelements)//2
elementoM=fiveelements[medio]
ultimo=fiveelements[-1]
print(primeroE)
print(elementoM)
print(ultimo)
#5._ Declara una lista llamada mixed_data_types, pon tu (nombre, edad, estatura, estado civil, dirección)
mixed_data_types=["Diego", "19", "1.67", "Aguascalientes", "Arandas"]
#6._ Declara una variable de lista llamada it_companies y asígnale los valores iniciales: Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
#7._ Imprime la lista usando print()
print(mixed_data_types)
print(it_companies)
#8._- Imprime el número de empresas en la lista
num_empresas=len(it_companies)
print(num_empresas)
#9._ Imprime la primera, la del medio y la última empresa
list1=it_companies[0]
enmedio=len(it_companies)//2
enmediofinal=it_companies[enmedio]
listul=it_companies[-1]
print("Primero: " ,list1)
print("Medio: ", enmediofinal)
print("Última: ", listul)
#10._Modificar una de las empresas:
it_companies[1]="Netflix"
print(it_companies)
#11._Agregar una empresa de TI
it_companies.append("Tesla")
print(it_companies)
#12._Insertar una empresa en el centro:
it_companies.insert(len(it_companies)//2, "OpenAI")
print(it_companies)
#13._Convertir una empresa a mayúsculas (excepto IBM)
it_companies[3]=it_companies[3].upper()
print(it_companies)
#14._Unir empresas con el string '#;  ':
unir='#;  '.join(it_companies)
print(unir)
#15._Verificar si una empresa existe:
print("Tesla" in it_companies)
#16._Ordenar la lista
it_companies.sort()
print(it_companies)
#17._Invertir en orden descendente
it_companies.reverse()
print(it_companies)
#18._Extraer 3 compañias de la lista
print(it_companies[1:4])
#19._Extraer las últimas 3 compañías
print(it_companies[-3:])
#20._Extrae de la lista la o las empresas de TI intermedias
n=len(it_companies)
if n % 2 == 0:
    print(it_companies[n//2-1 : n//2+1])
else:
    print(it_companies[n//2])
#21._ Eliminar la primera empresa
eliminado=it_companies.pop(0)
print(eliminado)
print(it_companies)
#22._Eliminar la(s) empresa(s) del medio:
n=len(it_companies)
if n % 2 == 0:
    del it_companies[n//2 - 1 : n//2 + 1]
else:
    del it_companies[n//2]
print(it_companies)
#23._Eliminar la última empresa
deleate=it_companies.pop(-1)
print(deleate)
print(it_companies)
#24._Eliminar todas las compañias de la lista
it_companies.clear()
print(it_companies)
#25._Destruir la lista
del it_companies[:]
print(it_companies)
#26._Une las siguientes listas
front_end= ["HTML", "CSS", "JS", "React", "Redux"]
back_end= ["Node", "Express", "MongoDB"]
full_stack=front_end+back_end
#27.Después de unir las listas en la pregunta 26, copie la lista unida y asígnela a una variable full_stack, luego inserte Python y SQL después de Redux.
indice=full_stack.index("Redux")+1
full_stack.insert(indice, "Python")
full_stack.insert(indice+1, "SQL")
print(full_stack)















