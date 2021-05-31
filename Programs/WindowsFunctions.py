#!/usr/bin/env python3
from os import system
from subprocess import run, PIPE
from time import sleep
import mouse
from subprocess import Popen, CREATE_NO_WINDOW


def get_command_output(command):
    output = run(command.split(), stdout=PIPE).stdout
    return output

class WindowsFunctions():

    def exec_command(*args):
        phrase = ""
        for arg in args[1]:
            phrase += arg + " "
        Popen(phrase)

    ## Utils

    def killActiveWindow(self):
        Popen("Powershell -WindowStyle Hidden -NoLogo -NonInteractive -NoProfile -ExecutionPolicy Bypass -Encoded WwBTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBFAG4AYwBvAGQAaQBuAGcAXQA6ADoAVQBUAEYAOAAuAEcAZQB0AFMAdAByAGkAbgBnACgAWwBTAHkAcwB0AGUAbQAuAEMAbwBuAHYAZQByAHQAXQA6ADoARgByAG8AbQBCAGEAcwBlADYANABTAHQAcgBpAG4AZwAoACgAJwB7ACIAUwBjAHIAaQBwAHQAIgA6ACIAUQBXAFIAawBMAFYAUgA1AGMARwBVAGcAUQBDAEkATgBDAGkAQQBnAGQAWABOAHAAYgBtAGMAZwBVADMAbAB6AGQARwBWAHQATwB3ADAASwBJAEMAQgAxAGMAMgBsAHUAWgB5AEIAVABlAFgATgAwAFoAVwAwAHUAVQBuAFYAdQBkAEcAbAB0AFoAUwA1AEoAYgBuAFIAbABjAG0AOQB3AFUAMgBWAHkAZABtAGwAagBaAFgATQA3AEQAUQBvAGcASQBIAEIAMQBZAG0AeABwAFkAeQBCAGoAYgBHAEYAegBjAHkAQgBVAGMAbQBsAGoAYQAzAE0AZwBlAHcAMABLAEkAQwBBAGcASQBGAHQARQBiAEcAeABKAGIAWABCAHYAYwBuAFEAbwBJAG4AVgB6AFoAWABJAHoATQBpADUAawBiAEcAdwBpAEsAVgAwAE4AQwBpAEEAZwBJAEMAQgB3AGQAVwBKAHMAYQBXAE0AZwBjADMAUgBoAGQARwBsAGoASQBHAFYANABkAEcAVgB5AGIAaQBCAEoAYgBuAFIAUQBkAEgASQBnAFIAMgBWADAAUgBtADkAeQBaAFcAZAB5AGIAMwBWAHUAWgBGAGQAcABiAG0AUgB2AGQAeQBnAHAATwB3ADAASwBmAFEAMABLAEkAawBBAE4AQwBnADAASwBKAEcARQBnAFAAUwBCAGIAZABIAEoAcABZADIAdAB6AFgAVABvADYAUgAyAFYAMABSAG0AOQB5AFoAVwBkAHkAYgAzAFYAdQBaAEYAZABwAGIAbQBSAHYAZAB5AGcAcABEAFEAbwBOAEMAaQBSAFgAUwBDAEEAOQBJAEcAZABsAGQAQwAxAHcAYwBtADkAagBaAFgATgB6AEkASAB3AGcAUAB5AEIANwBJAEMAUgBmAEwAbQAxAGgAYQBXADUAMwBhAFcANQBrAGIAMwBkAG8AWQBXADUAawBiAEcAVQBnAEwAVwBWAHgASQBDAFIAaABJAEgAMABOAEMAaQBSAGgAWQAzAFIAcABkAG0AVgBRAFMAVQBRAGcAUABTAEEAawBWADAAZwB1AFMAVQBRAE4AQwBsAE4AMABiADMAQQB0AFUASABKAHYAWQAyAFYAegBjAHkAQQB0AFIAbQA5AHkAWQAyAFUAZwBMAFUAbABFAEkAQwBSAGgAWQAzAFIAcABkAG0AVgBRAFMAVQBRAE4AQwBnAD0APQAiAH0AJwAgAHwAIABDAG8AbgB2AGUAcgB0AEYAcgBvAG0ALQBKAHMAbwBuACkALgBTAGMAcgBpAHAAdAApACkAIAB8ACAAaQBlAHgA", creationflags=CREATE_NO_WINDOW)

    def shutdown(self):
        Popen("shutdown /s", creationflags=CREATE_NO_WINDOW)

    def reboot(self):
        Popen("shutdown /r", creationflags=CREATE_NO_WINDOW)

    ## Folders
    def openDocumentsFolder(self):
        system(r'explorer.exe "S:\Documents"')

    def openDesktopFolder(self):
        system(r'explorer.exe "S:\Desktop"')
    
    def openDownloadsFolder(self):
        system(r'explorer.exe "S:\Downloads"')

    def openMusicsFolder(self):
        system(r'explorer.exe "S:\Music"')

    def openAppDataFolder(self):
        system(r'explorer.exe "C:\Users\lucas\AppData"')

    ## Web
    
    def openYoutube(self):
        system(r'"C:\Program Files\Mozilla Firefox\firefox.exe" youtube.com')

    def openGitHub(self):
        system(r'"C:\Program Files\Mozilla Firefox\firefox.exe" github.com')

    ## Apps

    def openWhatsapp(self):
        system(r'"C:\Users\lucas\AppData\Local\WhatsApp\WhatsApp.exe"')

    ## Clicks
    def click10(self):
        for i in range(10):
            sleep(0.025)
            mouse.click()

    def click25(self):
        for i in range(25):
            sleep(0.025)
            mouse.click()

    def click50(self):
        for i in range(50):
            sleep(0.025)
            mouse.click()

    def click100(self):
        for i in range(100):
            sleep(0.025)
            mouse.click()