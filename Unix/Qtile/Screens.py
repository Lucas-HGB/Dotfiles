#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libqtile import bar
from libqtile import widget
from libqtile.config import Screen
from libqtile.lazy import lazy
from Constants import CONSTANTS



class Screens:

	def __init__(self):
		self.colors = CONSTANTS.COLORS

	def get_widgets_left_monitor(self) -> list[widget]:
		return [
			widget.Sep(
				linewidth = 0,
				padding = 6,
				foreground = self.colors[2],
				background = self.colors[0]
				),
			widget.GroupBox(
				fontsize = 12,
				margin_y = 3,
				margin_x = 0,
				padding_y = 5,
				padding_x = 3,
				borderwidth = 3,
				active = self.colors[2],
				inactive = self.colors[2],
				rounded = False,
				highlight_color = self.colors[1],
				highlight_method = "line",
				this_current_screen_border = self.colors[3],
				this_screen_border = self.colors[4],
				other_current_screen_border = self.colors[0],
				other_screen_border = self.colors[0],
				foreground = self.colors[2],
				background = self.colors[0]
				),
			widget.Sep(
				linewidth = 0,
				padding = 40,
				foreground = self.colors[2],
				background = self.colors[0]
				),
			widget.WindowName(
				foreground = self.colors[6],
				background = self.colors[0],
				padding = 0,
				fontsize = 12
				),
			widget.Net(
				interface = "enp4s0",
				format = '{down} ↓↑{up}',
				foreground = self.colors[5],
				background = self.colors[0],
				padding = 5,
				fontsize = 12
				),
			widget.TextBox(
				text = '  |  ',
				background = self.colors[0],
				foreground = self.colors[4],
				padding = 0
				),
			widget.CPU(
				format = " {load_percent} ",
				foreground = self.colors[6],
				background = self.colors[0],
				padding = 0
				),
			widget.TextBox(
				text = '  |  ',
				background = self.colors[0],
				foreground = self.colors[5],
				padding = 0
				),
			widget.TextBox(
				text = '  |  ',
				background = self.colors[0],
				foreground = self.colors[4],
				padding = 0
				),
			widget.Memory(
				foreground = self.colors[4],
				background = self.colors[0],
				format = " {MemUsed} MB ",
				mouse_callbacks = {'Button1': lazy.spawn(f"{CONSTANTS.TERMINAL} -e bpytop")},
				padding = 5,
				fontsize = 12
				),
			widget.TextBox(
				text = '  |  ',
				background = self.colors[0],
				foreground = self.colors[5],
				padding = 0
				),
			widget.Clock(
				foreground = self.colors[5],
				background = self.colors[0],
				format = "%H:%M",
				fontsize = 12,
				),
			widget.Sep(
				linewidth = 0,
				padding = 10,
				foreground = self.colors[0],
				background = self.colors[0]
				)
		]

	def get_widgets_right_monitor(self) -> list[widget]:
		return [
			widget.Sep(
				linewidth = 0,
				padding = 6,
				foreground = self.colors[2],
				background = self.colors[0]
				),
			widget.GroupBox(
				fontsize = 12,
				margin_y = 3,
				margin_x = 0,
				padding_y = 5,
				padding_x = 3,
				borderwidth = 3,
				active = self.colors[2],
				inactive = self.colors[2],
				rounded = False,
				highlight_color = self.colors[1],
				highlight_method = "line",
				this_current_screen_border = self.colors[3],
				this_screen_border = self.colors[4],
				other_current_screen_border = self.colors[0],
				other_screen_border = self.colors[0],
				foreground = self.colors[2],
				background = self.colors[0]
				),
			widget.Sep(
				linewidth = 0,
				padding = 40,
				foreground = self.colors[2],
				background = self.colors[0]
				),
			widget.WindowName(
				foreground = self.colors[6],
				background = self.colors[0],
				padding = 0,
				fontisze = 12
				),
			widget.KeyboardLayout(
				foreground = self.colors[5],
				background = self.colors[0],
				padding = 0,
				fontsize = 12,
				configured_keyboards = ["us", "br"],
				display_map = {"us": "EN"}
				),
			widget.TextBox(
				text = '  |  ',
				background = self.colors[0],
				foreground = self.colors[4],
				padding = 0
				),
			widget.DF(
				foreground = self.colors[6],
				background = self.colors[0],
				format =" {r:.0f}%",
				partition = '/',
				visible_on_warn = False,
				padding = 0,
				fontsize = 12
				),
			widget.TextBox(
				text = '  |  ',
				background = self.colors[0],
				foreground = self.colors[5],
				padding = 0
				),
			widget.CheckUpdates(
				colour_have_updates = self.colors[5],
				background = self.colors[0],
				distro = "Arch",
				display_format = " {updates}",
				mouse_callbacks = {'Button1': lambda qtile:qtile.cmd_spawn(f"{CONSTANTS.TERMINAL} -e sudo pacman -Syu")},
				padding = 5,
				fontsize = 12
				)
		]

	def get_screens(self) -> tuple[Screen]:
		widgets_left = self.get_widgets_left_monitor()
		widgets_right = self.get_widgets_left_monitor()
		left_screen = self.init_screen(widgets_left)
		right_screen = self.init_screen(widgets_right)
		return (right_screen, left_screen)

	def init_screen(self, widgets):
		return Screen(top=bar.Bar(widgets=widgets), opacity=1.0, size=25)