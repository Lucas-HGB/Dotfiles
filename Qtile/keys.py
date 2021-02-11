from libqtile.config import Key
from libqtile.lazy import lazy

myterminal = "alacritty"

def return_keys(mod):
    keys = [
    ## Window Controls
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),
    Key([mod, "shift"], "m",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'),
    Key([mod], "Right",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall)'
        ),
    Key([mod], "Left",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall)'
        ),
    Key([mod, "shift"], "space",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
        ),

    ## Media Keys
    Key(["mod1"], "F3",
        lazy.spawn("amixer -D pulse sset Master 10%+"),
        desc='Increase volume by 10%'
        ),
    Key(["mod1"], "F2",
        lazy.spawn("amixer -D pulse sset Master 10%-"),
        desc='Lower volume by 10%'
        ),
    Key(["mod1"], "F5",
        lazy.spawn("omnipause previous"),
        desc='Plays previous media'
        ),
    Key(["mod1"], "F6",
        lazy.spawn("omnipause toggle"),
        desc='Pauses Media'
        ),
    Key(["mod1"], "F7",
        lazy.spawn("omnipause next"),
        desc='Next Media'
        ),

    ## Spawns
    Key([mod], "Return", lazy.spawn(myterminal), desc="Launch terminal"),
    Key([mod], "e", lazy.spawn("nemo"), desc="Launch File Explorer"),
    Key([mod], "w", lazy.spawn("vivaldi-stable"), desc="Launch Vivaldi"),
    Key([mod], "r", lazy.spawn("rofi -show drun -config ~/.config/rofi/themes/dt-dmenu.rasi -display-drun \"Run: \" -drun-display-format \"{name}\""),desc='Run dmenu'),

    ## Other
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "l", lazy.spawn("i3lock-fancy"), desc="Lock screen"),
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "Tab",lazy.next_layout(),desc='Toggle through layouts'),

    ## Custom Scripts
    Key([mod], "space", lazy.spawn("python3 /home/lucas/.config/qtile/Scripts/Change_Keyboard.py"), desc="Change keyboard layout"),
    Key([mod], "Print", lazy.spawn("flameshot gui"), desc="Spawns flameshot")
    ]
    return keys
  
def init_keys(mod, group_names, screens):
    keys = return_keys(mod)
    for i, (name, kwargs) in enumerate(group_names, 1):
        keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
        keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group
    return keys

if __name__ == "__main__":
    pass