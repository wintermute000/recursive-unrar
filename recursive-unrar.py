from pyunpack import Archive
import sys
import os
import rarfile

if len(sys.argv) != 2:
    # Exit the script
    sys.exit("Usage: ./recursive-unrar.py '<root directory>'")

startpath = sys.argv[1]
rarfile.UNRAR_TOOL = "C:\Python27\Scripts\UnRAR.exe"

def recursive_unrar():
    os.chdir(startpath)
    directories=next(os.walk('.'))[1]
    for x in directories:
        subdir = startpath+"\\"+x
        for r,d,f in os.walk(subdir):
            for file in f:
                if file.endswith('.rar'):
                    os.chdir(subdir)
                    print('Extracting '+file+'...')
                    rf = rarfile.RarFile(file)
                    rf.extract(startpath)
            print('Completed extracting '+file+'!!!')
    print('=========')
    print('COMPLETED')
    print('=========')
if __name__ == "__main__":
    recursive_unrar()