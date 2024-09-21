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

def exit_programm():
    pygame.quit()
    sys.exit()

def print_help():
    console.text_list.append("List of commands:")
    console.text_list.append(" * help: list of commands")
    console.text_list.append(" * clear: clear console")
    console.text_list.append(" * about: about this program")
    console.text_list.append(" * exit: exit")
    console.text_list.append(" * ls: print all files and dirs in this directory")

def print_about():
    console.text_list.append("This Shell Emulator has been created by Soup-o-Stat")
    console.text_list.append(f"Version: {main.ver}")

def open_game():
    console.text_list.append("open 0.2017046")
    webbrowser.open("vkplay://play/0.2017046")

def clear():
    console.text_list.clear()

def uniq(data):
    for i in range(len(data)):
        if data[i]==" ":
            option1=data[i+1:]
            for j in range(len(option1)-1):
                if option1[i]==" ":
                    option1=option1[i]
            break
    try:
        print(option1)
    except:
        console.text_list.append("Error! Options are empty")

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

def error_command(command):
    console.text_list.append(f"Command {command} is not exist. Type 'help' for command list")

def hello_message():
    console.text_list.append("=======================================================")
    console.text_list.append(f"Hello {getpass.getuser()}! Type help for command list!")
    console.text_list.append("=======================================================")

class Emulator():
    def __init__(self):
        pass

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