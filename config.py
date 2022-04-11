# -*- coding: utf-8 -*-

#import re
import string
from xkeysnail.transform import *

# define timeout for multipurpose_modmap
define_timeout(1)

# [Global modemap] Change modifier keys as in xmodmap
define_modmap({
    Key.CAPSLOCK: Key.ESC,
    Key.LEFT_META: Key.RIGHT_META,  # disable HUD
    Key.RIGHT_CTRL: Key.RIGHT_META, # Hyper tab switch
    #Key.LEFT_META: Key.LEFT_CTRL,
    #Key.LEFT_ALT: Key.CAPSLOCK,
    # Key.L_SUPER: Key.R_SUPER,
#    Key.CAPSLOCK: Key.LEFT_CTRL
})

#define_conditional_modmap(lambda wm_class: wm_class not in ("Emacs", "Hyper"), {
#    Key.LEFT_META: Key.LEFT_CTRL,
#})

# Always paste with ⌘-v
define_keymap(None, {
    K('Super-v'): [K("C-v"), set_mark(False)],
}, "Paste")

# Emacs-like keybindings
# Remap except emacs and terminal Hyper
# Gnome-terminal

mapping = {
    # Beginning/End of line
    K("C-a"): with_mark(K("home")),
    K("C-e"): with_mark(K("end")),
    
    # Delete
    K("C-d"): [K("delete"), set_mark(False)],
    K("C-h"): with_mark(K("backspace")),
    #K("M-d"): [K("C-delete"), set_mark(False)],
    
    # Kill line
    K("C-k"): [K("Shift-end"), K("C-x"), set_mark(False)],
}

for c in string.ascii_lowercase:
    mapping[K('Super-' + c)] = K('C-' + c)
#    mapping[K('Win-' + c)] = K('C-' + c)


define_keymap(lambda wm_class: wm_class not in ("Emacs", "Hyper"),
              mapping, "Emacs-like keys")



# ⌘-C for Copy and ⌘-V for Cut (but not in terminal)
# In terminal Hyper, mouse selection copies automatically
#define_keymap(lambda wm_class: wm_class not in ("Hyper",), {
#    K('Super-c'): [K("C-c"), set_mark(False)],
#    K('Super-x'): [K("C-x"), set_mark(False)],
#    K('Super-z'): [K("C-z"), set_mark(False)],
#}, "Copy")

# Additional mappings for Google Chrome
#define_keymap(lambda wm_class: wm_class in ('chrome'), {
#    # Cursor
#    # K("C-b"): with_mark(K("left")),
#}, "For Chrome browser")


