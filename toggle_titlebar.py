#!/usr/bin/env python
# −*− coding: UTF−8 −*−

# ToggleTitlebar - Terminator Plugin to toggle titlebar in context menu

from gi.repository import Gtk
import terminatorlib.plugin as plugin
from terminatorlib.translation import _

# Every plugin you want Terminator to load *must* be listed in 'AVAILABLE'
AVAILABLE = ['ToggleTitlebar']


class ToggleTitlebar(plugin.MenuItem):

    def __init__(self):
        plugin.MenuItem.__init__(self)

    def callback(self, menuitems, menu, terminal):
        item = Gtk.CheckMenuItem(_('Show titlebar'))
        item.set_active(terminal.titlebar.get_property('visible'))
        item.connect("toggled", self.do_titlebar_toggle, terminal)
        menuitems.append(item)

    @classmethod
    def do_titlebar_toggle(cls, _widget, terminal):
        config = terminal.config
        config['show_titlebar'] = not config['show_titlebar']
        config.save()
        terminal.toggle_widget_visibility(terminal.titlebar)
