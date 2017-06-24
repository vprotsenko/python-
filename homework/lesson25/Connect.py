import socket
server = socket.socket()
server.bind(('localhost', 8000))
server.listen(5)
client = server.accept()

client[0].send('sdfsdfsdfdsf'.encode('cp1251'))

while True:
    message = client[0].recv(65000)
    if message:
        print(message)




