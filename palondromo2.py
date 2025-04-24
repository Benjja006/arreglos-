
palabra ="girafarig"
nievapalabra=""

for i in range(len(palabra)):
    print(palabra [(len(palabra)-1) -i])  
    nievapalabra += (palabra [(len(palabra)-1) -i])
    print("la nueva palabra es : " + nievapalabra)

if palabra == nievapalabra:
    print( "la palabra :" + palabra "es igual a la palabra " + nievapalabra) 
else: 
    print("la palabra :" + palabra "es dstinta a la palabra " + nievapalabra) 