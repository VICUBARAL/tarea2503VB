
## EJERCICIO 1
def SuperficieRectangulo(base,altura):
    return base * altura
SuperficieRectangulo(5,6)

## EJERCICIO 2
def SuperficieTrianguloRectangulo (base,altura):
    return (base * altura)/2
SuperficieTrianguloRectangulo(4,5)

## EJERCICIO 3
def DescubrirNumeroPrimo(numero):
    for n in range (2, numero):
        if numero % n == 0:
            print ("No es primo", n , "es divisor")
            return False
    print ("Es primo!!")
    return True
DescubrirNumeroPrimo(37)

## EJERCICIO 4

def ContarCaracteresEnCadena(n):
    contador = 0
    while n:
        contador = contador + 1
        
    return contador
ContarCaracteresEnCadena(a)

## EJERCICIO 5

def Capicua(cadena):
    longitud = len(cadena)
    if longitud % 2 == 0:
        izquierda = cadena[:longitud // 2 -1 ]
        derecha = cadena [longitud // 2 ]
    else: 
        izquierda = cadena [:longitud // 2 - 1 ]
        derecha = cadena [longitud // 2 + 1 ]
    return izquierda == derecha [:: -1 ]

## EJERCICIO 6








