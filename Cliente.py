# ANA THAMYRES
# CLIENTE (inicia a conexão)

import socket
import threading

PORT = 65432 # Porta que o servidor está usando

# Função para receber mensagens do servidor
def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            # Se houver algum erro, encerra a conexão
            client.close()
            break

# Configuração do socket do cliente
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    # Solicita o endereço IP do servidor ao usuário
    HOST = input("Digite o endereço IP do servidor: ")

    client.connect((HOST, PORT))
    print('Conexão estabelecida com o servidor')
    

    # Inicia uma thread para receber mensagens do servidor
    thread = threading.Thread(target=receive)
    thread.start()

    # Envia mensagens para o servidor
    while True:
        print("Digite uma mensagem: ")
        message = input()
        client.send(message.encode())
