def suma_cifras_pares(numero):
    suma=0
    while numero>0:
        if (numero%10)%2==0:
            suma= suma+numero%10
        numero= numero/10
    respuesta=suma+numero
    return respuesta

def suma_cifras_impares(numero):
    suma=0
    while numero>0:
        if (numero%10)%2==1:
            suma= suma+numero%10
        numero= numero/10
    respuesta=suma+numero
    return respuesta

def cifra_mayor(numero):
    cifra=0
    while numero>0:
        if (numero%10)>cifra:
            cifra=numero%10
        numero= numero/10
    respuesta=cifra
    return respuesta

def numero_ordenado(numero):    
    exp=0    
    n=numero
    expo=0
    cifra=0
    final=0
    nu=0
    ex=0
    exponente=0        
    while n>0:               
        n/10
        exp=exp+1                  
    ex=exp
    n=numero
    while n>0:        
        expo=expo+1        
        nu=n
        cifra=0
        while nu>0:            
            if (nu%10)>cifra:
                cifra=nu%10            
                ex=exp
                nu=nu/10
            else:
                ex=ex-1
                nu=nu/10
        n=(n-(cifra*(10**ex)))        
           
        final=final+(cifra*10**expo)
        exp=exp-1
    return final
            
def suma_selectiva():
    numero=input("Inserte su número entero: ")
    print "1. Devuelve la suma de sus cifras pares"
    print "2. Devuelve la suma de sus cifras impares"
    print "3. Devuelve la mayor de sus cifras"
    print "4. Devuelve un número con las mismas cifras ordenadas de menor a mayor"
    opcion=input("¿Qué deseas hacer con tu número? Selecciona un número: ")
    if opcion==1:
        print "La suma de las cifras pares de tu número es: " ,suma_cifras_pares(numero),
    if opcion==2:
        print "La suma de las cifras impares de tu número es: " ,suma_cifras_impares(numero),   
    if opcion==3:
        print "La cifra mayor de tu número es: " ,cifra_mayor(numero),
    if opcion==4:
        print "El número ordenado de menor a mayor es: " ,numero_ordenado(numero),

suma_selectiva()








