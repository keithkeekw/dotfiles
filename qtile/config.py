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
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, extension
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess

mod = "mod4"
#terminal = guess_terminal()
terminal = "termite"
browser = "firefox"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k",
        lazy.layout.down(),
        desc="Move focus down in stack pane"),

    Key([mod], "j",
        lazy.layout.up(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "k",
        lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),

    Key([mod, "control"], "j",
        lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space",
        lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space",
        lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    Key([mod], "Return",
        lazy.spawn(terminal),
        desc="Launch terminal"),

    Key([mod, "shift"], "Return",
        # lazy.spawn("dmenu_run -p 'Run: '"),
        lazy.spawn("rofi -show drun -display-drun \"Run: \" -drun-display-format \"{name}\""),
        desc='Run Launcher'),

    ## MondaTall
    Key([mod, "control"], "i",
        lazy.layout.grow()),

    Key([mod, "control"], "o",
        lazy.layout.shrink()),

    Key([mod, "control"], "p",
        lazy.layout.normalize()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"),

    # Hardware Controls
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer set 'Master' 5%-"),
        desc="Reduce Volume"),

    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer set 'Master' 5%+"),
        desc="Increase Volume"),

    Key([], "XF86AudioMute",
        lazy.spawn("amixer set 'Master' toggle"),
        desc="Mute Volume"),

    Key([], "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set +10%")),

    Key([], "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 10%-")),

    # Window Controls
    Key([mod, "shift"], "q",
        lazy.window.kill(),
        desc="Kill focused window"),

    Key([mod, "control"], "r",
        lazy.restart(),
        desc="Restart qtile"),

    Key([mod, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown qtile"),

    Key([mod], "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Application: SUPER + ALT

    Key([mod, "mod1"], "b",
        lazy.spawn(browser),
        desc="Launch Browser"),

    Key([mod, "mod1"], "f",
        lazy.spawn(terminal + " -e ranger"),
        desc="Launch ranger"),

    Key([mod, "mod1"], "m",
        lazy.spawn(terminal + " -e tuner"),
        desc="Launch tuner"),

    Key([mod, "mod1"], "n",
        lazy.spawn(terminal + " -e newsboat"),
        desc="Launch newsboat"),

    Key([mod, "mod1"], "y",
        lazy.spawn(terminal + " -e pipe-viewer"),
        desc="Launch Terminal YT Viewer"),

    Key([mod, "mod1"], "r",
        lazy.spawn(terminal + " -e tuir"),
        desc="Launch Terminal UI Reddit"),

    Key([mod, "mod1"], "t",
        lazy.spawn(terminal + " -e rainbowstream"),
        desc="Launch Terminal Twitter - Rainbowstream"),

    Key([mod, "mod1"], "w",
        lazy.spawn(terminal + " -e whatscli"),
        desc="Launch Terminal Whatsapp"),

    Key([mod, "mod1"], "i",
        lazy.spawn("qutebrowser"),
        desc="Launch qutebrowser"),

#    Key([mod, "mod1"], "r", lazy.run_extension(extension.DmenuRun(
#        dmenu_prompt=">",
#       foreground='#D8DEE9',
#       background='#3B4252',
#       selected_background="#EBCB8B",
#       selected_foreground="#2E3440",
#        fontsize= 12.5
#    ))),

    Key([mod, "mod1"], "l",
        lazy.spawn(terminal + " -e slock"),
        desc="Lock the screen"),

    Key([mod, "mod1"], "v",
        lazy.spawn(terminal + " -e alsamixer"),
        desc="Launch alsamixer")
]

groups = [Group(i) for i in "1234"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name,
            lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name,
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])
### LAYOUT THEME ###
layout_theme = {"border_width":3,
                "margin": 10,
                "border_focus":'EBCB8B',
                "border_normal": '2E3440'}


layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Floating(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    # layout.TreeTab(
    #    font = "Ubuntu",
    #    fontsize = 10,
    #    sections = ["FIRST", "SECOND"],
    #    section_fontsize = 11,
    #    bg_color = "141414",
    #    active_bg = "90C435",
    #    active_fg = "000000",
    #    inactive_bg = "384323",
    #    inactive_fg = "a0a0a0",
    #    padding_y = 5,
    #    section_top = 10,
    #    panel_width = 320
    #     ),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=0,
    foreground='#D8DEE9',
    background='#3B4252',
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    foreground="#3B4252",
                    padding=7
                ),

                widget.GroupBox(
                    active="#BF616A",
                    inactive="#D8DEE9",
                    highlight_method="line",
                    rounded= False,
                    highlight_color="#EBCB8B",
                    this_current_screen_border="#D08770",
                    margin_y=5
                ),

                widget.Sep(
                    foreground="#3B4252",
                    padding=10
                ),

                widget.Prompt(),

                widget.Sep(
                    foreground="#3B4252",
                    padding=20
                ),

                widget.WindowName(),

                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),

                widget.TextBox(
                   text="◥",
                   fontsize= 47,
                   foreground="#EBCB8B",
                   padding=0
                ),

                widget.CheckUpdates(
                    update_interval=1800,
                    colour_have_updates="#BF616A",
                    colour_no_updates="#2E3440",
                    foreground="#BF616A",
                    background="#EBCB8B",
                    no_update_string="Updated!",
                    display_format="📦: {updates}",
                    custom_command="checkupdates"
                ),

                widget.TextBox(
                    text="◥",
                    fontsize= 47,
                    foreground="#A3BE8C",
                    background="#EBCB8B",
                    padding=0
                ),

                widget.CurrentLayoutIcon(
                    custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                    foreground="#2E3440",
                    background="#A3BE8C",
                    scale = 0.6,
                    padding=3
                ),

                widget.TextBox(
                    text="◥", fontsize= 47,
                    background="#A3BE8C",
                    foreground="#4C566A",
                    padding=0
                ),

                widget.TextBox(
                    text="Vol: ",
                    fontsize= 12,
                    background="#4C566A",
                    foreground="#D8DEE9",
                    padding=0
                ),

                widget.Volume(
                    background="#4C566A",
                    foreground="#D8DEE9",
                    volume_up_command ="amixer set 'Master' 2%+",
                    volume_down_command ="amixer set 'Master' 2%-",
                    padding=0,
                    volume_app="alsamixer"
                ),

                widget.TextBox(
                    text="◥", fontsize= 47,
                    background="#4C566A",
                    foreground="#3B4252",
                    padding=0
                ),

                widget.Memory(
                    background="#3B4252",
                    foreground="#D8DEE9",
                     mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(terminal+ ' -e gtop')},
                    format="Mem: {MemUsed}M / {MemTotal}M",
                    padding=0
                ),

                widget.TextBox(
                    text="◥",
                    fontsize= 47,
                    background="#3B4252",
                    foreground="#4c566A",
                    padding=0
                ),

                widget.TextBox(
                    text="Battery: ",
                    fontsize= 12,
                    background="#4C566A",
                    foreground="#D8DEE9",
                    padding=0
                ),

                widget.Battery(
                    background="#4C566A",
                    foreground="#D8DEE9",
                    format="{percent:2.0%}",
                    padding=0
                ),

                widget.TextBox(
                    text="◥",
                    fontsize= 47,
                    background="#4C566A",
                    foreground="#3b4252",
                    padding=0
                ),

                widget.Wlan(
                    background="#3B4252",
                    foreground="#D8DEE9",
                    interface='wlp0s20f3',
                    format='WLAN: {essid}',
                    padding=0,
                    mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(terminal+ ' -e nmtui')}
                ),

                widget.TextBox(
                    text="◥",
                    fontsize= 47,
                    background="#3B4252",
                    foreground="#4C566A",
                    padding=0
                ),

                widget.Clock(
                    format='%a, %I:%M %p',
                    foreground="#D8DEE9",
                    background="#4c566A"
                ),

                widget.TextBox(
                    text="◥",
                    fontsize= 47,
                    foreground="#3B4252",
                    background="#4C566A",
                    padding=0
                ),

                widget.Systray(
                    padding=0,
                    foreground="#3B4252",
                    background="#3B4252"
                ),

                widget.Sep(
                    foreground="#3B4252",
                    background="#3B4252",
                    padding=7
                )
            ],
            22,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
