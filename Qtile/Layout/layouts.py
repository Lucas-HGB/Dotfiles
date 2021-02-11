from libqtile import layout
layouts = [
    layout.Max(),
    layout.MonadTall(),
    layout.Floating()
]

def init_layouts():
    return layouts