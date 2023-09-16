#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:

def primer(numero):
    primo = True
    for i in range(2,numero,1):
        if numero%i==0:
            primo = False
            break
        else:
            primo = True
    return primo

print(primer(11))

# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:

def primlist(lista):
    lista_primos = [i for i in lista if primer(i)]  
    return lista_primos

listita = [0,1,2,3,4,5,6,7,8,9,10,11]
primlist(listita)


# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:

def repetidos(lista):
    conteo = 0
    for elemento in lista:
        cou = lista.count(elemento)
        if cou>conteo: 
            conteo = cou
            i = elemento
    return i,conteo

print(repetidos([1,1,2,3,4,5,7,3,44,2,2,2,2,2]))
print(repetidos([1,1,2,3,4,4,5]))

# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:

def conv_t(valor,unidad_origen,unidad_destino):
    conv_farenheit = lambda c: (c*(9/5)+32)
    conv_kelvin = lambda c: c + 273.15
    conv_celsius = lambda k: k - 273.15
    conv_celsiusf = lambda f: (f-32)*(5/9)
    if unidad_origen=='C' and unidad_destino=='F':
        temperatura = conv_farenheit(valor)
    if unidad_origen=='C' and unidad_destino=='K':
        temperatura = conv_kelvin(valor)
    if unidad_origen=='K' and unidad_destino=='C':
        temperatura = conv_celsius(valor)
    if unidad_origen=='K' and unidad_destino=='F':
        val_1 = conv_t(valor,'K','C')
        temperatura = conv_farenheit(val_1)
    if unidad_origen=='F' and unidad_destino=='C':
        temperatura = conv_celsiusf(valor,'F','C')
    if unidad_origen=='F' and unidad_destino=='K':
        val_1 = conv_t(valor,'F','C')
        temperatura = conv_kelvin(valor)
    return temperatura

print(conv_t(273.15,'K','F'))

# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:




# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:

def factorial(numero):
    ''' Calcula el factorial de un numero
    '''
    if type(numero)!=int or numero<0:
        return 'El valor proporcionado no permite calcular factorial'
    if numero>1:
        numero = numero*factorial(numero-1)
    return numero


