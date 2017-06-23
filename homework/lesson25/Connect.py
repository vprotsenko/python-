import socket
server = socket.socket()
server.bind(('localhost', 8000))
server.listen(5)
client = server.accept()

client[0].send('sdfsdfsdfdsf'.encode('cp1251'))