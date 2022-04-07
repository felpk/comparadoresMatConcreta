# PROGRAMA DE FUNCOES

def geradora ():        # GERA LISTAS 1 E 2 COM 100 INDICES
    from random import randint
    lista1 = []
    lista2 = []

    for c in range(0, 100):
        lista1.append(0)
        lista2.append(0)

    return lista1, lista2

def zeropraum (lista2):     # MUDA UM INDICE ALEATORIO DE 0 PARA 1
    from random import randint
    i = randint(0, 99)
    lista2[i] = 1

def csequencial(lista1, lista2):  # COMPARADOR SEQUENCIAL
    cont = 0
    for c in range(0, len(lista1)):
        if lista1[c] != lista2[c]:
            cont+=1
            break
        else:
            cont+=1 

    return cont 

def caleatorio(lista1, lista2):     # COMPARADOR ALEATORIO
    from random import randint

    cont = 0
    iusados = list()                # LISTA COM INDICES JA SORTEADOS

    for c in range(0, len(lista1)):
        i = randint(0, 99)

        if i not in iusados:        # VERIFICA SE INDICE JA FOI SORTEADO
            if lista1[i] != lista2[i]:
                cont+=1
                break
            
            else:
                cont+=1
                iusados.append(i)

        if i in iusados:
            pass

    return cont



