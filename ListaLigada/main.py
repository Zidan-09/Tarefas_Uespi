from models import No, Item
from func import *

l1 = criar()

for i in range(int(input('Quantos itens:'))):
    l1.Adicionar(No(Item(int(input('Chave:')), int(input('Valor:'))), None))
print('L1 feita')

l2 = criar()

for i in range(int(input('Quantos itens:'))):
    l2.Adicionar(No(Item(int(input('Chave:')), int(input('Valor:'))), None))
print('L2 feita')

l3 = Intercalar(l1, l2)

Imprimir(l3)