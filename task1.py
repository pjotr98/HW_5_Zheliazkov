import os
import pprint as pp


def make_dir():
    i = 1
    os.chdir('/Users/Oles/Desktop/HW_5')
    while i > 0:
        try:
            dirname = input('Input a folder name ')
            os.mkdir(dirname)
            pp.pprint('folder ' + dirname + ' was created')
            pp.pprint('Do you want to create another folder?')
            af = int(input('1 — yes 0 — no '))
            if af == 0:  # af - variable to create another folder
                i = 0
                break
            else:
                i += i
        except FileExistsError:
            pp.pprint('This folder is already exist!')


def create_text_file(filename):
    f = open(filename +'.txt', '+a')
    f.close()


def show_tree_of_folders():
    for root, dirs, files in os.walk("/Users/Oles/Desktop/HW_5"):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))


pp.pprint('Hi ' + os.getlogin() +'!')
make_dir()
create_text_file(input('Input text file name '))
show_tree_of_folders()