#[] = #arreglos ( permiten almacenar múltiples valores de un mismo tipo en una variable)
#len imprime el tamaño de un caracter, lista, etc 



playlistcurso = [
    "beat-it.mp3" , "loba,mp3" , "15b.mp3" , "diva virtua.mp3 " , "pokemon jhotho.mp3" , "los diablotes.mp3" #empieza a contar desde el 0
]
print(playlistcurso[3]) #los corchetes van dentro del parentesis 
print (playlistcurso[5])

print("TAMAÑO DEL ARREGLO")
listSize = len(playlistcurso)
print(listSize)
print("LA ULTIMA CACION ES")
print(playlistcurso[listSize-1])

print("imprimir todas las letras de una palabra")
palabra= "cristiano ronaldo"
for i in range(len(palabra)):
        print (palabra[i])