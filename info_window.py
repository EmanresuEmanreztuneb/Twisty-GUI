"""Standalone "Info" window: credits/thanks to Ultrawipf (Yannick Richter),
the author of the open-source OpenFFBoard firmware and GUI this project is
built on top of. Kept in its own file so main.py only needs a single button
+ one call to open_info_window() - none of the credits content lives there.

The credits text used to be a separate label here, but now lives baked
directly into the board image itself (per user request) - this window is
just that image and the GitHub link below it. No Close button (removed
per user request) - the window's own titlebar [X] already closes it.

Laid out with place(x=, y=) instead of pack() (per user request, pack()'s
own pady spacing made the link-to-button gap far bigger than intended) -
these coordinates are local to this window only, not part of the shared
Placement.py module, since nothing here is reused elsewhere.
"""
import os
import webbrowser

import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

WINDOW_WIDTH = 420
WINDOW_HEIGHT = 560

# Portrait board image (1088x1406 native) - box sized to that aspect ratio
# so it fills the space instead of landscape-fitting with empty side bars.
IMAGE_MAX_SIZE = (380, 490)
IMAGE_Y = 16

LINK_Y = IMAGE_Y + IMAGE_MAX_SIZE[1] + 16  # one line's worth of gap below the image

OPENFFBOARD_URL = "https://github.com/Ultrawipf/OpenFFBoard"


def _load_image(path, max_size):
    img = Image.open(path)
    img.thumbnail(max_size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)


def open_info_window(parent, images_dir):
    """Create and show the Info/credits Toplevel. Keeps its own PhotoImage
    reference alive via the window instance itself (win.board_img) so it's
    not garbage-collected while the window is open."""
    win = tk.Toplevel(parent)
    win.title("Info")
    win.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    win.resizable(False, False)
    win.transient(parent)

    # Toplevels don't inherit the root's iconbitmap() - without this, this
    # window shows Tk's own default feather-quill icon instead of Twisty's.
    icon_path = os.path.join(os.path.dirname(images_dir), "icon.ico")
    try:
        win.iconbitmap(icon_path)
    except tk.TclError:
        pass

    info_dir = os.path.join(images_dir, "info")
    win.board_img = _load_image(os.path.join(info_dir, "ffboard_board.png"), IMAGE_MAX_SIZE)

    ttk.Label(
        win, image=win.board_img, relief="solid", borderwidth=1,
    ).place(x=WINDOW_WIDTH // 2, y=IMAGE_Y, anchor="n")

    link = ttk.Label(
        win, text=OPENFFBOARD_URL, foreground="#1a5fb4", cursor="hand2",
    )
    link.place(x=WINDOW_WIDTH // 2, y=LINK_Y, anchor="n")
    link.bind("<Button-1>", lambda e: webbrowser.open(OPENFFBOARD_URL))

    return win
