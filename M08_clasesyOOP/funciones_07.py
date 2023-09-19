from herramientas_mio import Herramientas

class Funciones_07(Herramientas):

    def __init__(self): pass

    def fun(primo=0,lista_primos=[0],
                 lista_repetidos=[0],
                 convertir_temperatura=[0,'',''],
                 factor = 0):
        if primo!=0: 
            return Herramientas.primer(primo)
        if lista_primos!=[0]: 
            return Herramientas.primlist(lista_primos)
        if lista_repetidos!=[0]: 
            return Herramientas.repetidos(lista_repetidos)
        if convertir_temperatura!=[0,'','']:
            a = convertir_temperatura[0]
            b = convertir_temperatura[1]
            c = convertir_temperatura[2]
            return Herramientas.conv_t(a,b,c)
        if factor!=0:
            return Herramientas.factorial(factor)