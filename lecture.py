# primer ejemplo if estructurado
edad:int=int(input("escribe tu edad: "))
if edad>=18:
    print ("eres mayor")
else:
    print("eres menor de edad")
#segundo ejemlpo if almacenado en variable
edad_dos:int=int(input("escribe tu edad: "))
respuesta:str="eres mayor" if edad_dos>18 else "eres menor"
print (respuesta)
# crear un programa que me imprima 5 vocales
vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales:
    print(vocal)
vocales:str="aeiou"
for n in range(0,5): 
    print(vocales)
    #crear un programa que me muestre los 8 primero numeros pares 
    contador=0
    for n in range(1,17): 
        if n%2==0:
            contador+=1
            print(f"(n) es par numero (contador)")

#crear un progreama que pida al usuario escribir una oración y 
#mostrar por terminal la cantidad de vocales "a" que tiene esa oracion
# ojo: solo las "a" minúsculas
oracion = input("Escribe una oración: ")
contador_vocales = 0
vocales = 'a'
for letra in oracion:
    if letra.islower() and letra in vocales:
        contador_vocales += 1
print("La oración tiene", contador_vocales, "vocales en minúsculas.")
oracion:str=input("escribe una oracion: ") 
contador:int=0 
for n in range(0,len(oracion)): 
    if oracion[n]=="a": 
        contador-contador+1 
        #contador+=1 
print(f"la cantidad de letras a que tengo es (contador)")
for n in "aeiou":
     print(n)
for ind_vocal,let_vocal in enumerate("aeiou");
 print(f"el indice es (1) y la letra es (l)") 
print(f"la cantidad de letras a que tengo es (contador)")
#crear un programa que eme cuente la cantidad de comas y me muestre
#sus indices.
#ojo:tiene que pedir el uduario
# Solicitar al usuario que escriba una oración
oracion = input("Escribe una oración: ")

# Inicializar una lista para almacenar los índices de las comas
indices_comas = []

# Inicializar una variable para controlar si estamos dentro de comillas
dentro_comillas = False

# Contar la cantidad de comas y almacenar sus índices
for indice, caracter in enumerate(oracion):
    if caracter == '"':
        dentro_comillas = not dentro_comillas
    if caracter == ',' and not dentro_comillas:
        indices_comas.append(indice)

# Mostrar la cantidad de comas y sus índices
cantidad_comas = len(indices_comas)
print("La oración tiene", cantidad_comas, "coma(s) y están en los índices:", indices_comas)