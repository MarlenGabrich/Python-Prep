#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

a = 27


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

print(type(8.5))



# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:


print(type(a))


# 4) Crear una variable que contenga tu nombre

# In[2]:


name = 'Marlen'

# 5) Crear una variable que contenga un número complejo

# In[3]:


nc = 4+5j


# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:

print(type(nc))



# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416
vp = round(pi,4)
print(vp,type(vp))

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

v1 = 'True'
v2 = True



# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

print(type(v1),type(v2))



# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:


s1 = 4+5
s2 = sum([4,5])
print(s1,s2)


# 11) Realizar una operación de suma de números complejos

# In[2]:

s3 = (1+2j)+(2+3j)
s4 = sum([1+2j,2+3j])
print(s3,s4)



# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

s5 = 1.2+(1+2j)
s6 = sum([1.2+2j])
print(s5,s6)

# 13) Realizar una operación de multiplicación

# In[5]:

print(2*2)



# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

print(2**8)


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

co = 27/4
co2 = 27%4
co3 = 27//4



# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

print('parte entera:', co3)



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:

print('resto:',co2)



# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

re = (4*co3)+co2
print(re)


# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

af = '2'+'as'+'2'
print(af)


# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

print('2'==2)

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

da1 = '2'
da2 = 2
da1 = int(da1)
print(da1==da2)



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:


a = float(3.8)


# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:


va = 3
va -=1
print(va)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

print(1<<2)



# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

print(2+2,'2'+'2')



# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

print(2*'hola ')

