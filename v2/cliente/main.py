
import random
import hidrometro #importando CLIENTE UDP


print('----------------------------------------------------------------------')
print('---------------------------PAINEL HIDROMETRO--------------------------')
print('----------------------------------------------------------------------')
print('\nA VAZÃO DEVE SER SEMPRE NO FORMATO XX \n A ID DEVE TER O FORMATO DE XXXX')
print('----------------------------------------------------------------------')

id = random.randint(1000,9999) #gera a matrícula
hidrometroiD = str(random.randint(1000,9999))
hidrometro1 = hidrometro.Hidrometro(hidrometroiD) #cria objeto
r = 0
while r != 'n':
    print('----------------------------------------------------------------------')
    print('---------------------REGULE A VAZÃO DO HIDROMETRO---------------------')
    print('----------------------------------------------------------------------')
    print('\nA VAZÃO DEVE SER SEMPRE NO FORMATO ''XX'' \n A ID DEVE TER O FORMATO DE ''XXXX''')
    print('----------------------------------------------------------------------')
    dado = input('[Digite aqui a vazão que deseja]')
    hidrometro1.threadEnvia(15)    
    print('----------------------------------------------------------------------')
    r = input('Deseja continuar regulando a vazão do hidrometro? [''n'' para parar]')

