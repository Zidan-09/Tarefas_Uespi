class Processo:
    def __init__(self, size, id):
        self.id = id
        self.size = size

    def __repr__(self):
        return f'ID = {self.id:02}, Size = {self.size:02}'

class Processado:
    def __init__(self, processo, turn, tw):
        self.processo = processo
        self.turnAround = turn
        self.timeWait = tw

class Processador:
    def __init__(self):
        self.processos = []

    def addProcess(self, process):
        self.processos.append(process)

    def showProcess(self):
        print('Lista de processos:')
        for i in self.processos:
            print(i)
        print()

    def fifo(self):
        timeWaits = 0
        result = []

        for i, processo in enumerate(self.processos):
            if i == 0:
                result.append(Processado(processo, processo.size, 0))
            else:
                result.append(Processado(processo, processo.size + timeWaits, timeWaits))
                
            timeWaits += processo.size

        print('---------------------------------------------------------------')
        print('ID     SIZE     TA     TW')
        for i in result:
            print(f'{i.processo.id:02}      {i.processo.size:02}      {i.turnAround:02}     {i.timeWait:02}')
        print()
        print('DEBUG', timeWaits)
        print(f'Tempo médio de turnAround: {(timeWaits + self.processos[-1].size) / len(self.processos):.2f}')
        print(f'Tempo médio de timeWaits: {timeWaits / len(self.processos):.2f}')

    def sjf(self):
        timeWaits = 0
        result = []
        sortedList = sorted(self.processos, key=lambda p: p.size)

        for i, processo in enumerate(sortedList):
            if i == 0:
                result.append(Processado(processo, processo.size, 0))
            else:
                result.append(Processado(processo, processo.size + timeWaits, timeWaits))
            timeWaits += processo.size

        print('---------------------------------------------------------------')
        print('ID     SIZE     TA     TW')
        for i in result:
            print(f'{i.processo.id:02}      {i.processo.size:02}      {i.turnAround:02}     {i.timeWait:02}')
        print()
        print(f'Tempo médio de turnAround: {(timeWaits + sortedList[-1].size) / len(sortedList):.2f}')
        print(f'Tempo médio de timeWaits: {timeWaits / len(sortedList):.2f}')

class Execucao:
    @staticmethod
    def inicio(core):
        while True:
            try:
                qtd = int(input('\nQuantos processos você gostaria de adicionar?: '))
                break
            except ValueError:
                print("Por favor, insira um número inteiro válido.")

        for i in range(1, qtd + 1):
            while True:
                try:
                    size = int(input(f'Insira o tamanho do processo {i}: '))
                    break
                except ValueError:
                    print("Tamanho inválido. Digite um número inteiro.")
            core.addProcess(Processo(size, i))

        print('\n---------------------------------------------------------------')
        core.showProcess()
        print('---------------------------------------------------------------\n')

    @staticmethod
    def metodo(core):
        core.fifo()
        core.sjf()

        while True:
            continuar = input('Gostaria de reiniciar a simulação (R) ou fechar (F)?: ').upper()
            if continuar in ['R', 'F']:
                return continuar
            print("Opção inválida. Digite R ou F.")

def main():
    core = Processador()
    while True:
        Execucao.inicio(core)
        resposta = Execucao.metodo(core)

        if resposta == 'R':
            core = Processador()
        elif resposta == 'F':
            print('Simulação finalizada.')
            break

if __name__ == "__main__":
    main()