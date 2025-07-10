#Escrito por: Leonardo Otero
#02/07/2025
#version 2

print ("Bienvenido")
print ("En este codigo veremos la frecuencia de las letras en una palabra")

palabra = str(input("Ingrese una palabra"))
try:
    assert type(palabra) == str
except:
    print ("Eso no es una palabra")
    
diccionario_letras = {}

for letra in palabra:
    if letra in diccionario_letras:
        diccionario_letras[letra] += 1
    else:
        diccionario_letras[letra] = 1
        
print ("Frecuencia de las letras:")

for i in diccionario_letras.keys():
    print (i, "->", diccionario_letras[i])