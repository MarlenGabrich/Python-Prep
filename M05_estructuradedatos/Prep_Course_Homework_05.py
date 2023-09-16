#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:

cities = ['córdoba', 'santa fe', 'camboriu', 'esperanza', 'salsipuedes', 'cosquín']
print(cities)


# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:

cities[1]


# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:

cities[1:4]



# 4) Visualizar el tipo de dato de la lista

# In[12]:

print(type(cities),type(cities[2]))



# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:

cities[2:]



# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:

cities[:4]

    


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:

cities.append('córdoba')
cities.append('rosario')
print(cities)


# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:

cities.insert(3,'venado tuerto')


# In[21]:

print(cities)

# 9) Concatenar otra lista a la ya creada

# In[22]:

ages = [2020,2023,2019,1995]
cities.extend(ages)
cities


# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:

cities.index('salsipuedes')



# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:


cities.index('hola')


# 12) Eliminar un elemento de la lista

# In[25]:

cities.remove(1995)
cities



# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:


cities.remove('2021')


# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:

ultimo = cities.pop()
print(ultimo)

segundo = cities.pop(1)
segundo


# 15) Mostrar la lista multiplicada por 4

# In[29]:

print(ages*3)

ages.sort()
print(ages)

cities.sort()
print(cities)

let = ['hola','chau','que tal','buendi']
let.sort()
print(let)

let.sort(reverse=True)
print(let)

# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:

mi_tupla= (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(mi_tupla)


# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:

print(mi_tupla[9:15])


# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:


20 in mi_tupla
30 in mi_tupla

# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:

if not 'Paris' in mi_tupla:
    print('no está')
    mi_tupla[20]='Paris'



# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:

x = 11
y = 22
z = 'henry'
tupla2 = x,y,z
print(type(tupla2))



# 21) Convertir la tupla en una lista

# In[52]:

mi_tupla.count(12)


# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:

lista_co = list(mi_tupla)
print(lista_co,type(lista_co))


# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:

uno,dos,tres = mi_tupla[:3]
print(uno,dos,tres)

# 24) Imprimir las claves del diccionario

# In[59]:

_,_,_,cuarto,quinto = mi_tupla[:5]
print(cuarto,quinto)


# 25) Imprimir las ciudades a través de su clave

# In[61]:

p_dic={}
p_dic['ciudad']=cities
p_dic['país']='argentina'
p_dic


