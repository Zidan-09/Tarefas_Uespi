from models import No, Item
from func import *

l1 = criar()

for _ in range(int(input('Quantos itens:'))):
    l1.Adicionar(No(Item(int(input('Chave:')), int(input('Valor:'))), None))

Imprimir(l1)

l2 = criar()

for _ in range(int(input('Quantos itens:'))):
    l2.Adicionar(No(Item(int(input('Chave:')), int(input('Valor:'))), None))

Imprimir(l2)

VerificarOrdem(l1)
VerificarOrdem(l2)

Inverter(l1)
l3 = InverterNova(l2)

Inserir(l2, int(input('Posição da inserção:')))

Remover(l2, int(input('Posição da remoção:')))

l4 = Copiar(l3)

l5 = CopiarSemRepetir(l4)

l6 = Intercalar(l1, l2)

Imprimir(l6)

Contar(l4)