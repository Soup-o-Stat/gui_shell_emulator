import pygame
import console
import main
import input_box
import os

files_list=[]

class Emulator():
    def __init__(self):
        pass

    def read_command(self, command):
        if command=="help":
            console.text_list.append("List of commands:")
            console.text_list.append(" * help: list of commands")
            console.text_list.append(" * clear: clear console")
            console.text_list.append(" * about: about this program")
            console.text_list.append(" * exit: exit")
            console.text_list.append(" * ls: print all files and dirs in this directory")
        elif command=="about":
            console.text_list.append("This Shell Emulator has been created by Soup-o-Stat")
            console.text_list.append(f"Version: {main.ver}")
        elif command=="clear":
            console.text_list.clear()
        elif command=="exit":
            exit()
        elif command=="ls":
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
        else:
            console.text_list.append(f"Command {command} is not exist. Type 'help' for command list")
        input_box.input_history.append(command)
        input_box.history_step=0