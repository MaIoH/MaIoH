import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
client.connect((host, port))
message = input("Enter your text man? ")
client.send(message.encode("utf-8"))
client.close()
