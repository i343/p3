"""
При­мер 12.9. PP4E\Internet\Sockets\select-server.py
Сервер: обслуживает параллельно несколько клиентов с помощью select.
Использует модуль select для мультиплексирования в группе сокетов:
главных сокетов, принимающих от клиентов новые запросы на соединение,
и входных сокетов, связанных с клиентами, запрос на соединение от которых
был удовлетворен; вызов select может принимать необязательный 4-й аргумент –
0 означает "опрашивать", число n.m означает "ждать n.m секунд", отсутствие
аргумента означает "ждать готовности к обработке любого сокета".
"""



import sys, time
from select import select
from socket import socket, AF_INET, SOCK_STREAM

def now(): 
    time0 = time.time()
    time1 = time.ctime(time0)
    print("time ->",time0)
    print("time ->",time1)
    return time1

myHost = '192.168.0.1'
# компьютер-сервер, '' означает локальный хост
myPort0 = 50505
# использовать незарезервированный номер порта
lenSysArgv = len(sys.argv)

if lenSysArgv == 3: # хост/порт можно указать в командной строке
    myHost, myPort0 = sys.argv[1:]
myPort = int(myPort0)
print("len ->",lenSysArgv)
print('argv -> ',sys.argv[1:])
print('my -->>', myHost, myPort)
print('my type ->>', type(myHost), type(myPort))

numPortSocks = 2
# количество портов для подключения клиентов
# создать главные сокеты для приема новых запросов на соединение от клиентов

mainsocks, readsocks, writesocks = [], [], []

for i in range(numPortSocks):
    print('my2 -->>', i, myHost, myPort)
    portsock = socket(AF_INET, SOCK_STREAM) # создать объект сокета TCP
    portsock.bind((myHost, int(myPort))) # связать с номером порта сервера
    portsock.listen(5)
    # не более 5 ожидающих запросов
    mainsocks.append(portsock)
    # добавить в главный список
    # для идентификации
    readsocks.append(portsock)
    # добавить в список источников select
    myPort += 1
    # привязка выполняется к смежным портам
    # цикл событий: слушать и мультиплексировать, пока процесс не завершится
print('select-server loop starting')

print('readsocks +->',readsocks)
for iReadSocks in readsocks:
    print(iReadSocks)
print('\n')

print('mainsocks +->',mainsocks)
for imainsocks in mainsocks:
    print(imainsocks)
print('\n')


while True:
    readables, writeables, exceptions = select(readsocks, writesocks, [])
    for sockobj in readables:
        if sockobj in mainsocks:
            # для готовых входных сокетов
            # сокет порта: принять соединение от нового клиента
            newsock, address = sockobj.accept() # accept не должен
            # блокировать
            print('Connect:', address, id(newsock)) # newsock – новый сокет
            readsocks.append(newsock)
            # добавить в список select, ждать
        else:
            # сокет клиента: читать следующую строку
            data = sockobj.recv(1024)
            # recv не должен блокировать
            print('\tgot', data, 'on', id(sockobj))
            if not data:
                # если закрыто клиентом
                sockobj.close()
                # закрыть и удалить из списка
                readsocks.remove(sockobj)
                # иначе повторно будет
            else:
                # обслуживаться вызовом select
                # может блокировать: в действительности для операции записи
                # тоже следовало бы использовать вызов select
                reply = 'Echo=>%s at %s' % (data, now())
                sockobj.send(reply.encode())