#Импорт всякой фигни
import time
import pygame
import console
import main
import input_box
import os
import sys
import webbrowser
import getpass
import subprocess
from collections import Counter
import configparser
import zipfile
import configparser

#если это понадобиться, значит либо где-то потерялся ini файл, либо настал конец света
start_dir = '.'
username = getpass.getuser()
arch_dir = './arch_dir.tar'

#если нету флагов
try:
    script, one, two, three, four=sys.argv
    print("Этот скрипт называется: ", script)
    print(one)
    print(two)
    print(three)
    print(four)
except:
    pass

#чтение ини файла
def read_ini_file(filename):
    global start_dir, username, arch_dir
    config = configparser.ConfigParser()
    config.read(filename)
    for section in config.sections():
        print(f"[{section}]")
        for key, value in config.items(section):
            if key == "start_dir":
                start_dir = value
            if key == "username":
                username = value
            if key == "arch_dir":
                arch_dir = value
        print()

#попытка загрузить данные из ини
try:
    ini_file_path = 'config.ini'
    read_ini_file(ini_file_path)
except:
    print("Error with loading ini file!")

files_list = []
path_list = []

#эт для выхода
def exit_programm():
    pygame.quit()
    sys.exit()

#я не умею писать help)))
def print_help():
    console.text_list.append("List of commands:")
    console.text_list.append(" * help: list of commands")
    console.text_list.append(" * clear: clear console")
    console.text_list.append(" * about: about this program")
    console.text_list.append(" * exit: exit")
    console.text_list.append(" * ls: print all files and dirs in this directory")
    console.text_list.append(" * uniq: something with files idk))")
    console.text_list.append(" * tree: file tree")
    console.text_list.append(" * cd: change directory")

#о программе
def print_about():
    console.text_list.append("This Shell Emulator has been created by Soup-o-Stat")
    console.text_list.append(f"Version: {main.ver}")

#хз, зачем я это добавил, но пусть будет
def open_game():
    console.text_list.append("open 0.2017046")
    webbrowser.open("vkplay://play/0.2017046")

#отчиска консоли
def clear():
    console.text_list.clear()

#работа с дубликатами строк в тхт файле
def uniq(data):
    data_sorted = False
    for i in range(len(data)):
        if data[i] == " ":
            data = data[i + 1:]
            break
    arguments = data.split()
    if len(arguments) != 3:
        console.text_list.append("Error! Invalid number of parameters.")
        return
    param1 = arguments[0]
    param2 = arguments[1]
    param3 = arguments[2]

    # Если файл находится в zip архиве
    if start_dir.endswith('.zip'):
        with zipfile.ZipFile(start_dir, 'r') as z:
            if param2 in z.namelist():
                with z.open(param2) as fin:
                    lines = [line.decode('utf-8').strip() for line in fin]
                line_counts = Counter(lines)
                with open(param3, 'w', encoding='utf-8') as papers_please:
                    for line in lines:
                        if param1 == "-u" and line_counts[line] == 1:
                            papers_please.write(line + '\n')
                        elif param1 == "-d" and line_counts[line] > 1:
                            papers_please.write(line + '\n')
                data_sorted = True
            else:
                console.text_list.append(f"Error! File {param2} does not exist in archive.")
                return
    else:
        if not os.path.exists(param2):
            console.text_list.append(f"Error! File {param2} does not exist")
            return
        if param1 == "-u":
            with open(param2, encoding='utf-8') as fin:
                lines = [line.strip() for line in fin]
            line_counts = Counter(lines)
            with open(param3, 'w', encoding='utf-8') as papers_please:
                for line in lines:
                    if line_counts[line] == 1:
                        papers_please.write(line + '\n')
            data_sorted = True
        elif param1 == "-d":
            with open(param2, encoding='utf-8') as fin, open(param3, 'w', encoding='utf-8') as papers_please:
                seen = set()
                for line in fin:
                    if line.strip() not in seen:
                        seen.add(line.strip())
                        papers_please.write(line)
            data_sorted = True
        else:
            console.text_list.append(f"Error! {param1} is not a valid option")

    if data_sorted:
        os.startfile(param3)
        console.text_list.append(f"Done! Trying to open {param3}")

#для работы с зип файлами
def list_files_in_directory(start_path, indent='', zip_file=None):
    if zip_file:
        with zipfile.ZipFile(zip_file, 'r') as z:
            for item in z.namelist():
                console.text_list.append(f"{indent}-> {item}")
    else:
        items = os.listdir(start_path)
        for item in items:
            path = os.path.join(start_path, item)
            if os.path.isfile(path):
                console.text_list.append(f"{indent}-> {item}")
            elif os.path.isdir(path):
                console.text_list.append(f"{indent}-> {item}")
                list_files_in_directory(path, indent + '    ')

#переход на другую директорию
def cd(data):
    global start_dir
    for i in range(len(data)):
        if data[i] == " ":
            data = data[i + 1:]
            break
    try:
        if data.endswith('.zip'):
            start_dir = data
            console.text_list.append(f"Changed to ZIP file: {start_dir}")
            list_files_in_directory(start_dir)
        else:
            items = os.listdir(data)
            start_dir = data
    except FileNotFoundError:
        console.text_list.append(f"Error! Dir {data} does not exist")
    except NotADirectoryError:
        pass

