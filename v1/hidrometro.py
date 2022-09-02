



class Hidrometro:
    def __init__(self, id) -> None:
        self.id = id
        self.totalGasto = 0
        self.horarioConsumo = list()
        self.bloqueado = False

    def info(self):
        return self.id, self.totalGasto, self.horarioConsumo, self.bloqueado
    
    def geraGasto(self, gasto):
        gasto += self.totalGasto
        self.totalGasto = gasto
        return self.totalGasto
    
    def addConsumo(self, consumoAgora):
        self.horarioConsumo.append(consumoAgora)
        return self.horarioConsumo



#testando o hidrometro
print('Iniciando o hidrometro')
id =input('Insira o id do hidrometro')
hidrometro = Hidrometro(id)
print('O hidrometro foi criado com a id', hidrometro.id)
bloqueado = 's'
while bloqueado == 's':
    print('Regule litros da vazão do seu hidrometro')
    consumo = int(input('Quantos litros deseja para a vazão?'))
    print(consumo)
    hidrometro.geraGasto(consumo)
    bloqueado = input('Deve continuar enviand? [s/n]') #Aqui no programa original não vai ter
    print('O total gerado foi de', hidrometro.totalGasto)

