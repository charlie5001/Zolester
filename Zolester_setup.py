import os
import shutil
from pip._internal import main as pipmain
file_pathz = os.path.dirname(os.path.realpath(__file__))
pipmain(['install', 'pyfiglet'])
logo = "LOGO = Figlet(font='slant')"
path = input("paste your path here: ")
newpath=str(path)
R='r'
newestpath="import os,sys,shutil\nfrom pyfiglet import Figlet"+'\n'+'sys.path.insert'+'(1, '+'r'+"'"+file_pathz+"'"+")\n"+"path="+"r"+"'"+newpath+"'\n"
with open(file_pathz+'/insert.txt') as f:
    lines = f.readlines()
    f = open(file_pathz+"/ZolesterAuthorEdition.py", "a+")
    f.writelines(newestpath)
    f.writelines(lines)
    f.close()
    print(newpath)
    input("All set up now!\nPress ENTER to exit.")
