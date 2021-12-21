from libqtile.config import Key, Screen
from libqtile import bar, widget
from libqtile.lazy import lazy
from Constants import CONSTANTS


class Keys:

    def __init__(self, group_names):
        self.keys = []
        self.group_names = group_names

    def get_keys(self) -> list[Key]:
        self.init_windows_focus()
        self.init_window_control()
        self.init_window_sizes()
        self.init_launch()
        self.init_general()
        for i, (name, kwargs) in enumerate(self.group_names, 1):
            self.keys.append(Key([CONSTANTS.MOD], str(i), lazy.group[name].toscreen()))        # Switch to another group
            self.keys.append(Key([CONSTANTS.MOD, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

        return self.keys

    def init_windows_focus(self):
        self.keys += [
            Key([CONSTANTS.MOD], "h", lazy.layout.left(), 
                desc="Move focus to left"),
            Key([CONSTANTS.MOD], "l", lazy.layout.right(), 
                desc="Move focus to right"),
            Key([CONSTANTS.MOD], "j", lazy.layout.down(), 
                desc="Move focus down"),
            Key([CONSTANTS.MOD], "k", lazy.layout.up(), 
                desc="Move focus up"),
            Key([CONSTANTS.MOD], "space", lazy.layout.next(),
                desc="Move window focus to other window")
        ]

    def init_window_control(self):
        self.keys += [
            Key([CONSTANTS.MOD, "shift"], "h", lazy.layout.shuffle_left(),
                desc="Move window to the left"),
            Key([CONSTANTS.MOD, "shift"], "l", lazy.layout.shuffle_right(),
                desc="Move window to the right"),
            Key([CONSTANTS.MOD, "shift"], "j", lazy.layout.shuffle_down(),
                desc="Move window down"),
            Key([CONSTANTS.MOD, "shift"], "k", lazy.layout.shuffle_up(), 
                desc="Move window up")
        ]

    def init_window_sizes(self):
        self.keys += [
            Key([CONSTANTS.MOD, "control"], "h", lazy.layout.grow_left(),
                desc="Grow window to the left"),
            Key([CONSTANTS.MOD, "control"], "l", lazy.layout.grow_right(),
                desc="Grow window to the right"),
            Key([CONSTANTS.MOD, "control"], "j", lazy.layout.grow_down(),
                desc="Grow window down"),
            Key([CONSTANTS.MOD, "control"], "k", lazy.layout.grow_up(), 
                desc="Grow window up"),
            Key([CONSTANTS.MOD], "n", lazy.layout.normalize(), 
                desc="Reset all window sizes")
        ]

    def init_launch(self):
        self.keys += [
            Key([CONSTANTS.MOD], "Return", lazy.spawn(CONSTANTS.TERMINAL), 
                desc="Launch CONSTANTS.TERMINAL"),
            Key([CONSTANTS.MOD], "E", lazy.spawn(CONSTANTS.FILE_MANAGER), 
                desc="Launch File Manager"),
            Key([CONSTANTS.MOD], "f", lazy.spawn(CONSTANTS.WEB_BROWSER), 
                desc="Launch web browser"),
            Key([CONSTANTS.MOD], "r", lazy.spawn("/home/lucas/.config/rofi/bin/launcher"),
                desc='Run dmenu'),
        ]

    def init_general(self):
        self.keys += [
            Key([CONSTANTS.MOD], "Tab", lazy.next_layout(), 
                desc="Toggle between layouts"),
            Key([CONSTANTS.MOD], "q", lazy.window.kill(), 
                desc="Kill focused window"),
            Key([CONSTANTS.MOD, "shift"], "c", lazy.restart(), 
                desc="Restart Qtile"),
            Key([CONSTANTS.MOD, "control"], "q", lazy.shutdown(), 
                desc="Shutdown Qtile"),
        ]