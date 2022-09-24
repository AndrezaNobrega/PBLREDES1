<p align="center">
 <img width="100px" src="https://th.bing.com/th/id/R.02dc5a07fba13bf8fafcd5a9ef4650f2?rik=eUGmhqSWUgGq3Q&riu=http%3a%2f%2fdesignlooter.com%2fimages%2fwater-drop-svg-2.png&ehk=wRcSGTKTSlUGC4f05vU4XiJGsENTi9gq1%2fDJzsp%2fIIQ%3d&risl=&pid=ImgRaw&r=0" align="center" alt="GitHub Readme Stats" />
 <h2 align="center">Sistema para controle de consumo da água</h2>
 <p align="center">Projeto desenvolvido no MI de concorrência e conectividade.</p>
</p>
<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge"/>
</p>

# Componentes

- [Hidrômetro](#Hidrometro)
- [Servidor](#Servidor)
- [Tela do usuário](#usuario)
- [Tela do administrador](#admin)
- [API REST](#api)

# Hidrômetro

O componente hidrômetro envia dados de forma contínua para o servidor, estes são:
- Litros utilizados;
  Os litros são somados com a vazão do momento, para gerar o que foi consumido.
- Horário;
  O horário do gasto é sempre enviado, para que possa ser acompanhado pelo usuário e para controle do Administrador.
- Vazão;
  A vazão do hidrômetro é enviada, também pode ser alterada na própria interface do usuário;
- ID:
  A id do hidrômetro é a mesma do usuário, afim de atrelar o consumo a ele;
- Vazamento:
  O hidrômetro conta coom um sistema que verifica o tempo todo a pressão exercida pela água nele, por motivos de simulação esses dados são gerados de 0 a 9, caso seja 0, o hidrômetro retornará o valor 0, o que indica um possível vazamento naquela região.
  
  
 # Servidor

O servidor recebe os dados dos hidrômetros, os trata e envia para a nuvem (google sheets). Admite vários hidrômetros na conexão.

# Tela do usuário
O usuário se conecta ao BD por meio da API Rest. Este, por sua vez, possui um menu do usuário que apresenta as seguintes atribuições:
- Visualizar o histórico de consumo;
- Visualizar os liros consumidos;
- Visualizar o valor da sua conta;
- Pagar a sua conta;

# Tela do administrador 
O admin se conecta ao BD por meio da API rest. Que possui um menu, onde apresenta as seguintes atribuições:
- Listar todos os usuários com o Status e valor a ser pago;
  O status é gerado da seguinte forma: por motivos acadêmicos, são contabilizados dois minutos para o usuário ficar em débito.
- Pode bloquear um usuário;
- Lista também os hidrômetros com possível vazamento;
- A senha é 1234;

# Api Rest

A API Rest conecta o usuário e administrador ao banco de dado (google sheets). Possui métodos get, para histórico, listros consumidos, valor, status, admin e notificação. Também, post para bloqueio e desbloqueio dos hidrômetros. 





