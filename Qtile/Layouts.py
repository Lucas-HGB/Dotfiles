from libqtile import layout
layouts = [
    layout.Max(),
    layout.MonadTall(),
    layout.Floating()
]

def getLayouts():
    return layouts