print ("bienvenido")
print ("en este codigo veremos la frecuencia de las letras en una palabra")

palabra = str(input("ingrese una palabra"))
try:
    assert type(palabra) == str
except:
    print ("eso no es una palabra")
    
diccionario_letras = {}

for letra in palabra:
    if letra in diccionario_letras:
        diccionario_letras[letra] += 1
    else:
        diccionario_letras[letra] = 1
        
print ("frecuencia de las letras:")

for i in diccionario_letras.keys():
    print (i, "->", diccionario_letras[i])