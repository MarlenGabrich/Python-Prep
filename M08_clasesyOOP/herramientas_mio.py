class Herramientas:
    conv_farenheit = lambda c: (c*(9/5)+32)
    conv_kelvin = lambda c: c + 273.15
    conv_celsius = lambda k: k - 273.15
    conv_celsiusf = lambda f: (f-32)*(5/9)
    
    def __init__(self):
        pass
    
    def primer(numero):
        if numero == (str or int): pass
        else: return ('Ingrese un numero')

        try:
            primo = True
            for i in range(2,numero,1):
                if numero%i==0:
                    primo = False
                    break
                else:
                    primo = True
            return primo
        except ZeroDivisionError: 
            print('Debe ingresar un numero mayor a cero')


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


    def conv_t(self,valor,unidad_origen,unidad_destino):
        
        assert valor == int or float, f'{valor} no es convertible entre unidades de temperatura'
        assert (unidad_origen.upper() == 
                'C' or 'K' or 'F',
                f'{unidad_origen} no corresponde a una unidad valida'
                )
        
        if (unidad_origen.upper()=='C' 
            and unidad_destino.upper()=='F'
            ):

            temperatura = self.conv_farenheit(
                valor
                )
        
            return temperatura
        
        if (unidad_origen.upper()=='C'
            and unidad_destino.upper()=='K'
            ):

            temperatura = self.conv_kelvin(valor)
        
            return temperatura
        
        if (unidad_origen.upper()=='K' 
            and unidad_destino.upper()=='C'
            ):
            
            temperatura = self.conv_celsius(valor)
        
            return temperatura
        
        if (unidad_origen.upper()=='K' 
            and unidad_destino.upper()=='F'
            ):
            
            val_1 = self.conv_t(valor,'K','C')
            temperatura = self.conv_farenheit(
                val_1)
        
            return temperatura
        
        if (unidad_origen.upper()=='F' 
            and unidad_destino=='C'
            ):
            
            temperatura = self.conv_celsiusf(
                valor,'F','C'
                )
        
            return temperatura
        
        if (unidad_origen.upper()=='F' 
            and unidad_destino.upper()=='K'
            ):
            
            val_1 = self.conv_t(valor,'F','C')
            temperatura = self.conv_kelvin(valor)
    
            return temperatura
    

    def factorial(numero):
        ''' Calcula el factorial de un numero
        '''
        if numero == 0 : pass
        if type(numero)!=int or numero<0:
            return 'El valor proporcionado no permite calcular factorial'
        if numero>1:
            numero = numero*Herramientas.factorial(numero-1)
        
        return (numero)