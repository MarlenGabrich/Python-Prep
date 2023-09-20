#!/usr/bin/env python
# coding: utf-8

# ## Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor

# In[1]:

class Vehículo:
    def __init__(self,color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada


# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>

# In[5]:

class Vehículo:
    def __init__(self, tipo, color, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.dirección = 0

    def acelerar(self,V):
        self.velocidad += V
        return 'Acelere: ',self.velocidad
    
    def frenar(self,V):
        self.velocidad -= V
        return 'Frene: ',self.velocidad

    def doblar(self,D):
        self.dirección = D
        return print('Redireccione:',self.dirección,'°')



# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

# In[6]:

Vehículo('auto','azul',1.20).acelerar(20)
Vehículo('camión','amarillo',10).frenar(10)
Vehículo('moto','verde',1).doblar(-90)

# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

# In[12]:

class Vehículo:
    def __init__(self, tipo, color, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.dirección = 0

    def acelerar(self,V):
        self.velocidad += V
        return self.velocidad
    
    def frenar(self,V):
        self.velocidad -= V
        return self.velocidad

    def doblar(self,D):
        self.dirección = D
        return self.dirección
    
    def caracteristicas(self):
        return print(self.tipo,'color',self.color,'de',self.cilindrada,'litros')

    def estado(self):
        return print('Ha modificado su velocidad en', self.velocidad,'y su dirección en',self.dirección,'°')



# In[13]:


a = Vehículo('auto','rojo',2)
a.caracteristicas()

a.estado()
a.frenar(20)
a.doblar(90)
a.estado()
a.doblar(-90)
a.estado()

Vehículo('auto','rojo',2).caracteristicas()
Vehículo('auto','rojo',2).estado()

# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 7<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>

# In[33]:


from herramientas_mio import Herramientas

class Funciones_07(Herramientas):

    def __init__(self): pass



# 6) Probar las funciones incorporadas en la clase del punto 5

# In[28]:

Funciones_07.primlist([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
Funciones_07.factorial(3)
Funciones_07.conv_t(0,'K','C')
Funciones_07.primer(11)
Funciones_07.repetidos([1,12,3,193,1883,0-3,92,3,2,2,2,3])


# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

# In[55]:

from herramientas_mio import Herramientas

class Funciones_07(Herramientas):
    
    def __init__(self,lista):
        self.lista = lista
    
    def ck(self):
        lista_conversor = [Herramientas.conv_t(i,'C','K') for i in self.lista]
        return lista_conversor
    
    def usar(self):
            
        return ('Aplicando funcion primlist: ', Herramientas.primlist(self.lista),
                'Aplicando funcion repetidos: ', Herramientas.repetidos(self.lista),
                'Aplicando funcion conversion: ', Funciones_07(self.lista).ck(),
                'Aplicando funcion factorial: ', Herramientas.factorial(self.lista))

        
Funciones_07([1,2,3,4]).usar()    


# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones

# In[1]:

import sys

sys.path.append('/home/marlen/Desktop/Python-Prep/M07_funciones/')


