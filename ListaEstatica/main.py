from models import Item, ListaEstatica
from func import *

l1 = Criar(10)
for _ in range(5):
    l1.Adicionar(Item(int(input('Chave:')), int(input('Valor:'))))

Contar(l1)
VerificarOrdem(l1)
Imprimir(l1)
Ordenar(l1)
Imprimir(l1)
Recuperar(l1, 8)