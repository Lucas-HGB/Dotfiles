#!/usr/bin/env python3
from os import system
from time import sleep
import mouse
from subprocess import Popen, CREATE_NO_WINDOW, run, PIPE


class WindowsFunctions():

    def exec_command(*args):
        phrase = ""
        for arg in args[1]:
            phrase += arg + " "
        Popen(phrase)

    ## Utils

    def kill_active_window(self):
        Popen("Powershell -WindowStyle Hidden -NoLogo -NonInteractive -NoProfile -ExecutionPolicy Bypass -Encoded WwBTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBFAG4AYwBvAGQAaQBuAGcAXQA6ADoAVQBUAEYAOAAuAEcAZQB0AFMAdAByAGkAbgBnACgAWwBTAHkAcwB0AGUAbQAuAEMAbwBuAHYAZQByAHQAXQA6ADoARgByAG8AbQBCAGEAcwBlADYANABTAHQAcgBpAG4AZwAoACgAJwB7ACIAUwBjAHIAaQBwAHQAIgA6ACIAUQBXAFIAawBMAFYAUgA1AGMARwBVAGcAUQBDAEkATgBDAGkAQQBnAGQAWABOAHAAYgBtAGMAZwBVADMAbAB6AGQARwBWAHQATwB3ADAASwBJAEMAQgAxAGMAMgBsAHUAWgB5AEIAVABlAFgATgAwAFoAVwAwAHUAVQBuAFYAdQBkAEcAbAB0AFoAUwA1AEoAYgBuAFIAbABjAG0AOQB3AFUAMgBWAHkAZABtAGwAagBaAFgATQA3AEQAUQBvAGcASQBIAEIAMQBZAG0AeABwAFkAeQBCAGoAYgBHAEYAegBjAHkAQgBVAGMAbQBsAGoAYQAzAE0AZwBlAHcAMABLAEkAQwBBAGcASQBGAHQARQBiAEcAeABKAGIAWABCAHYAYwBuAFEAbwBJAG4AVgB6AFoAWABJAHoATQBpADUAawBiAEcAdwBpAEsAVgAwAE4AQwBpAEEAZwBJAEMAQgB3AGQAVwBKAHMAYQBXAE0AZwBjADMAUgBoAGQARwBsAGoASQBHAFYANABkAEcAVgB5AGIAaQBCAEoAYgBuAFIAUQBkAEgASQBnAFIAMgBWADAAUgBtADkAeQBaAFcAZAB5AGIAMwBWAHUAWgBGAGQAcABiAG0AUgB2AGQAeQBnAHAATwB3ADAASwBmAFEAMABLAEkAawBBAE4AQwBnADAASwBKAEcARQBnAFAAUwBCAGIAZABIAEoAcABZADIAdAB6AFgAVABvADYAUgAyAFYAMABSAG0AOQB5AFoAVwBkAHkAYgAzAFYAdQBaAEYAZABwAGIAbQBSAHYAZAB5AGcAcABEAFEAbwBOAEMAaQBSAFgAUwBDAEEAOQBJAEcAZABsAGQAQwAxAHcAYwBtADkAagBaAFgATgB6AEkASAB3AGcAUAB5AEIANwBJAEMAUgBmAEwAbQAxAGgAYQBXADUAMwBhAFcANQBrAGIAMwBkAG8AWQBXADUAawBiAEcAVQBnAEwAVwBWAHgASQBDAFIAaABJAEgAMABOAEMAaQBSAGgAWQAzAFIAcABkAG0AVgBRAFMAVQBRAGcAUABTAEEAawBWADAAZwB1AFMAVQBRAE4AQwBsAE4AMABiADMAQQB0AFUASABKAHYAWQAyAFYAegBjAHkAQQB0AFIAbQA5AHkAWQAyAFUAZwBMAFUAbABFAEkAQwBSAGgAWQAzAFIAcABkAG0AVgBRAFMAVQBRAE4AQwBnAD0APQAiAH0AJwAgAHwAIABDAG8AbgB2AGUAcgB0AEYAcgBvAG0ALQBKAHMAbwBuACkALgBTAGMAcgBpAHAAdAApACkAIAB8ACAAaQBlAHgA", creationflags=CREATE_NO_WINDOW)

    def shutdown(self):
        Popen("shutdown /s /t 10", creationflags=CREATE_NO_WINDOW)

    def reboot(self):
        Popen("shutdown /r", creationflags=CREATE_NO_WINDOW)

    def abort_shutdown(self):
        Popen("shutdown /a", creationflags=CREATE_NO_WINDOW)

    ## Folders

    def open_documents(self):
        system(r'explorer.exe "S:\Documents"')

    def open_desktop(self):
        system(r'explorer.exe "S:\Desktop"')
    
    def open_downloads(self):
        system(r'explorer.exe "S:\Downloads"')

    def open_evi_folder(self):
        system(r'explorer.exe "S:\Documents\Coding\evi-selenium-testing"')

    ## Web

    def open_gitHub(self):
        system(r'"C:\Program Files\Mozilla Firefox\firefox.exe" github.com')

    def open_whatsapp(self):
        system(r'"C:\Users\lucas\AppData\Local\WhatsApp\WhatsApp.exe"')

    ## Clicks
    
    def click_10(self):
        for i in range(10):
            sleep(0.025)
            mouse.click()

    def click_100(self):
        for i in range(100):
            sleep(0.025)
            mouse.click()