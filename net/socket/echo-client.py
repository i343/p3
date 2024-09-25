"""
стр.41 Программирование сокетов
При­мер 12.2. PP4E\Internet\Sockets\echo-client.py
На стороне клиента: использует сокеты для передачи данных серверу
и выводит ответ сервера на каждую строку сообщения; 'localhost' означает,
что сервер выполняется на одном компьютере с клиентом, что позволяет
тестировать клиента и сервер на одном компьютере; для тестирования
через Интернет запустите сервер на удаленном компьютере и установите
serverHost или argv[1] равными доменному имени компьютера или его IP-адресу;
сокеты Python являются переносимым интерфейсом к сокетам BSD,
с методами объектов для стандартных функций сокетов, доступных
в системной библиотеке C;
"""

import sys
from socket import *     # переносимый интерфейс сокетов плюс константы
serverHost = 'localhost' # имя сервера, например: 'starship.python.net'
serverPort = 50505       # незарезервированный порт, используемый сервером
# serverPort = 50007       # незарезервированный порт, используемый сервером
message = [b'Hello network world'] # текст, посылаемый серверу обязательно
# типа bytes: b'' или str.encode()

if len(sys.argv) > 1:
    serverHost = sys.argv[1]    # сервер в аргументе 1 командной строки
    serverPort = int(sys.argv[2])
    if len(sys.argv) > 2: # текст в аргументах командной строки 2..n
        message = (x.encode() for x in sys.argv[2:])

print("serverHost ->", serverHost)
print("serverPort ->", serverPort)
print(" 27 ->", type(message))
print(" 28 ->", message)
sockobj = socket(AF_INET, SOCK_STREAM) # создать объект сокета TCP/IP
sockobj.connect((serverHost, serverPort)) # соединение с сервером и портом

for line in message:
    bline = line
    print('type_bline =>',type(bline))
    print('bline =>',bline)
    sockobj.send(bline)              # послать серверу строчку через сокет
    data = sockobj.recv(1024)       # получить строку от сервера: до 1k
    print('Client received:', data) # строка bytes выводится в кавычках,
                                    # было `x`, repr(x)
sockobj.close() # закрыть сокет, чтобы послать серверу eof