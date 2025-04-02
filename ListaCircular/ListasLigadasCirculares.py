class Soldado:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __str__(self):
        return f'{self.nome}'

class No:
    def __init__(self, soldado, ponteiro):
        self.soldado = soldado
        self.ponteiro = ponteiro

    def __repr__(self):
        return f'{self.soldado}'

qty_soldados = int(input('Quantidade de soldados:'))

temp_soldado = Soldado(int(input('id:')), input('Nome:'))
temp_no = No(temp_soldado, None)

primeiro = [temp_no]

for i in range(qty_soldados - 1):

    soldado = Soldado(int(input('Id:')), input('Nome:'))
    no = No(soldado, None)

    temp_no.ponteiro = no
    temp_no = no

temp_no.ponteiro = primeiro[0]

soldado_escolhido = int(input('Qual o soldado (id):'))
vezes = int(input('Quantas vezes:'))

nos = primeiro[0]

for i in range(qty_soldados):

    if nos.soldado.id == soldado_escolhido:
        anterior = nos
        for j in range(vezes):
            anterior.ponteiro = nos
            nos = nos.ponteiro

        anterior.ponteiro = nos.ponteiro
        print(nos)
        print(anterior.item.valor)
        break
    else:
        anterior = nos
        nos = nos.ponteiro