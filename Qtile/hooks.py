from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    from os.path import expanduser
    from subprocess import call
    home = expanduser('~/.config/qtile/autostart.sh')
    call([home])

@hook.subscribe.client_new
def move(window):
    if window.name == "whatsdesk":
        c.togroup("CHAT")
    elif window.name == "discord":
        c.togroup("CHAT")
    elif window.name == "code":
        c.togroup("DEV")
    elif window.name == "spotify":
        c.togroup("MUS")