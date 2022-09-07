import threading
import hidrometro #importando CLIENTE UDP

hidrometro1 = hidrometro.Hidrometro('0023') #cria objeto
print('A VAZÃO DEVE SER SEMPRE NO FORMATO XX \n A ID DEVE TER O FORMATO DE XXXX')
dado = '15'
hidrome = threading.Thread(target = hidrometro1.enviaDado(dado), name = 'gera') #aaqui cria como thread
hidrome.start() #starta a thread
