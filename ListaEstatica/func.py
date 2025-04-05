from models import Item, ListaEstatica

def Criar(tamanho):
    lista = ListaEstatica(tamanho)
    print('Lista criada com sucesso!')

    return lista

def Imprimir(Lista):
    print('Itens da lista:')
    for i in range(Lista.tamanho):
        print(Lista.lista[i] if Lista.lista[i] is not None else None, end=' ')
    print()

def Contar(Lista):
    print(f'A lista tem {Lista.tamanho} espaços e {Lista.espaco} estão vazios!')

def VerificarOrdem(Lista):
    c = 0
    d = 0

    for i, j in zip(range(Lista.tamanho), range(1, Lista.tamanho)):
        if Lista.lista[i] == None:
            break
        if Lista.lista[j] is not None:
            if Lista.lista[i].chave > Lista.lista[j].chave:
                c += 1
            
            elif Lista.lista[i].chave > Lista.lista[j].chave and Lista.lista[j] is not None:
                d += 1
    
    if c > 0 and d == 0:
        return True, 'crescente'
    elif c == 0 and d > 0:
        return True, 'decresente'
    else:
        return False, None

def Ordenar(Lista):
    temp = None
    trocou = True
    sentido = input('Crescente ou decrescente (c/d):')

    while trocou:
        trocou = False

        if sentido == 'c':

            for i, j in zip(range(Lista.tamanho), range(1, Lista.tamanho)):
                if Lista.lista[j] is not None:
                    if Lista.lista[i].chave > Lista.lista[j].chave:
                        temp = Lista.lista[i]
                        Lista.lista[i] = Lista.lista[j]
                        Lista.lista[j] = temp
                        trocou = True
        elif sentido == 'd':
                for i, j in zip(range(Lista.tamanho), range(1, Lista.tamanho)):
                    if Lista.lista[j] is not None:
                        if Lista.lista[i].chave < Lista.lista[j].chave:
                            temp = Lista.lista[i]
                            Lista.lista[i] = Lista.lista[j]
                            Lista.lista[j] = temp
                            trocou = True

    return Lista

def Recuperar(Lista, chave):
    procurou = True
    meio = Lista.tamanho // 2

    while procurou:
        print(Lista.lista[meio:])
        procurou = False

        if chave > meio:
            meio += meio // 2
            procurou = True
        elif chave < meio:
            meio -= meio // 2
            procurou = True
        elif chave == meio:
            print(Lista.lista[chave])
        

