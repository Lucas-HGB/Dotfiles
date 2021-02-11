#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Layout.screens import init_screens
from Layout.layouts import init_layouts
from Layout.groups import init_groups
from keys import init_keys
from mouse import init_mouse
from settings import init_settings
from hooks import *

mod = "mod4"

## Inits
group_names, groups = init_groups()
screens = init_screens()
layouts = init_layouts()
mouse = init_mouse(mod)
keys = init_keys(mod = mod, group_names = group_names, screens = screens)

## Configs
dgroups_key_binder, dgroups_app_rules, main, follow_mouse_focus, bring_front_click, cursor_warp, auto_fullscreen, focus_on_window_activation, wmname = init_settings()