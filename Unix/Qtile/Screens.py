#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libqtile import bar
from libqtile.widget import *
from libqtile.config import Screen
from libqtile.lazy import lazy
from Constants import CONSTANTS

colors = CONSTANTS.COLORS

def init_widgets_right_monitor():
    widgets_list = [
              Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              GroupBox(
                       fontsize = 12,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[2],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[3],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[0],
                       other_screen_border = colors[0],
                       foreground = colors[2],
                       background = colors[0]
                       ),
              Sep(
                       linewidth = 0,
                       padding = 40,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              WindowName(
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0,
                       fontisze = 12
                       ),
              KeyboardLayout(
                       foreground = colors[5],
                       background = colors[0],
                       padding = 0,
                       fontsize = 12,
                       configured_keyboards = ["us", "br"],
                       display_map = {"us": "EN"}
                       ),
              TextBox(
                       text = '  |  ',
                       background = colors[0],
                       foreground = colors[4],
                       padding = 0
                       ),
              DF(
                       foreground = colors[6],
                       background = colors[0],
                       format =" {r:.0f}%",
                       partition = '/',
                       visible_on_warn = False,
                       padding = 0,
                       fontsize = 12
                       ),
              TextBox(
                       text = '  |  ',
                       background = colors[0],
                       foreground = colors[5],
                       padding = 0
                       ),
              CheckUpdates(
                       colour_have_updates = colors[5],
                       background = colors[0],
                       distro = "Arch",
                       display_format = " {updates}",
                       mouse_callbacks = {'Button1': lambda qtile:qtile.cmd_spawn(f"{CONSTANTS.TERMINAL} -e sudo pacman -Syu")},
                       padding = 5,
                       fontsize = 12
                       ),
              ]
    return widgets_list


def init_widgets_left_monitor():
    widgets_list = [
              Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              GroupBox(
                       fontsize = 12,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[2],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[3],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[0],
                       other_screen_border = colors[0],
                       foreground = colors[2],
                       background = colors[0]
                       ),
              Sep(
                       linewidth = 0,
                       padding = 40,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              WindowName(
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0,
                       fontsize = 12
                       ),
              Net(
                       interface = "enp4s0",
                       format = '{down} ↓↑{up}',
                       foreground = colors[5],
                       background = colors[0],
                       padding = 5,
                       fontsize = 12
                       ),
              TextBox(
                       text = '  |  ',
                       background = colors[0],
                       foreground = colors[4],
                       padding = 0
                       ),
              CPU(
                       format = " {load_percent} ",
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0
                       ),
              TextBox(
                       text = '  |  ',
                       background = colors[0],
                       foreground = colors[5],
                       padding = 0
                       ),
              TextBox(
                       text = '  |  ',
                       background = colors[0],
                       foreground = colors[4],
                       padding = 0
                       ),
              Memory(
                       foreground = colors[4],
                       background = colors[0],
                       format = " {MemUsed} MB ",
                       mouse_callbacks = {'Button1': lazy.spawn(f"{CONSTANTS.TERMINAL} -e bpytop")},
                       padding = 5,
                       fontsize = 12
                       ),
              TextBox(
                       text = '  |  ',
                       background = colors[0],
                       foreground = colors[5],
                       padding = 0
                       ),
              Clock(
                       foreground = colors[5],
                       background = colors[0],
                       format = "%H:%M",
                       fontsize = 12,
                       ),
              Sep(
                       linewidth = 0,
                       padding = 10,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              ]
    return widgets_list

def getScreens():
    return [Screen(top=bar.Bar(widgets=init_widgets_right_monitor(), opacity=1.0, size=25)),
            Screen(top=bar.Bar(widgets=init_widgets_left_monitor(), opacity=1.0, size=25))]
