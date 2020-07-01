
def es_impar(numero):
    resto = numero % 2
    if resto == 0:  ## El numero es par
        return False
    else:
        return True


lista = (1,3,5,4,6,8,2,10)
for numero in lista:
    print('Procesamos el numero ', numero)
    respuesta = es_impar(numero)
    if respuesta:  # respuesta == True
        print('El número es impar')
    else:
        print('El número es par')

# Damos un texto y lo ponga en mayusculas <- Test
def mayuscular(texto):
    return texto.upper()

#Damos un texto y cuenta las palabras que contiene <- test
def numero_palabras(texto):
    return len(texto.split())
