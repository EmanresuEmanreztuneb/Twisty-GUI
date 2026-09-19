"""Wide, flat strip chart for FFB Strength.

Deflection is horizontal (+/-100%), matching the physical left/right
direction of the force - this is why it is not a conventional chart with
time on the horizontal axis. Time runs vertically: the newest sample enters
at the bottom and old samples scroll upward off the top.
"""
import tkinter as tk

MAX_PCT = 100
MARGIN_PX = 8


class StripChart(tk.Canvas):
    def __init__(self, parent, height=120, row_height=3, **kwargs):
        kwargs.setdefault("bg", "#fdf6ec")
        kwargs.setdefault("highlightthickness", 0)
        super().__init__(parent, height=height, **kwargs)
        self.row_height = row_height
        self.samples = []
        self.bind("<Configure>", lambda e: self._redraw_trace())

    def _height(self):
        return int(self["height"])

    def _center_x(self):
        return self.winfo_width() / 2

    def _span_px(self):
        return max(1, self.winfo_width() / 2 - MARGIN_PX)

    def add_sample(self, pct):
        max_samples = max(2, self._height() // self.row_height)
        self.samples.append(pct)
        if len(self.samples) > max_samples:
            self.samples = self.samples[-max_samples:]
        self._redraw_trace()

    def _redraw_trace(self):
        self.delete("trace")
        n = len(self.samples)
        if n < 2:
            return
        h = self._height()
        cx = self._center_x()
        span = self._span_px()
        points = []
        for i, pct in enumerate(self.samples):
            y = h - (n - i) * self.row_height
            x = cx + max(-MAX_PCT, min(MAX_PCT, pct)) / MAX_PCT * span
            points.extend((x, y))
        self.create_line(*points, fill="#1a1a1a", width=1.3, tags="trace")
