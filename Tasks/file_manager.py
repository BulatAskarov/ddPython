import os


def pwd():
    print(os.getcwd())


def cd(path):
    try:
        os.chdir(path)
        print(os.getcwd())
    except FileNotFoundError:
        print("No such directory")


def touch(filename):
    file = open(filename, "w")
    file.write("")
    file.close()


def cat(filename):
    try:
        file = open(filename, "r")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("No such file")


def ls():
    print(os.listdir(os.getcwd()))


def rm(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        print("No such file")


while (True):
    print(os.getcwd())
    command = input(" : ")
    if "pwd" in command:
        pwd()
    if "cd" in command:
        lst = command.strip(" ")
        cd(command[1])
    if "touch" in command:
        lst = command.strip(" ")
        touch(command[1])
    if "cat" in command:
        lst = command.strip(" ")
        cat(command[1])
    if "ls" in command:
        ls()
    if "rm" in command:
        lst = command.strip(" ")
        rm(command[1])