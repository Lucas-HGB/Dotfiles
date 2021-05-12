from os import listdir, mkdir
from os.path import isfile, isdir
from shutil import move
from time import sleep
from subprocess import Popen, CREATE_NO_WINDOW

def filter(file):
    myDict = {
        "Executável": ["exe", "msi"],
        "Office": ["docx", "xlsx", "pdf", "xls", "ods"],
        "Picture": ["png", "jpg"],
        "Zippado": ["7z", "zip", "tar", "gz"],
        "Audio": ["mp3"],
        "Video": ["mp4"],
        "Coding": ["py", "java", "cs", "ps1", "sh"]
        }
    for key,value in myDict.items():
        if any([file.endswith(ext) for ext in value]):
            return key

def Main():
    while True:
        for file in [file for file in listdir("S:\Downloads") if isfile(f"S:\Downloads\{file}") and not isdir(f"S:\Downloads\{file}")]:
            result = filter(file)
            if result == "Executável":
                try: mkdir("S:\Downloads\Executáveis")
                except FileExistsError: pass
                endDir = f"S:\Downloads\Executáveis\{file}"
                move(f"S:\Downloads\{file}", endDir)

            elif result == "Office":
                try: mkdir("S:\Documents\Office\{}".format(file.split(".")[-1]))
                except FileExistsError: pass
                endDir = "S:\Documents\Office\{}\{}".format(file.split(".")[-1], file)
                move(f"S:\Downloads\{file}", endDir)

            elif result == "Picture":
                endDir = "S:\Pictures\{}".format(file)
                move(f"S:\Downloads\{file}", endDir)

            elif result == "Zippado":
                try: mkdir("S:\Downloads\Zip")
                except FileExistsError: pass
                endDir = "S:\Downloads\Zip\{}".format(file)
                move(f"S:\Downloads\{file}", endDir)

            elif result == "Audio":
                try: mkdir("S:\Music\Downloads")
                except FileExistsError: pass
                endDir = "S:\Music\Downloads\{}".format(file)
                move(f"S:\Downloads\{file}", endDir)

            elif result == "Coding":
                try: mkdir("S:\Downloads\Coding")
                except FileExistsError: pass
                endDir = "S:\Downloads\Coding\{}".format(file)
                move(f"S:\Downloads\{file}", endDir)

            elif result == "Video":
                endDir = "S:\Videos\{}".format(file)
                move(f"S:\Downloads\{file}", endDir)

            else:
                try: mkdir("S:\Downloads\{}".format(file.split(".")[-1]))
                except FileExistsError: pass
                endDir = "S:\Downloads\{}\{}".format(file.split(".")[-1], file)
                move(f"S:\Downloads\{file}", endDir)

            Popen(r"""powershell.exe -noprofile -File S:\Documents\Programs\Notification.ps1 "Moved {} to {}" """.format(file, endDir), creationflags=CREATE_NO_WINDOW)
        sleep(3)

Main()