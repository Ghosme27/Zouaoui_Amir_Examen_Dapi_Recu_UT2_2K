import os
def OrdenarLista(lista):
    '''Como parametros recibiremos una lista,para meterlo en un fichero ordenado y como salida no devolvera nada'''
    lista.sort()
    with open('ListaOrdenada.txt','w') as file:
        file.writelines(lista)
        
    return

    


def NumeroPar(fichero):
    '''Como parametros recibiremos un fichero,para meterlo en un fichero nuevo que solo sean los numeros pares y como salida no devolvera nada'''
    lista_par = []
    with open(fichero,'r') as file:
        file.read()
    for i in fichero:
        if i % 2 == 0:
            lista_par.append(i)
        else:
            None 
    with open('Numeropar.txt','w') as file:
        file.writelines(lista_par)




d = ['1','8','5','6','-1']
OrdenarLista(d)
NumeroPar('ListaOrdenada.txt')
