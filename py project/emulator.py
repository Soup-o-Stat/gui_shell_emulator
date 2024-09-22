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

start_dir='.'
username=getpass.getuser()
arch_dir='./arch_dir.tar'

def read_ini_file(filename):
    global start_dir, username, arch_dir
    config = configparser.ConfigParser()
    config.read(filename)
    for section in config.sections():
        print(f"[{section}]")
        for key, value in config.items(section):
            if key=="start_dir":
                start_dir=value
            if key=="username":
                username=value
            if key=="arch_dir":
                arch_dir=value
        print()
try:
    ini_file_path = 'config.ini'
    read_ini_file(ini_file_path)
except:
    print("Error with loading ini file!")

files_list=[]
path_list=[]

#отвечает за выход из программы
def exit_programm():
    pygame.quit()
    sys.exit()

#печатает в консоль гуи вот эти строки
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

#тут все интуитивно понятно, разбирать нет смысла
def print_about():
    console.text_list.append("This Shell Emulator has been created by Soup-o-Stat")
    console.text_list.append(f"Version: {main.ver}")

#я научил прогу запускать игры из вк плэй хддд
def open_game():
    console.text_list.append("open 0.2017046")
    webbrowser.open("vkplay://play/0.2017046")

#просто отчистка консоли
def clear():
    console.text_list.clear()

#сортировка говна в файле
def uniq(data):
    data_sorted=False
    for i in range(len(data)):
        if data[i]==" ":
            data=data[i+1:]
            break
    arguments = data.split()
    if len(arguments)!=3:
        console.text_list.append("Error! Invalid number of parameters.")
        return
    param1 = arguments[0]
    param2 = arguments[1]
    param3 = arguments[2]
    if not os.path.exists(param2):
        console.text_list.append(f"Error! File {param2} is not exist")
        return
    if param1=="-u":
        print("-u")
        with open(param2, encoding='utf-8') as fin:
            lines = [line.strip() for line in fin]
        line_counts = Counter(lines)
        with open(param3, 'w', encoding='utf-8') as papers_please:
            for line in lines:
                if line_counts[line] == 1:
                    papers_please.write(line + '\n')
                    data_sorted = True
    elif param1=="-d":
        with open(param2, encoding='utf-8') as fin, open(param3, 'w', encoding='utf-8') as papers_please:
            seen = set()
            for line in fin:
                if line.strip() not in seen:
                    seen.add(line.strip())
                    papers_please.write(line)
                    data_sorted=True
    else:
        console.text_list.append(f"Error! {param1} is not exist")
    if data_sorted==True:
        os.startfile(param3)
        console.text_list.append(f"Done! Trying to open {param3}")

def list_of_bullshit_in_the_fucking_dir_blyat(start_path, indent=''):
    items = os.listdir(start_path)
    for item in items:
        path = os.path.join(start_path, item)
        if os.path.isfile(path):
            console.text_list.append(f"{indent}-> {item}")
        elif os.path.isdir(path):
            console.text_list.append(f"{indent}-> {item}")
            list_of_bullshit_in_the_fucking_dir_blyat(path, indent + '    ')

#переход на другую директорию
def cd(data):
    global start_dir
    for i in range(len(data)):
        if data[i] == " ":
            data = data[i + 1:]
            break
    try:
        items = os.listdir(data)
    except:
        console.text_list.append(f"Error! Dir {data} is not exist")
        return
    start_dir=data

#дерево файлов
def tree(data):
    option_found=False
    for i in range(len(data)):
        if data[i]==" ":
            data=data[i+1:]
            option_found=True
            break
    if option_found==False:
        console.text_list.append("Error! No options")
        return
    option=data
    if option=="-d":
        files_list.clear()
        items = os.listdir(start_dir)
        for item in items:
            path = os.path.join(start_dir, item)
            if os.path.isdir(path):
                files_list.append(path)
        for i in range(len(files_list)):
            console.text_list.append(f"-> {files_list[i]}")
    elif option=="-a":
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
    elif option=="-f":
        files_list.clear()
        list_of_bullshit_in_the_fucking_dir_blyat(start_dir)

#вывод всех файлов и директорий в данной директории
def ls(data, find_bool):
    global start_dir
    if find_bool==True:
        for i in range(len(data)):
            if data[i]==" ":
                data=data[i+1:]
                break
    files_list.clear()
    try:
        items = os.listdir(data)
    except:
        console.text_list.append(f"Error! Dir {data} is not exist")
        return
    for item in items:
        path = os.path.join(data, item)
        if os.path.isfile(path):
            files_list.append(path)
        elif os.path.isdir(path):
            files_list.append(path)
    for i in range(len(files_list)):
        console.text_list.append(files_list[i])

#по сути это except
def error_command(command):
    console.text_list.append(f"Command {command} is not exist. Type 'help' for command list")

#стартовое сообщение
def hello_message():
    console.text_list.append("==========================================================")
    console.text_list.append(f"Hello {username}! Type help for command list!")
    console.text_list.append("==========================================================")
    console.text_list.append("")

#тесты
def start_test():
    clear()
    console.text_list.append("Lets start tests")
    Emulator.read_command(Emulator, "help")
    Emulator.read_command(Emulator,"help ")
    Emulator.read_command(Emulator,"help 12312")

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
    #пустой инит
    def __init__(self):
        pass

    #функция для чтения команд
    def read_command(self, command):
        if command=="help":
            print_help()
        elif command=="about":
            print_about()
        elif command=="open_game":
            open_game()
        elif command=="clear":
            clear()
        elif command=="exit":
            exit_programm()
        elif command=="ls":
            ls(data=start_dir, find_bool=False)
        elif command[:3]=="ls ":
            ls(data=command, find_bool=True)
        elif command=="cd":
            cd(data='.')
        elif command[:3]=="cd ":
            cd(data=command)
        elif command[:5]=="uniq ":
            uniq(data=command)
        elif command=="uniq":
            console.text_list.append("Error! Invalid number of parameters")
        elif command[:5]=="tree ":
            tree(data=command)
        elif command[:5]=="tree":
            console.text_list.append("Error! No options")
        elif command=="start_test":
            start_test()
        else:
            error_command(command=command)
        input_box.input_history.append(command)
        input_box.history_step=0

hello_message()