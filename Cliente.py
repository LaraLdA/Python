from socket import * # biblioteca que cria ferramentas e estabelece comunicação entre processos
# comunicação de um cliente que faz parte da rede com o nosso servidor.
servidor = "127.0.0.1"
porta = 43210

while True: # laço que possibilita que o cliente mande mais de uma mensagem para o servidor
    obj_socket = socket(AF_INET, SOCK_STREAM)
    obj_socket.connect((servidor, porta))  # conexao com o servidor, função connect
    msg = bytes(input("Digite sua mensagem: "),'utf-8') # o sockt so transmite dados do tipo byte
    obj_socket.send(msg) #envio da mensagem
    resposta=obj_socket.recv(1024) # recebe o dado enviado pelo serivdor
    print("Resposta do Servidor ",str(resposta)[2:-1])
    if str(msg)[2:-1].upper()=="FIM": #encerra a conversa
        break
obj_socket.close()