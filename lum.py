import os
import platform
import psutil
import shutil
import GPUtil
from colorama import Fore

ascii_art = r"""
          ___            _                    ___          
         /\    \          /\    \                  /\    \         
        /::\__\        /:::\\                /::\__\        
       /:::/    /       /:::/    /               /::::|   |        
      /:::/    /       /:::/    /               /:::::|   |        
     /:::/    /       /:::/    /               /::::::|   |        
    /:::/    /       /:::/    /               /:::/|::|   |        
   /:::/    /       /:::/    /               /:::/ |::|   |        
  /:::/    /       /:::/    /      ___    /:::/  |::|_|______  
 /:::/    /       /:::/____/      /\    \  /:::/   |::::::::\    \ 
/:::/__/       |:::|    /      /::\\/:::/    |:::::::::\\
\:::\    \       |:::|____\     /:::/    /\::/    / ~~~~~/:::/    /
 \:::\    \       \:::\    \   /:::/    /  \/____/      /:::/    / 
  \:::\    \       \:::\    \ /:::/    /               /:::/    /  
   \:::\    \       \:::\__/:::/    /               /:::/    /   
    \:::\    \       \::::::::/    /               /:::/    /    
     \:::\    \       \::::::/    /               /:::/    /     
      \:::\    \       \::::/    /               /:::/    /      
       \:::\____\       \::::/    /               /:::/    /       
        \::/    /        \::/____/                \::/    /        
         \/__/          ~~                       \/__/          
"""

def init():
    os.system('cls' if os.name == 'nt' else 'clear')

init()

print(Fore.CYAN + ascii_art)

def mkdir(name):
    os.mkdir(name)

def rmdir(name):
    os.rmdir(name)

def cd(name):
    os.chdir(name)

def ls():
    for file in os.listdir():
        print(file)

def touch(name, content):
    with open(name, 'w') as file:
        file.write(content)

def cat(name):
    with open(name, 'r') as file:
        print(file.read())

def rm(name):
    os.remove(name)

def pwd():
    return os.getcwd()

def cp(src, dst):
    shutil.copy(src, dst)
    print(Fore.BLUE + 'Файл или директория скопирована')

def mv(src, dst):
    shutil.move(src, dst)
    print(Fore.BLUE + 'Файл или директория перемещена')

def rename(src, dst):
    os.rename(src, dst)
    print(Fore.BLUE + 'Файл или директория переименована')

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
    print(Fore.BLUE + ascii_art)
    print(Fore.YELLOW + "==========================================================================")

while True:
    command = input(Fore.CYAN + "$ ")

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
    elif command == "exit":
        break
    else:
        print(Fore.RED + "Неизвестная команда")