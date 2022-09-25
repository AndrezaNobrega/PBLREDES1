import requests
#Front end das telas de usuário e de admin



def menu():
    print('_______________________________________________________')
    print('####################### M E N U #######################')
    print('_______________________________________________________')
    print('1) Cliente')
    print('2) Admin')
    resposta = input('Digite a opção: ')
    if resposta == '1':
        print('_______________________________________________________')
        print('####################### M E N U #######################')
        print('_____________________U S U Á R I O_____________________')
        print('')
        resposta = input('Digite sua matrícula: ')
        print('Bem vindo',  resposta)   
        print('1) Histórico do consumo') 
        print('2) Litros Acumulados')
        print('3) Valor')
        print('4) Pagar')
        print('5) Retornar para o menu')
        opcao = input('Digite a opção que deseja escolher: \n')  
        if opcao == '1':
            url = "http://127.0.0.1:5002/users"
            print('HISTÓRICO DE CONSUMO:')            
            payload = {"search": resposta}
            print('')
            print('Aguarde alguns instantes enquanto a consulta é realizada')
            print('')
            headers = {"Content-Type": "application/json"}
            response = requests.request("GET", url, json=payload, headers=headers)
            print(response.text)
            menu()
        elif opcao == '2':
            url = "http://127.0.0.1:5002/litros"
            print('TOTAL DE LITROS CONSUMIDOS:')
            print('')
            print('Aguarde alguns instantes enquanto a consulta é realizada')
            print('')
            payload = {"search": resposta}
            headers = {"Content-Type": "application/json"}
            response = requests.request("GET", url, json=payload, headers=headers)
            print(response.text)
            menu()
        elif opcao == '3':
            print('Valor da sua conta')
            print('')
            print('Aguarde alguns instantes enquanto a consulta é realizada')
            print('')
            url = "http://127.0.0.1:5002/valor"
            payload = {"search": resposta}
            headers = {"Content-Type": "application/json"}
            response = requests.request("GET", url, json=payload, headers=headers)
            print(response.text)
            menu()
        elif opcao == '4':
            print('Efetuar o pagamento da sua conta')
            url = "http://127.0.0.1:5002/ip"
            payload = {"search": resposta}
            headers = {"Content-Type": "application/json"}
            response1 = requests.request("GET", url, json=payload, headers=headers)            
            url = "http://127.0.0.1:5002/valor"
            payload = {"search": resposta}
            headers = {"Content-Type": "application/json"}
            response = requests.request("GET", url, json=payload, headers=headers)
            print(response.text)
            print(response1.text)
            print('Código da conta, digite para efetuar o pagamento')
            ip = str(input('Digite: \n'))
            url = "http://127.0.0.1:5002/desbloqueia"

            payload = {
                "search": resposta,
                "ip": ip
            }
            headers = {"Content-Type": "application/json"}

            response = requests.request("POST", url, json=payload, headers=headers)

            print(response.text)
            menu()
        elif opcao == '5':
            menu()
    else:
        print('Menu aministrador')
        senha = input('Digite aqui a senha: ')
        if senha == '1234':
            print('_______________________________________________________')
            print('####################### M E N U #######################')
            print('________________A D M I N S T R A D O R________________')
            print('')
            print('Bem vindo, Admin!')
            print('Digite a opção: \n')
            print('1) Liste todos os hidrômetros com status e valor a ser pago')
            print('2) Listra hidrometros com possível vazamento')           
            print('3) Bloqueia um usuário')            
            print('4) Volar para o menu')
            opcao = input('Digite aqui a opção que deseja acessar: \n')
            if opcao == '1':
                print('Listagem de todos os hidrômetros com Status de débito e valor a ser pago')
                print('')
                print('Aguarde alguns instantes enquanto a consulta é realizada')
                print('')
                url = "http://127.0.0.1:5002/admin"
                headers = {"Content-Type": "application/json"}
                response = requests.request("GET", url, headers=headers)
                print(response.text)
                menu()
            elif opcao == '2':
                print('Listagem de todos os hidrômetros com um possível vazamento na região')
                print('')
                print('Aguarde alguns instantes enquanto a consulta é realizada')
                print('')
                url = "http://127.0.0.1:5002/notifica"
                headers = {"Content-Type": "application/json"}
                response = requests.request("GET", url, headers=headers)
                print(response.text)
                menu()
            elif opcao == '3':
                print('bloqueio de hidrômetro')
                id = str(input('Digite aqui o id do hidrômetro que será bloqueado'))
                print('')
                print('Aguarde alguns instantes')
                print('') 
                #método de consulta do IP               
                url = "http://127.0.0.1:5002/ip"
                payload = {"search": id}
                headers = {"Content-Type": "application/json"}
                response = requests.request("GET", url, json=payload, headers=headers)
                print('Código do hidrometro. Use-o para o bloqueio')
                print(response.text)
                ip = str(input('Digite aqui o código do hidrômetro que será bloqueado'))
                #método de bloqueio
                url = "http://127.0.0.1:5002/bloqueia"
                payload = {
                    "search": id,
                    "ip": ip
                }
                headers = {"Content-Type": "application/json"}
                response = requests.request("POST", url, json=payload, headers=headers)
                print(response.text)
                menu()
            else:
                menu()  
        else:
            print('Senha errada!')
            menu()

menu()