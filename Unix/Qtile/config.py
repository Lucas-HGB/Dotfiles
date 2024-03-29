## COPYRIGHT
    # Copyright (c) 2010 Aldo Cortesi
    # Copyright (c) 2010, 2014 dequis
    # Copyright (c) 2012 Randall Ma
    # Copyright (c) 2012-2014 Tycho Andersen
    # Copyright (c) 2012 Craig Barnes
    # Copyright (c) 2013 horsik
    # Copyright (c) 2013 Tao Sauvage
    #
    # Permission is hereby granted, free of charge, to any person obtaining a copy
    # of this software and associated documentation files (the "Software"), to deal
    # in the Software without restriction, including without limitation the rights
    # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    # copies of the Software, and to permit persons to whom the Software is
    # furnished to do so, subject to the following conditions:
    #
    # The above copyright notice and this permission notice shall be included in
    # all copies or substantial portions of the Software.
    #
    # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THEqq
    # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    # SOFTWARE.

from typing import List  # noqa: F401

from libqtile import layout
from libqtile.config import Click, Drag, Match
from libqtile.lazy import lazy

## CUSTOM
from Groups import Groups
from Keys import Keys
from Layouts import Layout
from Settings import getSettings
from Screens import Screens

screens = Screens().get_screens()

group_names, groups = Groups().get_groups()
keys = Keys(group_names).get_keys()
layouts = Layout().get_layouts()

locals().update(Settings().get_settings())

widget_defaults = extension_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3
)


# Drag floating layouts.
mouse = [
    Drag([CONSTANTS.MOD], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([CONSTANTS.MOD], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([CONSTANTS.MOD], "Button2", lazy.window.bring_to_front())
]


floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='pavucontrol'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])

