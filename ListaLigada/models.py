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
        self.quantidade = 0
    
    def __repr__(self):
        return f'{self.item}'
    
    def Adicionar(self, No):
        try:
            lista = self
            temp = self

            while True:
                if temp.ponteiro == None:
                    temp.ponteiro = No
                    print('Item adicionado com sucesso!')
                    self.quantidade += 1
                    return lista
                temp = temp.ponteiro

        except:
            raise 'Erro'
    
    def Remover(self, Valor):
        try:
            lista = self

            temp = self.ponteiro
            anterior = self

            while temp != None:
                if temp.item.valor == Valor:
                    anterior.ponteiro = temp.ponteiro

                else:
                    anterior = temp
                temp = temp.ponteiro

            print('Itens removidos com sucesso!')
            return lista
        
        except:
            raise 'Erro ao remover!'