from models import No, Item
from func import *

l1 = criar()

for i in range(int(input('Quantos itens:'))):
    l1.Adicionar(No(Item(int(input('Chave:')), int(input('Valor:'))), None))

temp = l1.ponteiro
while temp != None:
    print(temp)
    temp = temp.ponteiro

Inserir(l1, 5)

temp = l1.ponteiro
while temp != None:
    print(temp)
    temp = temp.ponteiro