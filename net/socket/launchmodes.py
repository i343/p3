"""
запускает программы Python с помощью механизмов командной строки и классов
схем запуска; автоматически вставляет “python” и/или путь к выполняемому файлу
интерпретатора в начало командной строки; некоторые из инструментов в этом
модуле предполагают, что выполняемый файл 'python’ находится в системном пути
поиска (смотрите Launcher.py);
можно было бы использовать модуль subprocess, но он сам использует функцию
os.popen(), и к тому же цель этого модуля состоит в том, чтобы запустить
независимую программу, а не подключиться к ее потокам ввода-вывода;
можно было бы также использовать пакет multiprocessing, но данный модуль
предназначен для выполнения программ, а не функций: не имеет смысла запускать
процесс, когда можно использовать одну из уже имеющихся возможностей;
новое в этом издании: при запуске сценария передает путь к файлу сценария
через функцию normpath(), которая в Windows замещает все / на \; исправьте
соответствующие участки программного кода в PyEdit и в других сценариях;
вообще в Windows допускается использовать / в командах открытия файлов, но этот
символ может использоваться не во всех инструментах запуска программ;
"""

import sys, os
pyfile = (sys.platform[:3] == 'python.exe') or 'python'
pypath = sys.executable # использовать sys в последних версиях Python

def fixWindowsPath(cmdline):
    """
    замещает все / на \ в путях к сценариям в начале команд;
    используется только классами, которые запускают инструменты, требующие
    этого в Windows; в других системах в этом нет необходимости (например,
    os.system в Unix);
    
    """
    splitline = cmdline.lstrip().split(' ') # разбить по пробелам
    fixedpath = os.path.normpath(splitline[0]) # заменить прямые слешы
    return ' '.join([fixedpath] + splitline[1:]) # снова объединить в строку

class LaunchMode:
    """
    при вызове экземпляра класса выводится метка и запускается команда;
    подклассы форматируют строки команд для метода run(), если необходимо;
    команда должна начинаться с имени запускаемого файла сценария Python
    и не должна начинаться со слова “python” или с полного пути к нему;
    """

    def __init__(self, label, command):
        self.what = label
        self.where = command
    def __call__(self):
        # вызывается при вызове экземпляра,
        self.announce(self.what) # например как обработчик щелчка на кнопке
        self.run(self.where)
        # подклассы должны определять метод run()
    def announce(self, text):
        # подклассы могут переопределять метод
        print(text)
        # announce() вместо логики if/elif
    def run(self, cmdline):
        assert False, "run must be defined"

class System(LaunchMode):
    """
    запускает сценарий Python, указанный в команде оболочки
    внимание: может блокировать вызывающую программу,
    если в Unix не добавить &
    """
    def run(self, cmdline):
        cmdline = fixWindowsPath(cmdline)
        os.system("%s %s" % (pypath, cmdline))

class Popen(LaunchMode):
    """ 
    запускает команду оболочки в новом процессе
    внимание: может блокировать вызывающую программу, потому что
    канал закрывается немедленно
    """

    def run(self, cmdline):
        cmdline = fixWindowsPath(cmdline)
        os.popen(pypath + ' ' + cmdline)
        # предполагается, что нет данных
        # для чтения

class Fork(LaunchMode):
    """ 
    запускает команду в явно созданном новом процессе
    только для Unix-подобных систем, включая cygwin
    """
    def run(self, cmdline):
        assert hasattr(os, "fork")
        cmdline = cmdline.split()
        # превратить строку в список
        if os.fork() == 0:
        # запустить новый процесс
            os.execvp(pypath, [pyfile] + cmdline) # запустить новую программу 


class Start(LaunchMode):
    """ 
    запускает команду, независимую от вызывающего процесса
    только для Windows: использует ассоциации с расширениями имен файлов
    """

    def run(self, cmdline):
        assert sys.platform[:3] == "win"
        cmdline = fixWindowsPath(cmdline)
        os.startfile(cmdline)

class StartArgs(LaunchMode):
    """ 
    только для Windows: в аргументах могут присутствовать символы прямого
    слеша
    """

    def run(self, cmdline):
        assert sys.platform[:3] == "win"
        os.system('start ' + cmdline) # может создать окно консоли

class Spawn(LaunchMode):
    """ 
    запускает python в новом процессе, независимом от вызывающего,
    для Windows и Unix; используйте P_NOWAIT для окна dos;
    символы прямого слеша допустимы
    """

    def run(self, cmdline):
        os.spawnv(os.P_DETACH, pypath, (pyfile, cmdline))

class Top_level(LaunchMode):
    """ 
    запускает тот же процесс в новом окне
    на будущее: требуется информация о классе графического интерфейса
    """
    def run(self, cmdline):
        assert False, 'Sorry - mode not yet implemented'


#
# выбор “лучшего” средства запуска для данной платформы
# возможно, выбор придется уточнить в других местах
#


if sys.platform[:3] == 'win':
    PortableLauncher = Spawn
else:
    PortableLauncher = Fork

class QuietPortableLauncher(PortableLauncher):
    def announce(self, text):
        pass    
        
def selftest():
    file = 'echo.py'
    input('default mode...')
    launcher = PortableLauncher(file, file)
    launcher()

    input('system mode...')
    System(file, file)()

    if sys.platform[:3] == 'win':
       input('DOS start mode...')
       StartArgs(file, file)()

if __name__ == '__main__': selftest()      