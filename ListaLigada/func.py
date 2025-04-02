from models import No, Item

def VerificarOrdem(Lista):
    anterior = Lista
    temp = Lista.ponteiro

    c = 0
    d = 0

    while temp.ponteiro != None:
        if anterior.ponteiro.item.chave > temp.ponteiro.item.chave:
            d += 1
        elif anterior.ponteiro.item.chave < temp.ponteiro.item.chave:
            c += 1

        anterior = temp
        temp = temp.ponteiro

    if c > 0 and d == 0:
        print('Lista em ordem crescente.')
        return True, 'crescente'
    
    elif c == 0 and d > 0:
        print('Lista em ordem decrescente.')
        return True, 'decrescente'
    
    else:
        print('Lista não está ordenada.')
        return False, None

def Ordenar(Lista):
    ordem = input('Ordem crescente ou decrescente (c/d):')

    if ordem == 'c':
        while True:
            trocou = False
            anterior = None
            atual = Lista.ponteiro

            while atual != None and atual.ponteiro != None:
                proximo = atual.ponteiro

                if atual.item.chave > proximo.item.chave:
                
                    atual.ponteiro = proximo.ponteiro
                    proximo.ponteiro = atual

                    if anterior == None:
                        Lista.ponteiro = proximo

                    else:
                        anterior.ponteiro = proximo

                    trocou = True
                    anterior = proximo

                else:
                    anterior = atual
                    atual = atual.ponteiro

            if not trocou:
                break

        return Lista
    
    elif ordem == 'd':
        while True:
            trocou = False
            anterior = None
            atual = Lista.ponteiro

            while atual != None and atual.ponteiro != None:
                proximo = atual.ponteiro

                if atual.item.chave < proximo.item.chave:
                
                    atual.ponteiro = proximo.ponteiro
                    proximo.ponteiro = atual

                    if anterior == None:
                        Lista.ponteiro = proximo

                    else:
                        anterior.ponteiro = proximo

                    trocou = True
                    anterior = proximo

                else:
                    anterior = atual
                    atual = atual.ponteiro

            if not trocou:
                break

    return Lista

def Inverter(Lista):
    pass