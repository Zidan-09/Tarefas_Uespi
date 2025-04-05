class Item:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor

    def __str__(self):
        return f'{self.valor}'

class ListaEstatica:
    def __init__(self, tamanho):
        self.lista = [None] * tamanho
        self.tamanho = tamanho
        self.espaco = tamanho
    
    def __repr__(self):
        return f'{self.lista}'
    
    def Adicionar(self, item):
        try:
            if self.espaco > 0:
                for i in range(self.tamanho):
                    if self.lista[i] == None:
                        self.lista[i] = item
                        self.espaco -= 1
                        break
            print('Item adicionado com sucesso!')
            return self
        except:
            raise Error('Erro ao adicionar!')

    def Eliminar(self, valor):
        try:
            for i in range(self.tamanho):
                if self.lista[i].item.valor == valor:
                    self.lista[i] = None
                    self.espaco += 1
            return self
        except:
            raise Error('Erro ao eliminar!')
