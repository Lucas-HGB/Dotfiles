from libqtile.config import Group
group_names = [("WWW", {'layout': 'monadtall', "spawn": ["vivaldi-stable"]}),
               ("DEV", {'layout': 'monadtall', "spawn": [""]}),
               ("SYS", {'layout': 'monadtall'}),
               ("CHAT", {'layout': 'monadtall', "spawn": ["whatsdesk", "discord"]}),
               ("MUS", {'layout': 'monadtall', "spawn": ["spotify"]})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

def init_groups():
    return group_names, groups
