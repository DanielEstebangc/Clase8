import problema1
'''''
hasta ahora emos trabajado
con varios
variables que permiten almacenar un unico valor
'''''

edad = 12

altura = 1.79

nombre = "juan"

estado = True

'''''
en pyton podemos usar una variable que
 podemos usar una coleccion de 
 datos y luego acceder usando un subindice
'''''

#lista de enteros
lista1 = [10, 5, 3, 9]

#lista de decimales
lista2 = [1.78, 2.66, 1.55, 89.4, 6.9]

#lista de string
lista3 = ["lunes","martes","miercoles"]

'''''
lista de elementos 
de distinto tipo
'''''

lista4 = ["juan",45,1.92,False]


if __name__ == '__main__':

    ''''
    catidad de elementos de cada lista :
    '''
    print(len(lista1))
    print(len(lista2))
    print(len(lista3))
    print(len(lista4))

    print()
    print(lista1)
    lista1[0] = 1
    print()
    print(lista1)

    problema1.sumar_5_enteros()
