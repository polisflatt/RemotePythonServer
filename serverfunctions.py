import os

def oscommand(text):
    print(os.popen(text).read())

def cd(directory):
    os.chdir(directory)

def ls():
    for filename in os.listdir():
        print(filename)