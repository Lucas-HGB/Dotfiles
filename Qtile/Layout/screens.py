#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libqtile import bar
from libqtile.widget import *
from libqtile.config import Screen
from libqtile.lazy import lazy
from subprocess import Popen, PIPE
from emoji import emojize
myterminal = "alacritty"

colors = [["#282c34", "#282c34"], # panel background
          ["#434758", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#8d62a9", "#8d62a9"], # border line color for other tab and odd widgets
          ["#668bd7", "#668bd7"], # color for the even widgets
          ["#e1acff", "#e1acff"]] # window name

def init_widgets_screen1():
    widgets_list = [
              Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              Image(
                       filename = "~/.config/icons/python.png"
                      ),
              GroupBox(
                       fontsize = 9,
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
                       padding = 0
                       ),
              KeyboardLayout(
                       foreground = colors[5],
                       background = colors[0],
                       padding = 0,
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
                       format =emojize(":floppy_disk:") + " {r:.0f}%",
                       partition = '/',
                       visible_on_warn = False,
                       padding = 0
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
                       display_format = "{updates} " + emojize(":package:"),
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(f"{myterminal} -e sudo pacman -Syu")},
                       padding = 5
                       ),
              ]
    return widgets_list


def init_widgets_screen2():
    widgets_list = [
              Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              Image(
                       filename = "~/.config/icons/python.png"
                      ),
              GroupBox(
                       fontsize = 9,
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
                       padding = 0
                       ),
              Net(
                       interface = "enp4s0",
                       format = '{down}  ↓↑ {up}',
                       foreground = colors[5],
                       background = colors[0],
                       padding = 5
                       ),
              TextBox(
                       text = '  |  ',
                       background = colors[0],
                       foreground = colors[4],
                       padding = 0
                       ),
              CPU(
                       format = "{load_percent} CPU",
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
                       text = "🌡",
                       padding = 2,
                       foreground = colors[2],
                       background = colors[0],
                       fontsize = 13
                       ),
              ThermalSensor(
                       foreground = colors[5],
                       background = colors[0],
                       threshold = 90,
                       padding = 5
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
                       format = "{MemUsed} MB " + emojize(":pager:"),
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(f"{myterminal} -e bpytop")},
                       padding = 5
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
                       format = "%H:%M"
                       ),
              Sep(
                       linewidth = 0,
                       padding = 10,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              ]
    return widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20))]
