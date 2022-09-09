from socket import *
# ferramenta que "escuta" e atende aos pedidos dos clientes

servidor = "127.0.0.1" # localhost
porta = 43210
obj_socket = socket(AF_INET, SOCK_STREAM) # objeto criado definie a familia responsavel por identificar os pacotes (AF_INET - utiliza a identificação do emissor/receptor do pacote via DNS ou IP)
#e transporte do pacote (SOCK_STREAM - via TCP)
obj_socket.bind((servidor,porta)) # associação do objeto com servidor e porta
obj_socket.listen(2) #máximo de clientes que o servidor atende simultaneamente
print("Aguardando cliente....")
while True:
    con, cliente = obj_socket.accept() # aguarda um cliente - funçao accept. A identificação do cliente e a da conexão (con)
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024)) # aguarda solicitação
        print("Recebemos: ", str(msg_recebida)[2:-1]) # conversão da mensagem para string. e slice que pega a partir do segundo caractere.
        msg_enviada = bytes(input("Sua resposta "), 'utf-8') # gera uma mensagem para ser enviada no formato de bytes
        con.send(msg_enviada)
        break
    con.close() # fecha a conexao e volta-se a aguardar uma nova