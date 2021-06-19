from libqtile.config import Group
group_names = [("Code ", {'layout': 'monadtall', "spawn": [""]}),
               ("Web ", {'layout': 'monadtall', "spawn": [""]}),
               ("System ", {'layout': 'monadtall'}),
               ("Chat ", {'layout': 'monadtall', "spawn": [""]}),
               ("Music 阮", {'layout': 'monadtall', "spawn": [""]}),
               ("Study ", {'layout': 'monadtall', "spawn": [""]})
               ]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

def getGroups():
    return group_names, groups