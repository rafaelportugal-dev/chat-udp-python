import socket

HOST = 'localhost'
PORT = 50001

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Você: ")
    client.sendto(msg.encode(), (HOST, PORT))

    resposta, _ = client.recvfrom(1024)
    print("Servidor:", resposta.decode())
