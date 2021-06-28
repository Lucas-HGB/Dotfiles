#!/usr/bin/python3
import keyboard
import sys
from os.path import dirname, realpath
programDir = dirname(realpath(__file__))
sys.path.insert(0, programDir)
from src.WindowsFunctions import WindowsFunctions
from json import load

class ShortcutsHandler(WindowsFunctions):

    def __init__(self):
        self.rawShortcuts = load(open(f"{programDir}\\src\\Shortcuts.json", "r"))
        self.initShortcuts()
        self.initAbbreviations()
        self.initListeners()

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

if __name__ == "__main__":
    ShortcutsHandler()
    keyboard.wait()
