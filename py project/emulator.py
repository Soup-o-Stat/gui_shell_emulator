import pygame
import console
import main
import input_box
import os
import sys
import webbrowser
import getpass
import time

files_list=[]

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

#TODO эта поебота не работает, исправить это говно
#сортировка говна в файле
def uniq(data):
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
    if not os.path.exists(param3):
        param3="output.txt"
    if param1=="-u":
        print("-u")
        with open(param2, 'r') as fin, open(param3, 'w') as papers_please:
            unique_lines = set()
            for line in fin:         #'charmap' codec can't decode byte 0x8d in position 8: character maps to <undefined>   пизда какая-то
                if line.strip():
                    if line not in unique_lines:
                        unique_lines.add(line.strip())
                        papers_please.write(line)
    elif param1=="-d":
        pass
    elif param1=="-D":
        pass

#вывод всех файлов и директорий в данной директории
def ls():
    files_list.clear()
    items = os.listdir('.')
    for item in items:
        path = os.path.join('.', item)
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
    console.text_list.append(f"Hello {getpass.getuser()}! Type help for command list!")
    console.text_list.append("==========================================================")
    console.text_list.append("")

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
            ls()
        elif command[:4]=="uniq":
            uniq(data=command)
        else:
            error_command(command=command)
        input_box.input_history.append(command)
        input_box.history_step=0

hello_message()