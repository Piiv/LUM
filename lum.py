import os
import platform
import psutil
import shutil
import GPUtil
from colorama import Fore
import time
import requests
import cowsay
from datetime import datetime


# импорты ↑↑


def get_system_info():
    system = platform.system()
    release = platform.release()

def init():
    os.system('cls' if os.name == 'nt' else 'clear')

init()



# команды ↓↓


def mkdir(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print(Fore.RED + f"Директория '{name}' уже существует.")
    except PermissionError:
        print(Fore.RED + f"Недостаточно прав для создания директории '{name}'.")
    except Exception as e:
        print(Fore.RED + f"Произошла ошибка при создании директории '{name}': {str(e)}")

def rmdir(name):
    try:
        os.rmdir(name)
    except FileNotFoundError:
        print(Fore.RED + f"Директория '{name}' не найдена.")
    except PermissionError:
        print(Fore.RED + f"Недостаточно прав для удаления директории '{name}'.")
    except NotADirectoryError:
        print(Fore.RED + f"Объект '{name}' не является директорией.")
    except Exception as e:
        print(Fore.RED + f"Произошла ошибка при удалении директории '{name}': {str(e)}")

def cd(name):
    try:
        os.chdir(name)
    except FileNotFoundError:
        print(Fore.RED + f"Директория '{name}' не найдена.")
    except PermissionError:
        print(Fore.RED + f"Недостаточно прав для перехода в директорию '{name}'.")
    except Exception as e:
        print(Fore.RED + f"Произошла ошибка при переходе в директорию '{name}': {str(e)}")

def ls():
    try:
        for file in os.listdir():
            print(file)
    except Exception as e:
        print(Fore.RED + f"Произошла ошибка при получении списка файлов: {str(e)}")

def touch(name, content):
    try:
        with open(name, 'w') as file:
            file.write(content)
    except PermissionError:
        print(Fore.RED + f"Недостаточно прав для создания файла '{name}'.")
    except Exception as e:
        print(Fore.RED + f"Произошла ошибка при создании файла '{name}': {str(e)}")

def cat(name):
    try:
        with open(name, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(Fore.RED + f"Файл '{name}' не найден.")
    except PermissionError:
        print(Fore.RED + f"Недостаточно прав для чтения файла '{name}'.")
    except Exception as e:
        print(Fore.RED + f"Произошла ошибка при чтении файла '{name}': {str(e)}")

def rm(name):
    try:
        os.remove(name)
    except FileNotFoundError:
        print(Fore.RED + f"Файл '{name}' не найден.")
    except PermissionError:
        print(Fore.RED + f"Недостаточно прав для удаления файла '{name}'.")
    except Exception as e:
        print(Fore.RED + f"Произошла ошибка при удалении файла '{name}': {str(e)}")

def cp(src, dst):
    try:
        shutil.copy(src, dst)
        print(Fore.BLUE + 'Файл или директория скопирована')
    except FileNotFoundError:
        print(Fore.RED + f"Файл или директория '{src}' не найдены.")
    except PermissionError:
        print(Fore.RED + f"Недостаточно прав для копирования файла или директории '{src}'.")
    except Exception as e:
        print(Fore.RED + f"Произошла ошибка при копировании файла или директории '{src}': {str(e)}")

def pwd():
    try:
        return os.getcwd()
    except Exception as e:
        print(Fore.RED + f"Произошла ошибка при получении текущей директории: {str(e)}")
def mv(src, dst):
    try:
        shutil.move(src, dst)
        print(Fore.BLUE + 'Файл или директория перемещена')
    except FileNotFoundError:
        print(Fore.RED + f"Файл или директория '{src}' не найдены.")
    except PermissionError:
        print(Fore.RED + f"Недостаточно прав для перемещения файла или директории '{src}'.")
    except Exception as e:
        print(Fore.RED + f"Произошла ошибка при перемещении файла или директории '{src}': {str(e)}")

def rename(src, dst):
    try:
        os.rename(src, dst)
        print(Fore.BLUE + 'Файл или директория переименована')
    except FileNotFoundError:
        print(Fore.RED + f"Файл или директория '{src}' не найдены.")
    except PermissionError:
        print(Fore.RED + f"Недостаточно прав для переименования файла или директории '{src}'.")
    except Exception as e:
        print(Fore.RED + f"Произошла ошибка при переименовании файла или директории '{src}': {str(e)}")

def df():
    try:
        total, used, free = shutil.disk_usage('/')
        print(f"Общий объем диска: {total / 2**30:.2f} GB")
        print(f"Используемый объем диска: {used / 2**30:.2f} GB")
        print(f"Свободный объем диска: {free / 2**30:.2f} GB")
    except Exception as e:
        print(Fore.RED + f"Произошла ошибка при получении информации о диске: {str(e)}")
    
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def request(adress):
    try:
        request_fr_user = requests.get(adress)
        print(Fore.GREEN + f"HTTP-статус код: {request_fr_user.status_code}")
        print(Fore.YELLOW + f"Ответа: {request_fr_user.text}")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Ошибка запроса: {str(e)}")

def cowsaying(text):
    cowsay.draw(text)

def time():
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"{Fore.MAGENTA}Текущее время: {current_time}")


def help():
    print('')
    print(Fore.CYAN + 'Список доступных команд:')
    print(Fore.MAGENTA +'mkdir - создать директорию')
    print(Fore.MAGENTA +'rmdir - удалить директорию')
    print(Fore.MAGENTA + 'cd - перейти в директорию')
    print(Fore.MAGENTA + 'ls - показать содержимое текущей директории')
    print(Fore.MAGENTA + 'touch - создать новый файл')
    print(Fore.MAGENTA + 'cat - вывести содержимое файла')
    print(Fore.MAGENTA + 'rm - удалить файл')
    print(Fore.MAGENTA + 'pwd - показать текущую директорию')
    print(Fore.MAGENTA + 'help - вывести справку')
    print(Fore.MAGENTA + 'cp - скопировать файл или директорию')
    print(Fore.MAGENTA + 'mv - переместить файл или директорию')
    print(Fore.MAGENTA + 'rename - переименовать файл или директорию')
    print(Fore.MAGENTA + 'neofetch - получить информацию о системе')
    print(Fore.MAGENTA + 'df - получить информацию о дисковом пространстве')
    print(Fore.MAGENTA + 'clear - очистить консоль')
    print(Fore.MAGENTA +'request <адрес> - выполнить GET-запрос к указанному адресу')
    print(Fore.MAGENTA +'cowsay - корова скажет')
    print(Fore.MAGENTA + 'time - показать текущее время')
    print(Fore.MAGENTA + 'cmd - открыть командную строку')
    print(Fore.MAGENTA + 'exit - выйти')


def neofetch():
    cpu = platform.processor()
    cores = psutil.cpu_count(logical=True)
    ram = round(psutil.virtual_memory().total / (1024 ** 3), 2)
    os_info = platform.system() + " " + platform.release()
    gpu_info = "Неизвестный GPU"

    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu_info = gpus[0].name
    except ImportError:
        gpu_info = "Не удалось импортировать GPUtil"

    print(Fore.YELLOW + "=== System Information ===================================================")
    print(Fore.BLUE + f"Python: {platform.python_version()}") 
    print(Fore.YELLOW + '==========================================================================')
    print(Fore.BLUE + f"Architecture: {platform.machine()}")
    print(Fore.BLUE + f"CPU: {cpu} ({cores} cores)")
    print(Fore.BLUE + f"GPU: {gpu_info}")
    print(Fore.YELLOW + '==========================================================================')
    print(Fore.BLUE + f"System: {platform.system()}")
    print(Fore.BLUE + f"OS: {os_info}")
    print(Fore.BLUE + f"Username: {os.getlogin()}")
    print(Fore.YELLOW + '==========================================================================')
    print(Fore.BLUE + f"RAM: {ram} GB")
    print(Fore.YELLOW + "==========================================================================")





# основной цикл ↓↓


while True:
    command = input(Fore.CYAN + "~")
    

    if command == "mkdir":
        name = input("Введите имя директории: ")
        mkdir(name)
    elif command == "rmdir":
        name = input("Введите имя директории для удаления: ")
        rmdir(name)
    elif command == "cd":
        name = input("Введите имя директории: ")
        cd(name)
    elif command == "ls":
        ls()
    elif command == "touch":
        name = input("Введите имя файла: ")
        content = input("Введите содержимое файла: ")
        touch(name, content)
    elif command == "cat":
        name = input("Введите имя файла: ")
        cat(name)
    elif command == "rm":
        name = input("Введите имя файла: ")
        rm(name)
    elif command == "pwd":
        print(pwd())
    elif command == "cp":
        src = input("Введите имя источника: ")
        dst = input("Введите имя назначения: ")
        cp(src, dst)
    elif command == "mv":
        src = input("Введите имя источника: ")
        dst = input("Введите имя назначения: ")
        mv(src, dst)
    elif command == "rename":
        src = input("Введите текущее имя: ")
        dst = input("Введите новое имя: ")
        rename(src, dst)
    elif command == "help":
        help()
    elif command == "neofetch":
        neofetch()
    elif command == 'df':
        df()
    elif command == 'clear':
        clear()
    elif command == 'request':
        request()
    elif command == ('cowsay'):
        text = input('Введите текст: ')
        cowsay.cow(text)
    elif command == 'time':
        time()
    elif command == 'cmd':
        print(Fore.RED + 'Командная строка открыта Windows ↓↓↓')
        print(Fore.RESET + '')
        os.system('cmd.exe')
    elif command == "exit":
        break
    else:
        print(Fore.RED + "Неизвестная команда")