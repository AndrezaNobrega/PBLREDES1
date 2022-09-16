
class Hidrometro: #construtor
    def __init__(self, id):
        self.id = id
        self.bloqueado = False       

    def getId(self): #retorna ID
        id = str(self.id)
        return id

    def setBloqueado(self): #Bloquear e desbloquear hidrometro
        if self.bloqueado == False:
            bloqueado = True
            self.bloqueado = bloqueado
        else:
            self.bloqueado = False
        return self.bloqueado    

