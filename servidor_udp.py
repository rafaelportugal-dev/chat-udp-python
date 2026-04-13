import socket

HOST = 'localhost'
PORT = 50001

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print("Servidor UDP ativo...")

while True:
    msg, addr = server.recvfrom(1024)
    print("Cliente:", msg.decode())

    resposta = input("Você: ")
    server.sendto(resposta.encode(), addr)
