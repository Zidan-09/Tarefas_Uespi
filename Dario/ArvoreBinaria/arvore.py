class Item:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.valor}'


class Tree:
    def __init__(self):
        self.raiz = None
        self.qty = 0

    def inserir(self, item):
        self.qty += 1
        temp = self.raiz
        
        if self.raiz == None:
            self.raiz = item
        else:
            while True:
                if temp.valor > item.valor:
                    if temp.left == None:
                        temp.left = item
                        return self
                    else:
                        temp = temp.left
                else:
                    if temp.right == None:
                        temp.right = item
                        return self
                    else:
                        temp = temp.right
                    

    def ver(self, valor):
        temp = self.raiz

        for i in range(self.qty):

            print(temp)

            if temp == None:
                return 'achei!'
            elif temp.valor == valor:
                return 'Achei'
            
            if valor < temp.valor:
                temp = temp.left
            else:
                temp = temp.right


tree = Tree()

i1 = Item(13)
i2 = Item(10)
i3 = Item(25)
i4 = Item(2)
i5 = Item(12)
i6 = Item(20)
i7 = Item(31)
i8 = Item(29)

l = [i1, i2, i3, i4, i5, i6, i7, i8]

for i in l:
    tree.inserir(i)

tree.ver(12)