#иерархия файлов
def tree(data):
    option_found = False
    for i in range(len(data)):
        if data[i] == " ":
            data = data[i + 1:]
            option_found = True
            break
    if not option_found:
        console.text_list.append("Error! No options")
        return

    option = data
    if start_dir.endswith('.zip'):
        with zipfile.ZipFile(start_dir, 'r') as z:
            items = z.namelist()
            if option == "-d":
                dirs = [item for item in items if item.endswith('/')]
                for dir in dirs:
                    console.text_list.append(f"-> {dir}")
            elif option == "-a":
                for item in items:
                    console.text_list.append(f"-> {item}")
            elif option == "-f":
                for item in items:
                    console.text_list.append(f"-> {item}")
    else:
        if option == "-d":
            files_list.clear()
            items = os.listdir(start_dir)
            for item in items:
                path = os.path.join(start_dir, item)
                if os.path.isdir(path):
                    files_list.append(path)
            for i in range(len(files_list)):
                console.text_list.append(f"-> {files_list[i]}")
        elif option == "-a":
            files_list.clear()
            items = os.listdir(start_dir)
            for item in items:
                path = os.path.join(start_dir, item)
                if os.path.isfile(path):
                    files_list.append(path)
                elif os.path.isdir(path):
                    files_list.append(path)
            for i in range(len(files_list)):
                console.text_list.append(f"-> {files_list[i]}")
        elif option == "-f":
            files_list.clear()
            list_files_in_directory(start_dir)

#вывод файлов в данной директории
def ls(data, find_bool):
    global start_dir
    if find_bool:
        for i in range(len(data)):
            if data[i] == " ":
                data = data[i + 1:]
                break
    files_list.clear()
    if data.endswith('.zip'):
        list_files_in_directory(start_path=data, zip_file=data)
    else:
        try:
            items = os.listdir(data)
        except FileNotFoundError:
            console.text_list.append(f"Error! Dir {data} does not exist")
            return
        for item in items:
            path = os.path.join(data, item)
            if os.path.isfile(path):
                files_list.append(path)
            elif os.path.isdir(path):
                files_list.append(path)
        for i in range(len(files_list)):
            console.text_list.append(files_list[i])

#типо эксепт
def error_command(command):
    console.text_list.append(f"Command {command} does not exist. Type 'help' for command list")

#приветственное сообщение
def hello_message():
    console.text_list.append("==========================================================")
    console.text_list.append(f"Hello {username}! Type help for command list!")
    console.text_list.append("==========================================================")
    console.text_list.append("")

#тесты
def start_test():
    clear()
    console.text_list.append("Let's start tests")
    Emulator.read_command(Emulator, "help")
    Emulator.read_command(Emulator, "help ")
    Emulator.read_command(Emulator, "help 12312")

    Emulator.read_command(Emulator, "about")
    Emulator.read_command(Emulator, "about ")
    Emulator.read_command(Emulator, "about 12312")

    Emulator.read_command(Emulator, "ls")
    Emulator.read_command(Emulator, "ls ")
    Emulator.read_command(Emulator, "ls /")

    Emulator.read_command(Emulator, "cd")
    Emulator.read_command(Emulator, "ls")
    Emulator.read_command(Emulator, "cd /")
    Emulator.read_command(Emulator, "ls")
    Emulator.read_command(Emulator, "cd /herobotina228")
    Emulator.read_command(Emulator, "ls .")
    Emulator.read_command(Emulator, "cd")

    Emulator.read_command(Emulator, "uniq")
    Emulator.read_command(Emulator, "uniq -u name.txt govno2.txt")
    Emulator.read_command(Emulator, "uniq -d name.txt govno2.txt")
    Emulator.read_command(Emulator, "uniq chavo.txt")

    Emulator.read_command(Emulator, "tree")
    Emulator.read_command(Emulator, "tree -a")
    Emulator.read_command(Emulator, "tree -d")
    Emulator.read_command(Emulator, "tree -f")

#класс эмулятора
class Emulator():
    def __init__(self):
        pass

    def read_command(self, command):
        if command == "help":
            print_help()
        elif command == "about":
            print_about()
        elif command == "open_game":
            open_game()
        elif command == "clear":
            clear()
        elif command == "exit":
            exit_programm()
        elif command == "ls":
            ls(data=start_dir, find_bool=False)
        elif command[:3] == "ls ":
            ls(data=command, find_bool=True)
        elif command == "cd":
            cd(data=start_dir)
        elif command[:3] == "cd ":
            cd(data=command)
        elif command[:5] == "uniq ":
            uniq(data=command)
        elif command == "uniq":
            console.text_list.append("Error! Invalid number of parameters")
        elif command[:5] == "tree ":
            tree(data=command)
        elif command[:5] == "tree":
            console.text_list.append("Error! No options")
        elif command == "start_test":
            start_test()
        else:
            error_command(command=command)
        input_box.input_history.append(command)
        input_box.history_step = 0

#подгрузка флажков
try:
    if one=="ls":
        ls(data=start_dir, find_bool=False)
    if two=="cd":
        cd(data=start_dir)
    if three=="tree":
        tree(data="tree -a")
    if four=="uniq":
        uniq(data="uniq -u common.txt uncommon.txt")
except:
    console.text_list.append("Error with reading flags!")

hello_message()