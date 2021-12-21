from libqtile import layout


class Layout:

	def __init__(self):
		self.layouts = []

	def init_layouts(self):
		self.layouts += [
		    layout.Max(),
		    layout.MonadTall(),
		    layout.Floating()
		]

	def get_layouts(self) -> list[layout]:
		self.init_layouts()
		return self.layouts