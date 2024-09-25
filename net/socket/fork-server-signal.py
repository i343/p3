"""
стр.68 Глава 12. Сетевые сценарии
При­мер 12.6. PP4E\Internet\Sockets\fork-server-signal.py
То же, что и fork-server.py, но использует модуль signal, чтобы обеспечить
автоматическое удаление дочерних процессов-зомби после их завершения вместо
явного удаления перед приемом каждого нового соединения; действие SIG_IGN
означает игнорирование и может действовать с сигналом SIGCHLD завершения
дочерних процессов не на всех платформах; смотрите документацию
к операционной системе Linux, где описывается возможность перезапуска
вызова socket.accept, прерванного сигналом;
"""


import os, time, sys, signal, signal
from socket import * # получить конструктор сокета и константы
myHost = ''
# компьютер сервера, '' означает локальный хост
myPort = 50007
# использовать незарезервированный номер порта
sockobj = socket(AF_INET, SOCK_STREAM) # создать объект сокета TCP
sockobj.bind((myHost, myPort))
# связать с номером порта сервера
sockobj.listen(5)
# не более 5 ожидающих запросов
signal.signal(signal.SIGCHLD, signal.SIG_IGN) # автоматически удалять
# дочерние процессы-зомби

def now():
# текущее время на сервере
    return time.ctime(time.time())

def handleClient(connection):
    time.sleep(5)
    while True:
        # дочерний процесс: ответить, выйти
        # имитировать блокирующие действия
        # чтение, запись в сокет клиента
        data = connection.recv(1024)
        if not data: break
        reply = 'Echo=>%s at %s' % (data, now())
        connection.send(reply.encode())
    connection.close()
    os._exit(0)

def dispatcher():
    # пока процесс работает
    while True:
    # ждать запроса очередного клиента,
        connection, address = sockobj.accept()
        # передать процессу
        print('Server connected by', address, end=' ') # для обслуживания
        print('at', now())
        childPid = os.fork()
        # копировать этот процесс
        if childPid == 0:
        # в дочернем процессе: обслужить
            handleClient(connection) # иначе: ждать следующего запроса


dispatcher()