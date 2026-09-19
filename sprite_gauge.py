"""Value-driven sprite animation, same technique as the old Twisty Tkinter GUI:
swap a Label's image for one of 256 pre-rendered frames (000.png..255.png)
depending on the current value. The mapping to 0..255 is purely cosmetic -
it only picks which frame to show, it never affects the real numeric value.
"""
import os
import tkinter as tk

from PIL import Image, ImageTk

FRAME_COUNT = 256


class SpriteGauge(tk.Label):
    def __init__(self, parent, image_dir, scale=1.0, **kwargs):
        super().__init__(parent, **kwargs)
        self._frames = []
        for i in range(FRAME_COUNT):
            path = os.path.join(image_dir, f"{i:03d}.png")
            img = Image.open(path)
            if scale != 1.0:
                size = (max(1, round(img.width * scale)), max(1, round(img.height * scale)))
                img = img.resize(size, Image.LANCZOS)
            self._frames.append(ImageTk.PhotoImage(img))
        self.set_index(0)

    def set_index(self, index):
        index = max(0, min(FRAME_COUNT - 1, int(index)))
        self.configure(image=self._frames[index])

    def set_value(self, value, vmin, vmax):
        """Scale value from [vmin, vmax] to a frame index [0, 255]."""
        if vmax <= vmin:
            self.set_index(0)
            return
        ratio = (value - vmin) / (vmax - vmin)
        ratio = max(0.0, min(1.0, ratio))
        self.set_index(round(ratio * (FRAME_COUNT - 1)))
