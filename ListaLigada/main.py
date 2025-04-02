from models import No, Item
from func import *

def criar():
    no_cabeca = No(Item(None, None), None)
    print('Lista criada com sucesso!')

    return no_cabeca

l1 = criar()

for i in range(int(input('Quantos itens:'))):
    l1.Adicionar(No(Item(int(input('Chave:')), int(input('Valor:'))), None))

Inverter(l1)

temp = l1
while temp.ponteiro != None:
    print(temp.ponteiro)
    temp = temp.ponteiro