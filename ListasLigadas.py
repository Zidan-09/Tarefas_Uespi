class Item:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
    
    def __str__(self):
        return f'{self.valor}'

class No:
    def __init__(self, item, ponteiro):
        self.item = item
        self.ponteiro = ponteiro
    
    def __repr__(self):
        return f'{self.item}'

def VerificarOrdem(Lista):
    pass

def Ordenar(Lista):
    pass

def Copiar(Lista):
    pass

def CopiarSemRepetir(Lista):
    pass

def Inverter(Lista):
    pass

def InverterNova(Lista):
    pass

def Intercalar(Lista1, Lista2):
    pass

def RemoverItens(Lista):
    Ordem, sentido = VerificarOrdem(Lista)
    if Ordem == False:
        Lista = Ordenar(Lista)
    
    remover = int(input('remover item:'))