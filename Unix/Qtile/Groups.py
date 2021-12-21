from libqtile.config import Group

class Groups:

	def __init__(self):
		self.group_names = [
			("Code ", {'layout': 'monadtall', "spawn": [""]}),
        	("Web ", {'layout': 'monadtall', "spawn": [""]}),
        	("System ", {'layout': 'monadtall'}),
        	("Chat ", {'layout': 'monadtall', "spawn": [""]}),
        	("Music 阮", {'layout': 'monadtall', "spawn": [""]}),
        	("Study ", {'layout': 'monadtall', "spawn": [""]})
        ]

	def get_groups(self) -> tuple[list[tuple[str, dict]], list[Group]]:
		groups = [Group(name, **kwargs) for name, kwargs in self.group_names]
		return (self.group_names, groups)