# ANA THAMYRES
# SERVIDOR (aguarda conexão)
import socket
import threading

HOST = '127.0.0.1' # Endereço IP do servidor
PORT = 65432 # Porta que o servidor usará
clients = [] # Lista de clientes conectados

# Função paroa lidar com a conexão de cada cliente
def handle_client(conn, addr):
    conn.send('Bem-vindo ao chat!'.encode())
    print(f'Conexão estabelecida com {addr}')
    
    

    while True:
        try:
            message = conn.recv(1024).decode()
            if message:
                print(f'{addr}: {message}')

                # Envia a mensagem para todos os outros clientes conectados
                for client in clients:
                    if client != conn:
                        client.send(message.encode())

            else:
                # Se não houver mais mensagens, encerra a conexão
                remove(conn)
                conn.close()
                break

        except:
            # Se houver algum erro, encerra a conexão
            remove(conn)
            conn.close()
            break

# Função para remover um cliente da lista
def remove(conn):
    if conn in clients:
        clients.remove(conn)

# Configuração do socket do servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Servidor rodando em {HOST}:{PORT}')

    while True:
        # Aceita novas conexões de clientes
        conn, addr = s.accept()

        # Adiciona o cliente na lista de clientes conectados
        clients.append(conn)

        # Inicia uma thread para lidar com o cliente
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
