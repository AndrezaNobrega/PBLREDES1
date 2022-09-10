from threading import Thread
from threading import Event
from time import sleep
import datetime

class Hidrometro(Thread):
    def __init__(self):
        self._active = Event()
        self._active.set()
        Thread.__init__(self)

    def run(self):
        global x
        dado = 10
        vazao = dado
        while True:
            self._active.wait()
            vazao = int(vazao)  
            dado = int(dado)                
            dado = dado+vazao
            dado = str(dado)
            vazao = str(vazao)
            data = datetime.datetime.now() #horário atual
            dataAux = str(data) #convertendo para string
            dataAux= dataAux[:16] #recortando horas e segundos            
            print ('\n ID:', id ,'\nLitros utilizados:', dado, '\nData do envio:', dataAux, '\nVazão atual:', vazao)
            x+=1
            sleep(5)

    def stop(self):
        self._active.clear()

    def play(self):
        self._active.set()


h = Hidrometro()
h.run()