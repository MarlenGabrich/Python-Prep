#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:

list = []
i=-15
while i<0:
    list.append(i)
    i+=1
print(list)


# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:

i=0
while i<len(list):
    if list[i]%2==0:
        print(list[i])
    i+=1

# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:

for i in list:
    if i%2==0:
        print(list[i])


# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

# In[7]:

iti = iter(list)
i=0
while i<3:
    print(next(iti))
    i+=1


# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:

for i in enumerate(list):
    print(i)


# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:

lista = [1,2,5,7,8,10,13,14,15,17,20]
ite = iter(lista)
a = next(ite)
i=0

while i<20:
    i+=1
    if i!=a:
        lista.append(i)
    else:
        a = next(ite)

    
lista.sort()
print (lista)


# In[11]:

# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:

# sucesión de Fibonacci 
lista = [0,1]
i=2

while len(lista)<30:     
        n = lista[i-1]+lista[i-2]
        lista.append(n)
        i+=1

print(lista)

# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:

print(sum(lista))


# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:

lista.reverse()
eit=iter(lista)
b = next(eit)
count=0
while count<5:
    c = next(eit)
    print(b/c)
    b=c
    count+=1


# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:

cadena = 'Hola mundo. Esto es una practica del lenguaje de programacion Python'
for i in enumerate(cadena):
    if i[1]=='n':
        print(i[0])


# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:

dic = {'mes':['oct','nov','dic','ene','mar'],'año':['1990','2000','2010','2015','2020']}
print(type(dic))
dor = iter(dic)
i = 0

while i<len(dic):
    print(next(dor))
    i+=1


# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:

lista = list(cadena)
itera = iter(lista)
i=0


# In[45]:

while i<len(lista):
    print(next(itera))
    i+=1


# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:

li1 = ['dia:','mes:','año:']
li2 = [22,'octubre',1996]

liz = zip(li1,li2)
liz1 = list(liz)
print(liz1)



# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# In[49]:

lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
iterador = iter(lis)
a = next(iterador)
n = 1

lisnueva = []
while n < len(lis):
    n+=1
    if a%7==0:
        lisnueva.append(a)
        a = next(iterador)
    else:
        a = next(iterador)
    
print(lisnueva)


# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# In[56]:

lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# In[51]:

lis2 = [i for i in lis if i%7==0]

# In[57]:

print(lis2)

# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:

for indice,elemento in enumerate(lis):
    if type(elemento)!=list:
        lis[indice]=[elemento]
print (lis)

iterable = [1,2,3,4,5,6]
lista = [2*elemento for elemento in iterable if elemento%2==0]
print(lista)

frase = 'El perro de San Roque no tiene rabo'
erres = [i for i in frase.lower() if i=='r']
print(len(erres))