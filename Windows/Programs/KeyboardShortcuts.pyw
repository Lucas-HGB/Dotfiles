#!/usr/bin/python3
import keyboard
import sys
from os.path import dirname, realpath
programDir = dirname(realpath(__file__))
sys.path.insert(0, programDir)
from src.WindowsFunctions import WindowsFunctions
from json import load
from threading import Thread
from time import sleep

class ShortcutsHandler(WindowsFunctions):

    def load_json(self):
        try:
            self.rawShortcuts = load(open(f"{programDir}\\src\\Shortcuts.json", "r"))
        except:
            pass

    def initShortcuts(self):
        for shortcut, action in self.rawShortcuts["Shortcuts"].items():
            actionFunc = getattr(self, action["Function"])
            if action.get("args"):
                keyboard.add_hotkey(shortcut, actionFunc, args=(action["args"],))
            else:
                keyboard.add_hotkey(shortcut, actionFunc)

    def initAbbreviations(self):
        for abbreviation, replace in self.rawShortcuts["Replacements"].items():
            keyboard.add_abbreviation(abbreviation, replace)

    def initListeners(self):
        for listen, action in self.rawShortcuts["Listeners"].items():
            actionFunc = getattr(self, action)
            keyboard.add_word_listener(listen, lambda a=listen, func=actionFunc:([keyboard.press_and_release("backspace") for i in range(len(a) + 1)], 
                func()), triggers=["tab"])

    def update_shortcuts(self):
        self.initShortcuts()
        self.initAbbreviations()
        self.initListeners()


def update_shortcuts():
    global handler
    while True:
        keyboard.unhook_all()
        handler.load_json()
        handler.update_shortcuts()
        print("UPDATED")
        sleep(10)


if __name__ == "__main__":
    handler = ShortcutsHandler()
    Thread(target=update_shortcuts).start()
    keyboard.wait()