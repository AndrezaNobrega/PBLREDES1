import threading
import hidrometro #importando CLIENTE UDP

hidrometro1 = hidrometro.Hidrometro(123) #cria objeto

dado = '15'
hidrome = threading.Thread(target = hidrometro1.enviaDado(dado), name = 'gera') #aaqui cria como thread
hidrome.start() #starta a thread
