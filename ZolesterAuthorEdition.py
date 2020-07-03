import os,sys,shutil
from pyfiglet import Figlet
sys.path.insert(1, r'C:\Users\charl\Desktop\Zolester\Zolester Suite')
source_path = os.path.dirname(os.path.realpath(__file__))
path=r'C:\Users\charl\Desktop\Zolester\Zolester Suite'
LOGO = Figlet(font='slant')
print(LOGO.renderText('ZOLESTER'))
filetoread = open(source_path+"/.zotero-ft-info")
line = filetoread.readline()
while True:
    line = filetoread.readline()
    if "Author:" in line:
        break
line = line.replace("Author:", "")
line = line.replace("\n", "")
line = line.replace("         ", "")
newfolder = path + "/" + line
source_path = os.path.dirname(os.path.realpath(__file__))        
os.chdir(source_path)
shutil.copytree(source_path, newfolder)

print("if any thing went wrong contact your brother or read the README")  
input("Press enter to get out of here!")
os.remove(newfolder+"/ZolesterAuthorEdition.py")