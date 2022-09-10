import threading
import hidrometro #importando CLIENTE UDP


print('----------------------------------------------------------------------')
print('---------------------------PAINEL HIDROMETRO--------------------------')
print('----------------------------------------------------------------------')
print('\nA VAZÃO DEVE SER SEMPRE NO FORMATO XX \n A ID DEVE TER O FORMATO DE XXXX')
print('----------------------------------------------------------------------')
hidrometroiD = str(input('DIGITE O ID DO HIDROMETRO:'))
hidrometro1 = hidrometro.Hidrometro(hidrometroiD) #cria objeto
r = 0
while r != 'n':
    print('----------------------------------------------------------------------')
    print('---------------------REGULE A VAZÃO DO HIDROMETRO---------------------')
    print('----------------------------------------------------------------------')
    print('\nA VAZÃO DEVE SER SEMPRE NO FORMATO ''XX'' \n A ID DEVE TER O FORMATO DE ''XXXX''')
    print('----------------------------------------------------------------------')
    dado = input('[Digite aqui a vazão que deseja]')
    hidrome = threading.Thread(target = hidrometro1.enviaDado(dado), name = 'gera') #aaqui cria como thread
    hidrome.start() #starta a thread
    print('----------------------------------------------------------------------')
    r = input('Deseja continuar regulando a vazão do hidrometro? [''n'' para parar]')

