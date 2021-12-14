import os
from shutil import move
from time import sleep
from subprocess import Popen, CREATE_NO_WINDOW, PIPE, run


def get_command_output(command):
    output = run(["powershell.exe", "-Command", command],
                 stdout=PIPE).stdout.decode('utf-8')
    return output.replace("\n", "").replace("\r", "")



class Folders:

    def get_downloads():
        return get_command_output(""" powershell.exe -Command "Write-Host (New-Object -ComObject Shell.Application).NameSpace('shell:Downloads').Self.Path" """)

    def get_documents():
        return get_command_output(""" powershell.exe -Command "[environment]::getfolderpath('MyDocuments')" """)

    def get_pictures():
        return get_command_output(""" powershell.exe -Command "[environment]::getfolderpath('MyPictures')" """)

    def get_videos():
        return get_command_output(""" powershell.exe -Command "[environment]::getfolderpath('MyVideos')" """)

    def get_music():
        return get_command_output(""" powershell.exe -Command "[environment]::getfolderpath('MyMusic')" """)


class Main():

    def __init__(self):
        self.script_path = os.path.dirname(os.path.realpath(__file__))
        self.extension_blacklist = ['part', 'tmp']
        self.extension_mapping = {
            self.move_executable: ["exe", "msi"],
            self.move_office: ["docx", "xlsx", "pdf", "xls", "ods"],
            self.move_picture: ["png", "jpg", "jpeg"],
            self.move_compressed: ["7z", "zip", "rar", "tar", "gz"],
            self.move_audio: ["mp3"],
            self.move_video: ["mp4"]
        }
        self.set_folders()

    def set_folders(self):
        self.downloads = Folders.get_downloads()
        self.documents = Folders.get_documents()
        self.pictures  = Folders.get_pictures()
        self.music     = Folders.get_music()
        self.videos    = Folders.get_videos()

    def organize(self):
        self.update_files()
        for file in self.files:
            self.filter(file)

    def filter(self, file):
        extension = self.get_file_extension(file)
        for move_function, extensions in self.extension_mapping.items():
            if extension in extensions:
                complete_path, successfull = move_function(file)
                if successfull:
                    self.notify(os.path.join(self.downloads, file), complete_path)
                return
        complete_path, successfull = self.move_no_ext(file)
        if successfull:
            self.notify(os.path.join(self.downloads, file), complete_path)

    def update_files(self):
        self.files = [f for f in os.listdir(self.downloads) if self.get_file_extension(f) not in self.extension_blacklist and os.path.isfile(os.path.join(self.downloads, f))]

    def get_file_extension(self, file):
        return os.path.splitext(file)[1].lower()[1::]

    def create_if_not_exists(self, path):
        try:
            os.makedirs(path)
        except FileExistsError:
            return

    def move(self, file, end_path):
        try:
            move(file, end_path)
            return True
        except (FileNotFoundError, PermissionError):
            return False

    def move_executable(self, file):
        end_dir = os.path.join(self.downloads, 'Executables')
        return self.move_default(end_dir, file)

    def move_office(self, file):
        end_dir = os.path.join(self.documents, 'Office')
        return self.move_default(end_dir, file)

    def move_compressed(self, file):
        end_dir = os.path.join(self.downloads, 'Compressed')
        return self.move_default(end_dir, file)

    def move_picture(self, file):
        return self.move_default(self.pictures, file)

    def move_audio(self, file):
        return self.move_default(self.music, file)

    def move_video(self, file):
        return self.move_default(self.videos, file)

    def move_default(self, end_dir, file):
        complete_path = os.path.join(end_dir, file)
        self.create_if_not_exists(end_dir)
        return complete_path, self.move(os.path.join(self.downloads, file), complete_path)

    def move_no_ext(self, file):
        file_extension = self.get_file_extension(file)
        end_dir = os.path.join(self.downloads, file_extension)
        complete_path = os.path.join(end_dir, file)
        self.create_if_not_exists(end_dir)
        return complete_path, self.move(os.path.join(self.downloads, file), complete_path)

    def notify(self, start_path, end_path):
        split_end_dir = "\\".join(end_path.split("\\")[-3::])
        Popen(r"""powershell -ExecutionPolicy unrestricted -command "& {{ . '{}\\src\\Notify.ps1'; Notify -Title 'Downloads' -PathToImg '{}\\src\\DownloadIcon.png' -Text '{}' -Action '{}' }} " """.format(
        self.script_path, self.script_path, split_end_dir, end_path), creationflags=CREATE_NO_WINDOW)



if __name__ == "__main__":
    main = Main()
    while True:
        main.organize()
        sleep(1)
