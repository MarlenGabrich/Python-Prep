#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

a = 0
if a<0: print("a es menor q 0")
if a>0: print("a es mayor a 0")
else: print("a es 0")


# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

b = 'hola'
c = 1234

if type(b)==type(c): print('mismo tipo de datos')
else: print('variables de diferente tipo')



# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

for i in range(1,21):
    if i%2==0:print(i,'es un número par')
    else: print(i, 'es un número impar')


# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

for i in range(0,6): print('i elevado al cubo es:', i**3)


# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:

d = 4
for i in range(d):
    print(i)
    pass



# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

c=1
d=4
if type(d)==int and d>0:
    factorial = d
    while d>2:
        d-=1
        factorial*=d
    print('d!:',factorial)



# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:

while d>0:
    for i in range(d):print (i)
    break



# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:

for i in range (10):
    while i%2==0:
        print('sigo')
        break



# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

n=0
ciclos=0
li = []
primo = True
while (n<30):
    for i in range(2,n):
        ciclos +=1
        if (n%i==0 and n!=i):
            primo = False
            break
        if primo==True and n not in li:
            li.append(n)
        else:
            primo = True   
    n+=1
print(li)
print(ciclos)


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:

n2=0
ciclos2=0
li2 = []
primo2 = True
while (n2<31):
    for j in range(2,n2):
        ciclos2 +=1
        if (n2%j==0 and n2!=j):
            primo2 = False
            break
        if primo2 and n2 not in li2:
            li2.append(n2)
            break
        else:
            primo2 = True
    n2+=1
print(li2)
print(ciclos2)



# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:

print (round((ciclos2/ciclos)*100,2),'% de optimización')


# In[57]:




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

n=99

while n<300:
    n+=1
    if (n%12!=0):continue
    print(n)
    



# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:

print('Desea encontrar el primer número primo? S(1)/N(0)')
a=input()
n=1
primo = True

while (a=='1'):
    for i in range(2,n):
        if (n%i==0 and n!=i):
            primo = False
            break
    if (primo):
        print('Número primo: ',n)
        print('Desea continuar con el siguiente número primo?')
        if (input()!='1'):
            print('Proceso finalizado')
            break
    else:
        primo = True
    n+=1


# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:


bu = False

while not bu:
    for i in range (100,301):
        if i%6!=0: continue
        print(i)
        bu = True
        break
