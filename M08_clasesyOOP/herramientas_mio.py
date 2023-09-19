class Herramientas:

    def __init__(self):
        pass
    
    def primer(numero):
        if numero == 0: pass
        else:
            primo = True
            for i in range(2,numero,1):
                if numero%i==0:
                    primo = False
                    break
                else:
                    primo = True
            return primo

    def primlist(lista):
        lista_primos = [i for i in lista if Herramientas.primer(i)]  
        return lista_primos

    def repetidos(lista):
        if lista == [0]: pass
        else:
            conteo = 0
            for elemento in lista:
                cou = lista.count(elemento)
                if cou>conteo: 
                    conteo = cou
                    i = elemento
            return i,conteo

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

    def factorial(numero):
        ''' Calcula el factorial de un numero
        '''
        if numero == 0 : pass
        if type(numero)!=int or numero<0:
            return 'El valor proporcionado no permite calcular factorial'
        if numero>1:
            numero = numero*Herramientas.factorial(numero-1)
        return numero