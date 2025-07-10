#Escrito por: Leonardo Otero
#02/07/2025
#version 2

print ("Bienvenido")
print ("En este codigo veremos la frecuencia de los caracteres en una palabra")

palabra = str(input("Ingrese una palabra"))
try:
    assert type(palabra) == str
except:
    print ("Eso no es una palabra")
    
diccionario_caracter = {}

for caracter in palabra:
    if caracter in diccionario_caracter:
        diccionario_caracter[caracter] += 1
    else:
        diccionario_caracter[caracter] = 1
        
print ("Frecuencia de las letras:")

for caracter in diccionario_caracter.keys():
    print (caracter, "->", diccionario_caracter[caracter], sep = " ")
    
print ("Quiere ver el tipo de cada caracter?")
respuesta = str(input("si o no?"))

if respuesta == "si":
    for caracter in palabra:
        es_letra = caracter.isalpha()
        es_numero = caracter.isdigit()
        
        if es_letra:
            print (caracter, "->", "letra", sep = " ")
        elif es_numero:
            print (caracter, "->", "numero", sep = " ")
        else:
            print (caracter, "->", "caracter especial", sep = " ")
elif respuesta == "no":
    print ("Esta bien")
else:
    print ("?")