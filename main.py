#!usr/bin/env python3
import sys
import subprocess
import datetime


class SerchCommand(object):
    a = sys.argv[0]
    #dpath = (current directory)/serch_command/
    dpath = a[0:-7]

    def __init__(self):    
        self.cmd = None         

    def get_command(self):
        self.cmd = input('Enter a command : ')
        return self.cmd

    def make_file_path(self, *args):
        #make a path to open a template file
        #args contain inputs that user entered
        file_path = self.a[0:-7] + 'lib/' + args[0] + '.txt'
        return file_path

    
class History(SerchCommand):
    def format(self, *args):
        self.now = datetime.datetime.now()
        self.now =  self.now.strftime('%Y/%m/%d-%H/%M/%S')
        self.draft = str(self.now) + ' : ' + args[0]

    def append_history(self, gc):
        #not to append an input to the history if it was a subcomannd
        for i in SUBCOMMANDS:
            if i == gc:
                return

        path = self.dpath + 'history.txt'    
        with open(path, 'a') as f:
            f.write(self.draft)    
            f.write('\n')
    
    def open_history(self):
        a = self.a[0:-7] + 'history.txt'
        with open(a, 'r') as f:
            print(f.read())


def is_subcommand(arg):
    for i in SUBCOMMANDS:
        if i == arg:
            return True

def subcommand(sub):
    if sub == 'HISTORY':
        SH.open_history()
    # TODO convert txt to json
    elif sub == 'HELP':
        a = sys.argv[0]
        path = a[0:-7] + 'lib/all_commands.txt'
        with open (path, 'r') as f:
            print(f.read())

def do_continue():
        a = input('Search again ? Y/n : ')
        return a
    

SC = SerchCommand()
SH = History()
SUBCOMMANDS = ['HISTORY', 'HELP']

while True:
    gc = SC.get_command()
    path = SC.make_file_path(gc)

    #write a command to the history file
    SH.format(gc)
    SH.append_history(gc)

    is_sub = is_subcommand(gc)
    if is_sub == True:
        subcommand(gc)
    else:
        try:
            with open(path, 'r') as f:
                print(f.read())
        except FileNotFoundError as ex:
            print("The command '" + gc + "' does not exist in the list.")    

    doContinue = do_continue()
    if doContinue == 'n':
        break


# TODO docstringを記載する
# TODO 実際にコマンドを実行するオプション -e
# TODO 表示できるコマンドをすべて表示するサブコマンド HELP
    # TODO all_commands.txtをjsonファイルに変換してキー値のみ表示
# TODO 名付け