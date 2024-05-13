from socket import *
serverSocket = socket( AF_INET, SOCK_STREAM)
port = 7919
serverSocket.bind(('',port))
serverSocket.listen(1)

while True:
    connectSocket,addr = serverSocket.accept()
    try:
        message = connectSocket.recv(1024).decode()
        print(message)
        filename = message.split()[1]
        header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
        connectSocket.send(header.encode())
        with open(filename[1:],'r',encoding='utf-8') as file:
            outputdata = file.read()
        for i in range(0,len(outputdata)):
            connectSocket.send(outputdata[i].encode())
    except IOError:
        header = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n'
        connectSocket.send(header.encode())
        with open('404.html','r',encoding='utf-8') as file:
            outputdata = file.read()
        for i in range(0,len(outputdata)):
            connectSocket.send(outputdata[i].encode())
    connectSocket.close()

