import time
import threading    

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
        
    def turnAround(self):
        timeWaits = 0
        result = []

        for i in range(len(self.processos)):
            if i == 0:
                processado = Processado(self.processos[i], self.processos[i].size, 0)
                result.append(processado)

            else:
                processado = Processado(self.processos[i], self.processos[i].size + timeWaits, timeWaits)
                result.append(processado)
            
            timeWaits += self.processos[i].size

        print('---------------------------------------------------------------')
        print('ID     SIZE     TA     TW')
        for i in result:
            print(f'{i.processo.id:02}      {i.processo.size:02}      {i.turnAround:02}     {i.timeWait:02}')
        print()

    def sfj(self):
        timeWaits = 0
        result = []
        sortedList = sorted(self.processos, key=lambda p: p.size)
        
        for i in range(len(self.processos)):
            if i == 0:
                processado = Processado(sortedList[i], sortedList[i].size, 0)
                result.append(processado)

            else:
                processado = Processado(sortedList[i], sortedList[i].size + timeWaits, timeWaits)
                result.append(processado)
            
            timeWaits += sortedList[i].size

        print('---------------------------------------------------------------')
        print('ID     SIZE     TA     TW')
        for i in result:
            print(f'{i.processo.id:02}      {i.processo.size:02}      {i.turnAround:02}     {i.timeWait:02}')
        print()
    
    def executeWithThreads(self):
        threads = []

        for process in self.processos:
            t = threading.Thread(target=executeProcess, args=(process,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print("Todos os processos foram executados.")

def executeProcess(processo):
    print(f"[Thread] Iniciando execução do processo {processo.id:02} (tamanho: {processo.size})")
    time.sleep(5)
    print(f"[Thread] Processo {processo.id:02} finalizado.")

core = Processador()

for i in range(1, int(input('Quantos processos você gostaria de adicionar?: ')) + 1):
    core.addProcess(Processo(int(input('Insira o tamanho do processo: ')), i))

core.showProcess()

core.turnAround()

core.sfj()

core.executeWithThreads()