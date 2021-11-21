import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
server.bind((host, port))
server.listen(5)
client, address = server.accept()
print("Connected successfully")
receiver = server.recv(1024)
receiver = message.decode("utf-8")
print(reciever)
