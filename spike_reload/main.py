#!/usr/bin/env python3
from nice_gui import ui, pad

print(pad, __name__, "MAIN: create label")
ui.label('Hello NiceGUI!')

print(pad, __name__, "MAIN: create timer")
ui.timer()