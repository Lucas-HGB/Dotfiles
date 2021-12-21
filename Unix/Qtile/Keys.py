from libqtile.config import Key, Screen
from libqtile import bar, widget
from libqtile.lazy import lazy
from Constants import CONSTANTS

def windowFocus(mod):
    windowFocusKeys = [
        Key([mod], "h", lazy.layout.left(), 
            desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), 
            desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), 
            desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), 
            desc="Move focus up"),
        Key([mod], "space", lazy.layout.next(),
            desc="Move window focus to other window")
    ]
    return windowFocusKeys

def windowControl(mod):
    windowControlKeys = [
        Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
            desc="Move window to the left"),
        Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
            desc="Move window to the right"),
        Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
            desc="Move window down"),
        Key([mod, "shift"], "k", lazy.layout.shuffle_up(), 
            desc="Move window up")
    ]
    return windowControlKeys

def windowSizes(mod):
    windowSizeKeys = [
        Key([mod, "control"], "h", lazy.layout.grow_left(),
            desc="Grow window to the left"),
        Key([mod, "control"], "l", lazy.layout.grow_right(),
            desc="Grow window to the right"),
        Key([mod, "control"], "j", lazy.layout.grow_down(),
            desc="Grow window down"),
        Key([mod, "control"], "k", lazy.layout.grow_up(), 
            desc="Grow window up"),
        Key([mod], "n", lazy.layout.normalize(), 
            desc="Reset all window sizes")
    ]
    return windowSizeKeys

def launch(mod):
    launchKeys = [
        Key([mod], "Return", lazy.spawn(CONSTANTS.TERMINAL), 
            desc="Launch CONSTANTS.TERMINAL"),
        Key([mod], "E", lazy.spawn(CONSTANTS.FILE_MANAGER), 
            desc="Launch File Manager"),
        Key([mod], "f", lazy.spawn(CONSTANTS.WEB_BROWSER), 
            desc="Launch web browser"),
        Key([mod], "r", lazy.spawn("/home/lucas/.config/rofi/bin/launcher"),
            desc='Run dmenu'),
    ]

    return launchKeys

def general(mod):
    generalKeys = [
        Key([mod], "Tab", lazy.next_layout(), 
            desc="Toggle between layouts"),
        Key([mod], "q", lazy.window.kill(), 
            desc="Kill focused window"),
        Key([mod, "shift"], "c", lazy.restart(), 
            desc="Restart Qtile"),
        Key([mod, "control"], "q", lazy.shutdown(), 
            desc="Shutdown Qtile"),
    ]
    return generalKeys


def getKeys(mod, groupNames, screens):
    keys = []
    [keys.append(shortcut) for shortcut in windowFocus(mod)]
    [keys.append(shortcut) for shortcut in windowControl(mod)]
    [keys.append(shortcut) for shortcut in launch(mod)]
    [keys.append(shortcut) for shortcut in general(mod)]
    for i, (name, kwargs) in enumerate(groupNames, 1):
        keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
        keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group
    return keys
