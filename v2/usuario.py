class Usuário:
    def __init__(self, id):
        self.id = id
        self.bloqueado = False
        self.nome = 'nome' 

    def getId(self): #retorna ID
        return id

    def setBloqueado(self): #Bloquear e desbloquear hidrometro
        if self.bloqueado == False:
            bloqueado = True
            self.bloqueado = bloqueado
        else:
            self.bloqueado = False
        return self.bloqueado