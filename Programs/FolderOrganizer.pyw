from os import listdir, mkdir
from os.path import isfile, isdir, dirname, realpath, join
from shutil import move
from time import sleep
from subprocess import Popen, CREATE_NO_WINDOW, PIPE, run


def get_command_output(command):
    output = run(["powershell.exe", "-Command", command],
                 stdout=PIPE).stdout.decode('utf-8')
    return output.replace("\n", "").replace("\r", "")


def filter(file):
    myDict = {
        "Executável": ["exe", "msi"],
        "Office": ["docx", "xlsx", "pdf", "xls", "ods"],
        "Picture": ["png", "jpg"],
        "Compressed": ["7z", "zip", "rar", "tar", "gz"],
        "Audio": ["mp3"],
        "Video": ["mp4"],
        "Coding": ["py", "java", "cs", "ps1", "sh", "html", "ps1", "pyw"]
    }
    for key, value in myDict.items():
        if any([file.endswith(ext) for ext in value]):
            return key


def Main():
    Downloads = get_command_output(
        """ powershell.exe -Command "Write-Host (New-Object -ComObject Shell.Application).NameSpace('shell:Downloads').Self.Path" """)
    Documents = get_command_output(
        """ powershell.exe -Command "[environment]::getfolderpath('MyDocuments')" """)
    Pictures = get_command_output(
        """ powershell.exe -Command "[environment]::getfolderpath('MyPictures')" """)
    Videos = get_command_output(
        """ powershell.exe -Command "[environment]::getfolderpath('MyVideos')" """)
    Music = get_command_output(
        """ powershell.exe -Command "[environment]::getfolderpath('MyMusic')" """)
    while True:
        for file in [file for file in listdir(Downloads) if isfile(join(Downloads, file)) 
            and not file.endswith("part") and not file.endswith("tmp")]:
            result = filter(file)
            if result == "Executável":
                if not isdir(join(Downloads, "Executáveis")):
                    mkdir(join(Downloads, "Executáveis"))

                endDir = join(Downloads, "Executáveis", file)
                move(join(Downloads, file), endDir)

            elif result == "Office":
                if not isdir(join(Documents, "Office")):
                    mkdir(join(Documents, "Office"))

                if not isdir(join(Documents, "Office", file.split(".")[-1])):
                    mkdir(join(Documents, "Office", file.split(".")[-1]))

                endDir = join(Documents, "Office", file.split(".")[-1], file)
                move(join(Downloads, file), endDir)

            elif result == "Picture":
                endDir = "S:\\Pictures\\{}".format(file)
                move(join(Downloads, file), endDir)

            elif result == "Compressed":
                if not isdir(join(Downloads, "Compressed")):
                    mkdir(join(Downloads, "Compressed"))

                endDir = join(Downloads, "Compressed", file)
                move(join(Downloads, file), endDir)

            elif result == "Audio":
                if not isdir(join(Music, "Downloads")):
                    mkdir(join(Music, "Downloads"))

                endDir = join(Music, "Downloads", file)
                move(join(Downloads, file), endDir)

            elif result == "Coding":
                if not isdir(join(Downloads, "Coding")):
                    mkdir(join(Downloads, "Coding"))

                endDir = join(Downloads, "Coding", file)
                move(join(Downloads, file), endDir)

            elif result == "Video":
                endDir = join(Videos, file)
                move(join(Downloads, file), endDir)

            else:
                if not isdir(join(Downloads, file.split(".")[-1])):
                    mkdir(join(Downloads, file.split(".")[-1]))

                endDir = join(Downloads, file.split(".")[-1], file)
                move(join(Downloads, file), endDir)

            programDir = dirname(realpath(__file__))
            partEndDir = "\\".join(endDir.split("\\")[-3::])
            Popen(r"""powershell -ExecutionPolicy unrestricted -command "& {{ . '{}\\src\\Notify.ps1'; Notify -Title 'Downloads' -PathToImg '{}\\src\\DownloadIcon.png' -Text '{}' -Action '{}' }} " """.format(
                programDir, programDir, partEndDir, endDir), creationflags=CREATE_NO_WINDOW)
        sleep(3)


if __name__ == "__main__":
    Main()
