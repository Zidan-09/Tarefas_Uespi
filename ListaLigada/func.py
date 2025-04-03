from models import No, Item

def criar():
    no_cabeca = No(Item(None, None), None)
    print('Lista criada com sucesso!')

    return no_cabeca

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
    primeiro = Lista.ponteiro

    atual = primeiro.ponteiro
    proximo = atual.ponteiro

    while proximo != None:
        atual.ponteiro = primeiro
        primeiro = atual
        atual = proximo
        proximo = proximo.ponteiro

        if proximo == None:
            atual.ponteiro = primeiro
            break
    
    Lista.ponteiro.ponteiro = None
    Lista.ponteiro = atual

    return Lista

def InverterNova(Lista):
    l2 = criar()

    primeiro = Lista.ponteiro

    atual = primeiro.ponteiro
    proximo = atual.ponteiro

    while proximo != None:
        atual.ponteiro = primeiro
        primeiro = atual
        atual = proximo
        proximo = proximo.ponteiro

        if proximo == None:
            atual.ponteiro = primeiro
            break
    
    Lista.ponteiro.ponteiro = None
    Lista.ponteiro = atual
    l2.ponteiro = atual

    return l2

def Inserir(Lista, pos):
        ordem, sentido = VerificarOrdem(Lista)

        if not ordem:
            Ordenar(Lista)
            ordem, sentido = VerificarOrdem(Lista)
        
        try:
            lista = Lista
            temp = Lista

            item = No(Item(int(input('Chave:')), int(input('Valor:'))), None)
            if sentido == 'crescente':
                while True:
                    if temp.ponteiro.ponteiro.item.chave >= pos:
                        item.ponteiro = temp.ponteiro
                        temp.ponteiro = item
                        print('Item inserido com sucesso!')
                        Lista.quantidade += 1
                        return lista
                    temp = temp.ponteiro
            elif sentido == 'decrescente':
                while True:
                    if temp.ponteiro.ponteiro.item.chave <= pos:
                        item.ponteiro = temp.ponteiro
                        temp.ponteiro = item
                        print('Item inserido com sucesso!')
                        Lista.quantidade += 1
                        return lista
                    temp = temp.ponteiro

        except:
            raise 'Erro'