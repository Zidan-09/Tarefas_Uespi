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

def Ordenar(Lista): #Troca os ITENS
    trocou = True

    while trocou:
        trocou = False

        anterior = Lista.ponteiro
        atual = anterior.ponteiro

        while atual != None:
            if anterior.item.chave > atual.item.chave:
                temp = anterior.item
                anterior.item = atual.item
                atual.item = temp

                trocou = True
            
            anterior = atual
            atual = atual.ponteiro
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

    inserir = Lista

    for _ in range(Lista.quantidade):
        l2.Adicionar(No(Item(inserir.ponteiro.item.chave, inserir.ponteiro.item.valor), None))
        inserir = inserir.ponteiro

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

def Remover(Lista, pos):
        ordem, sentido = VerificarOrdem(Lista)

        if not ordem:
            Ordenar(Lista)
            ordem, sentido = VerificarOrdem(Lista)
        
        try:
            lista = Lista
            temp = Lista
            contador = 1

            while True:
                    if contador == pos:
                        temp.ponteiro = temp.ponteiro.ponteiro
                        print('Item removido com sucesso!')
                        Lista.quantidade -= 1
                        return lista
                    temp = temp.ponteiro
                    contador += 1
        
        except:
            raise 'Erro ao remover'

def Imprimir(Lista):
    temp = Lista
    print('Itens da Lista:')
    for _ in range(Lista.quantidade):
        print(temp.ponteiro, end=' ')
        temp = temp.ponteiro
    print()

def Copiar(Lista):
    l2 = criar()

    temp = Lista

    for _ in range(Lista.quantidade):
        l2.Adicionar(No(Item(temp.ponteiro.item.chave, temp.ponteiro.item.valor), None))
        temp = temp.ponteiro

    return l2

def CopiarSemRepetir(Lista):
    l2 = criar()

    temp = Lista
    valores = []

    for _ in range(Lista.quantidade):
        if temp.ponteiro.item.valor not in valores:
            l2.Adicionar(No(Item(temp.ponteiro.item.chave, temp.ponteiro.item.valor), None))
            valores.append(temp.ponteiro.item.valor)
        temp = temp.ponteiro
    
    return l2

def Contar(Lista):
    print(f'A lista tem {Lista.quantidade} itens')

def Intercalar(Lista1, Lista2):
    l3 = criar()

    temp1 = Lista1
    temp2 = Lista2

    c = 0

    for _ in range(Lista1.quantidade + Lista2.quantidade):
        if temp1.ponteiro != None and temp2.ponteiro != None:
            if c % 2 == 0:
                l3.Adicionar(No(Item(temp1.ponteiro.item.chave, temp1.ponteiro.item.valor), None))
                temp1 = temp1.ponteiro
                c += 1

            elif c % 2 != 0:
                l3.Adicionar(No(Item(temp2.ponteiro.item.chave, temp2.ponteiro.item.valor), None))
                temp2 = temp2.ponteiro
                c += 1
        
        elif temp1.ponteiro != None and temp2.ponteiro == None:
            l3.Adicionar(No(Item(temp1.ponteiro.item.chave, temp1.ponteiro.item.valor), None))
            temp1 = temp1.ponteiro
        
        elif temp1.ponteiro == None and temp2.ponteiro != None:
            l3.Adicionar(No(Item(temp2.ponteiro.item.chave, temp2.ponteiro.item.valor), None))
            temp2 = temp2.ponteiro
    
    return l3