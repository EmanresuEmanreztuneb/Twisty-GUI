"""Layout constants only - no classes, no logic.

Every placed object gets its own pair of constants, named "<OBJECT>_X" and
"<OBJECT>_Y" - these are the exact pixel coordinates passed to that widget's
place(x=..., y=...) call in main.py. Edit the numbers here to move things;
nothing else in this file needs to change, and nothing outside this file
should contain a raw x/y pixel number.

A few non-coordinate sizes (canvas WIDTH/HEIGHT, a slider's drag-track
LENGTH, column spacing) are grouped alongside the coordinates they affect -
these are marked as sizes, not coordinates, in their comment.
"""

# ------------------------------------------------------------------ window
WINDOW_TITLE = "FFBoard Twisty GUI"
WINDOW_GEOMETRY = "920x620"  # fixed "<width>x<height>" - window is not resizable, edit this value to change the size; widened so EFFECTS_WIDTH=1080 (see below) isn't clipped
WINDOW_SCALING = None  # Tk widget-scaling factor (e.g. 1.5 for HiDPI); None = leave at Tk's own default

# Shared style for every "DegreeButton.TButton"/"InvertToggle.TCheckbutton"
# button (main.py's App._setup_button_style()) - Save/Load, the 5 toolbar
# buttons, the 4 analog-calibration buttons, the degree/Center button, and
# the Invert toggle all use these, not coordinates but grouped here since
# they're referenced from multiple unrelated classes.
BUTTON_BG_COLOR = "#ffffff"        # rest-state background (DegreeButton's only state; InvertToggle's "off"/"!selected" state)
BUTTON_PRESSED_COLOR = "#c0c0c0"   # DegreeButton's "pressed" background; InvertToggle's "on"/"selected" background
BUTTON_HOVER_COLOR = "#e0e0e0"     # DegreeButton's "active"/hover background only - InvertToggle has no separate hover color
BUTTON_BORDERWIDTH = 1             # width of the border/relief shading, both styles
BUTTON_RELIEF = "raised"           # rest-state relief, both styles
BUTTON_RELIEF_PRESSED = "sunken"   # pressed ("pressed" state)/on ("selected" state) relief, both styles
BUTTON_BORDER_COLOR = "#c4c4c4"    # 8f8f8f outline color of the borrowed clam "Button.border" element, both styles -
                                    # was previously unset (no distinct outline, just the raised/sunken bevel);
                                    # this adds a visible ring around every button, tune/remove (set equal to
                                    # BUTTON_BG_COLOR) if an invisible border is preferred instead
BUTTON_SHADOW_LIGHT_COLOR = "#ffffff"  # top/left bevel-edge highlight of the raised look - not a real drop
                                        # shadow (ttk has none), just the same border element's edge shading;
                                        # size follows BUTTON_BORDERWIDTH, no separate size option exists
BUTTON_SHADOW_DARK_COLOR = "#989ba1"   # bottom/right bevel-edge shading of the raised look, pairs with
                                        # BUTTON_SHADOW_LIGHT_COLOR above

# Shared width (ttk's own character-count width=, not a coordinate) for
# every styled button, per user request ("nicht alle Buttons gleich
# breit") - sized to the single longest real button label in the app,
# "Release + Click" (15 characters, the two analog-calibration buttons),
# so nothing else needs truncating/wrapping room. Renders at 96px under
# DegreeButton.TButton (measured live via winfo_reqwidth()) - used below
# to recompute the pixel positions of button pairs/groups that need to
# stay centered as their shared width changes (the degree/Invert pair,
# the Advanced tab's Save/Load pair).
BUTTON_WIDTH_CHARS = len("Release + Click")
BUTTON_WIDTH_PX = 96  # size, not a coordinate - see BUTTON_WIDTH_CHARS comment

# ------------------------------------------------------------- InputsCanvas
# Value analog 1/2 gauges, their Min/Max calibration sliders, and the
# 10-button digital inputs - no longer a bordered "Inputs" box (removed per
# user request, see MAIN_CONTENT_* below): these coordinates are still
# relative to this block's own (now virtual) top-left corner, translated
# onto App.main_frame by InputsCanvas's base_x/base_y (see main.py's
# PlacedGroup).
INPUTS_HEIGHT = 200   # logical block height, not a coordinate - used below (MAIN_EFFECTS_BASE_Y) to stack the Effects block beneath this one

allInputsY = -12  # global vertical nudge added to every former-Inputs-block Y coordinate below (Y = n + allInputsY) - change this single value to shift the whole block up/down

# "Value analog 1" gauge (label above the sprite image, "0" readout below it)
# This is the Y-axis sprite animation (SpriteGauge(..., "Y")).
INPUTS_GAUGE1_LABEL_X = 110
INPUTS_GAUGE1_LABEL_Y = 10 + allInputsY
INPUTS_GAUGE1_IMAGE_X = 110
INPUTS_GAUGE1_IMAGE_Y = 28 + allInputsY
INPUTS_GAUGE1_Y_AXIS_SCALE = 1  # scale factor for the Y-axis animation sprite, not a coordinate
INPUTS_GAUGE1_NUMBER_X = 110
INPUTS_GAUGE1_NUMBER_Y = 162 + allInputsY

# "Value analog 2" gauge (mirrors Gauge 1 on the right side)
# This is the Z-axis sprite animation (SpriteGauge(..., "Z")).
INPUTS_GAUGE2_LABEL_X = 792
INPUTS_GAUGE2_LABEL_Y = 10 + allInputsY
INPUTS_GAUGE2_IMAGE_X = 792
INPUTS_GAUGE2_IMAGE_Y = 28 + allInputsY
INPUTS_GAUGE2_Z_AXIS_SCALE = 1  # scale factor for the Z-axis animation sprite, not a coordinate
INPUTS_GAUGE2_NUMBER_X = 792
INPUTS_GAUGE2_NUMBER_Y = 162 + allInputsY

# Min/Slider/Max calibration stack for apin adr=1 ("Value analog 1")
INPUTS_CONTROLS1_MIN_LABEL_X = 275
INPUTS_CONTROLS1_MIN_LABEL_Y = 10 + allInputsY
INPUTS_CONTROLS1_MIN_ENTRY_X = 325
INPUTS_CONTROLS1_MIN_ENTRY_Y = 10 + allInputsY
INPUTS_CONTROLS1_MIN_BUTTON_X = 300
INPUTS_CONTROLS1_MIN_BUTTON_Y = 35 + allInputsY
INPUTS_CONTROLS1_SLIDER_X = 230
INPUTS_CONTROLS1_SLIDER_Y = 10 + allInputsY
# "Invert" button (per user request - swaps which end of the physical
# travel reads as full/zero deflection, for games that read a trigger
# backwards) - same X column as Min/Max, sits in the gap between the
# "Release + Click" button above and the "Max:" label below.
INPUTS_CONTROLS1_INVERT_X = 300
INPUTS_CONTROLS1_INVERT_Y = 82 + allInputsY

INPUTS_CONTROLS1_MAX_LABEL_X = 275
INPUTS_CONTROLS1_MAX_LABEL_Y = 131 + allInputsY
INPUTS_CONTROLS1_MAX_ENTRY_X = 325
INPUTS_CONTROLS1_MAX_ENTRY_Y = 131 + allInputsY
INPUTS_CONTROLS1_MAX_BUTTON_X = 300
INPUTS_CONTROLS1_MAX_BUTTON_Y = 156 + allInputsY

# Min/Slider/Max calibration stack for apin adr=0 ("Value analog 2")
INPUTS_CONTROLS2_MIN_LABEL_X = 577
INPUTS_CONTROLS2_MIN_LABEL_Y = 10 + allInputsY
INPUTS_CONTROLS2_MIN_ENTRY_X = 627
INPUTS_CONTROLS2_MIN_ENTRY_Y = 10 + allInputsY
INPUTS_CONTROLS2_MIN_BUTTON_X = 602
INPUTS_CONTROLS2_MIN_BUTTON_Y = 35 + allInputsY
INPUTS_CONTROLS2_SLIDER_X = 672
INPUTS_CONTROLS2_SLIDER_Y = 10 + allInputsY

# "Invert" button - same idea as INPUTS_CONTROLS1_INVERT_X/_Y above.
INPUTS_CONTROLS2_INVERT_X = 602
INPUTS_CONTROLS2_INVERT_Y = 84 + allInputsY

INPUTS_CONTROLS2_MAX_LABEL_X = 577
INPUTS_CONTROLS2_MAX_LABEL_Y = 131 + allInputsY
INPUTS_CONTROLS2_MAX_ENTRY_X = 627
INPUTS_CONTROLS2_MAX_ENTRY_Y = 131 + allInputsY
INPUTS_CONTROLS2_MAX_BUTTON_X = 602
INPUTS_CONTROLS2_MAX_BUTTON_Y = 156 + allInputsY

INPUTS_SLIDER_LENGTH = 169  # RangeSlider drag-track length in px - a size, not a coordinate; shared by both sliders above

# 10-button digital inputs, sitting in the gap between the two slider stacks
INPUTS_BUTTONS_IMAGE_SCALE = 0.5  # scale factor for the button cluster/solo-lamp images, not a coordinate
INPUTS_BUTTONS_LEFT_CLUSTER_X = 405   # 4-button diamond cluster (E1-E4)
INPUTS_BUTTONS_LEFT_CLUSTER_Y = 25 + allInputsY
INPUTS_BUTTONS_LEFT_SOLO_X = 405      # "Wippe links" solo lamp, below the cluster
INPUTS_BUTTONS_LEFT_SOLO_Y = 130 + allInputsY
INPUTS_BUTTONS_RIGHT_CLUSTER_X = 495  # 4-button diamond cluster (E5-E8)
INPUTS_BUTTONS_RIGHT_CLUSTER_Y = 25 + allInputsY
INPUTS_BUTTONS_RIGHT_SOLO_X = 495     # "Wippe rechts" solo lamp, below the cluster
INPUTS_BUTTONS_RIGHT_SOLO_Y = 130 + allInputsY

# ------------------------------------------------------------ EffectsCanvas
# All FFB effect sliders stacked on the left, the X-axis degree gauge plus
# Range/degree/Invert/Center controls on the right, below the gauge image -
# no longer a bordered "Effects" box (removed per user request, see
# MAIN_CONTENT_* below): these coordinates are still relative to this
# block's own (now virtual) top-left corner, translated onto App.main_frame
# by EffectsCanvas's base_x/base_y (see main.py's PlacedGroup).

allEffectsY = -20  # global vertical nudge added to every former-Effects-block Y coordinate below (Y = n + allEffectsY) - change this single value to shift the whole block up/down

# Left column: 4 axis sliders + 4 global fx-gain sliders, stacked top to
# bottom. Range used to be the first row here (y=1) - moved below the gauge
# image per user request (see EFFECTS_SLIDER_RANGE_X/Y further down); that
# slot is deliberately left empty, not closed up by the rest of the list.
# Row order per user request: Power, Endstop Gain, Test Spring, Overall
# Gain, then the 4 Gain sliders - so the Y values below are out of order
# relative to the constant names (e.g. FXRATIO_Y > ESGAIN_Y/IDLESPRING_Y),
# each constant still names its own firmware command, only its Y moved.
#
# Overall Gain + the 4 Gain sliders below them form one group and Permanent
# damper/friction/inertia further below form another - each group is only
# marked by a thin separator line above it (EFFECTS_SLIDER_DIVIDER*), sized
# to the sliders' own width. The per-group/per-row caption texts these
# dividers used to introduce were removed again per user request; the
# normal 25px row-to-row gap stays widened to 31px only at these 2 group
# boundaries (left over from when the caption needed the extra room),
# everywhere else it's unchanged.
# Expo, placed above Power per user request ("packe das links über die
# vorhandenen, ich press das dann irgendwie zusammen") - same 22px row
# spacing as its neighbors below, not yet squeezed together with them
# (user said they'll adjust that themselves).
EFFECTS_SLIDER_POWER_X = 15
EFFECTS_SLIDER_POWER_Y = 3 + allEffectsY
EFFECTS_SLIDER_EXPO_X = 15
EFFECTS_SLIDER_EXPO_Y = 25 + allEffectsY
EFFECTS_SLIDER_ESGAIN_X = 15
EFFECTS_SLIDER_ESGAIN_Y = 47 + allEffectsY
EFFECTS_SLIDER_IDLESPRING_X = 15
EFFECTS_SLIDER_IDLESPRING_Y = 69 + allEffectsY

EFFECTS_SLIDER_DIVIDER_X = 15        # shared by both group-boundary separators below
EFFECTS_SLIDER_DIVIDER_WIDTH = 107 # size, not a coordinate - matches SLIDER_WIDTH (below), i.e. ends where the sliders end
EFFECTS_SLIDER_DIVIDER1_Y = 94 + allEffectsY      # between Test Spring and the "Multiplies Game Effects" group

EFFECTS_SLIDER_FXRATIO_X = 15
EFFECTS_SLIDER_FXRATIO_Y = 95 + allEffectsY
EFFECTS_SLIDER_SPRING_X = 15
EFFECTS_SLIDER_SPRING_Y = 117 + allEffectsY
EFFECTS_SLIDER_DAMPER_X = 15
EFFECTS_SLIDER_DAMPER_Y = 139 + allEffectsY
EFFECTS_SLIDER_FRICTION_X = 15
EFFECTS_SLIDER_FRICTION_Y = 161 + allEffectsY
EFFECTS_SLIDER_INERTIA_X = 15
EFFECTS_SLIDER_INERTIA_Y = 183 + allEffectsY

EFFECTS_SLIDER_DIVIDER2_Y = 208 + allEffectsY      # between the "Multiplies Game Effects" group and the "Adds to Game Effect" group

# The 3 always-on "permanent" effects (moved here from the Advanced Tuning
# tab's former LimitsPanel per user request - same LabeledSlider
# style/column as the sliders above, continuing the sequence). Speed limit
# was also moved here at first but then removed again - not needed.
EFFECTS_SLIDER_PERMDAMPER_X = 15
EFFECTS_SLIDER_PERMDAMPER_Y = 209 + allEffectsY
EFFECTS_SLIDER_PERMFRICTION_X = 15
EFFECTS_SLIDER_PERMFRICTION_Y = 231 + allEffectsY
EFFECTS_SLIDER_PERMINERTIA_X = 15
EFFECTS_SLIDER_PERMINERTIA_Y = 253 + allEffectsY

# "Save"/"Load" buttons below all left-column sliders, per user request -
# same design (style="DegreeButton.TButton", main.py) as the degree/Invert
# buttons above the Range slider on the right, using the shared
# BUTTON_WIDTH_PX (96px, see its own comment) like every other button now.
# Y = last slider's own Y (245-20=225, local) + SLIDER_HEIGHT (24) + 15px
# gap = 264. X starts at the same left edge as the slider column
# (EFFECTS_SLIDER_POWER_X, no anchor= given so place()'s default "nw" left-
# aligns it there); Load sits right after Save + a 10px gap.
EFFECTS_SAVE_LOAD_Y = 284 + allEffectsY
EFFECTS_SAVE_X = 48
EFFECTS_LOAD_X = 152  # = EFFECTS_SAVE_X + BUTTON_WIDTH_PX (96) + 10px gap

# Right column: X-axis degree gauge, then (below the image, per user
# request) Range, the degree readout, and the Invert/Center row. Shifted
# +100 from its original X (was 650) so the gap between the sliders and the
# gauge (now home to the force chart, see EFFECTS_FORCE_CHART_* below) has
# room without overlapping - see EFFECTS_WIDTH.
# This is the X-axis sprite animation (SpriteGauge(..., "X")).
EFFECTS_GAUGE_IMAGE_X = 710   # sprite image
EFFECTS_GAUGE_IMAGE_Y = -10 + allEffectsY
EFFECTS_GAUGE_X_AXIS_SCALE = 1  # scale factor for the X-axis animation sprite, not a coordinate - source PNGs (data/images/X) are now pre-scaled to the target 315x280 (originally 450x400, downscaled offline with LANCZOS to avoid resizing 256 frames at every startup - see data/images/X_original_450x400 backup), so no runtime resize is needed; rendered size stays 315x280, centered on EFFECTS_GAUGE_IMAGE_X so it spans x=592..908, y=0..280

# ">0.0°<" degree readout button (also triggers "Set center position") and
# the "Invert" toggle - both share BUTTON_WIDTH_PX (96px, see its own
# comment) since every button in the app was unified to one width per user
# request. 10px gap kept (not specified by the user, same as before). Total
# row = 96+10+96 = 202px, centered on local-X 707 (an arbitrary center point
# chosen when this row was first laid out) -> starts at 707-101 = 606 (left
# edge). Each X below is that widget's own anchor="n" (top-center) point,
# i.e. left edge + half its own width: degree button 606+48 = 654; Invert
# (606+96+10)+48 = 760. If BUTTON_WIDTH_PX ever changes, re-derive this
# whole block by hand - it will not follow automatically.
EFFECTS_GAUGE_DEGREE_X = 661
EFFECTS_GAUGE_DEGREE_Y = 284 + allEffectsY

EFFECTS_INVERT_X = 765
EFFECTS_INVERT_Y = 284 + allEffectsY

# Range - a Label+Entry only (LabeledEntry, no slider track - the RangeSlider
# bar was dropped per user request) sitting directly above the Center/Invert
# row, centered on that row's own horizontal center (606..808, see above ->
# center 707) rather than kept at the old full-width slider's position.
# Frame width = EFFECTS_SLIDER_RANGE_LABEL_W (38) + SLIDER_INNER_GAP (6) +
# SLIDER_READOUT_W (44) = 88 -> left edge = 707 - 88/2 = 663. Y keeps the old
# slider's Y (230) - already the same 34px gap above the button row (264)
# that separated them before, so the vertical spacing didn't need to change,
# only X (centering) and the dropped WIDTH (no more slider track to size).
EFFECTS_RANGE_ENTRY_X = 671
EFFECTS_RANGE_ENTRY_Y = 258 + allEffectsY
EFFECTS_SLIDER_RANGE_LABEL_W = 38  # this field's own label-column width (overrides the shared SLIDER_LABEL_W below), tightened to "Range"'s own measured text width (33px) + 5px margin per user request - brings the entry field closer to the label
EFFECTS_INVERT_ROW_HEIGHT = 23  # size, not a coordinate - shared explicit height (place()'s own height=, not each widget's natural sizing) for any button pairing a "DegreeButton.TButton" with an "InvertToggle.TCheckbutton" - the degree/Invert pair here, and InputsCanvas's Release/Press + Click buttons with their "Invert Output" checkbuttons - since the two styles render at slightly different natural heights (21px vs 23px, measured live) which otherwise leaves them visually misaligned/uneven

# Force chart: the always-on FFB-strength strip chart. Formerly a whole
# standalone "Force" section (ForceCanvas, now removed) with a "FFB
# Strength" caption, a numeric value, a "Graph" show/hide checkbox and the
# Voltage/Temp readouts alongside it - all of those have since moved out
# (the numeric value + caption and the readouts into ReadoutBar in main.py,
# own full-width row below App's toolbar per user request; the checkbox
# removed outright per user request, so the chart is simply always shown
# now) - this chart is what's left. It used to sit below that block too (as
# one wide, flat row) but was squeezed, per user request, into the gap
# between the sliders and the gauge instead - see EFFECTS_FORCE_CHART_*
# below.
#
# Squeezed into the gap between the sliders and the gauge image (which
# starts at x=592, see EFFECTS_GAUGE_IMAGE_X above) - the chart's drawing
# already runs newest-sample-at-bottom vertically with horizontal +/-100%
# deflection (strip_chart.py), so a tall, narrow box here actually suits it
# better than the old wide, flat one. Full height of the slider column:
# EFFECTS_SLIDER_POWER_Y (top) to EFFECTS_SLIDER_PERMINERTIA_Y +
# SLIDER_HEIGHT (bottom) = 25 to 287+24=311.
#
# X is a one-time-computed fixed number, not a formula, per user request
# (InputsCanvas and EffectsCanvas are deliberately not to be linked): the
# chart's own trace is drawn centered on its own canvas width
# (strip_chart.py: cx = winfo_width()/2), so its visible line sits at
# EFFECTS_FORCE_CHART_X + EFFECTS_FORCE_CHART_WIDTH/2. Chosen so that lands
# on 450 - the midpoint between the two Inputs button-diamond clusters,
# (INPUTS_BUTTONS_LEFT_CLUSTER_X + INPUTS_BUTTONS_RIGHT_CLUSTER_X) / 2 =
# (405 + 495) / 2 = 450, valid since both blocks share the same base_x
# (MAIN_CONTENT_X): 450 - EFFECTS_FORCE_CHART_WIDTH/2 (95) = 355. If the
# button clusters ever move, re-derive this by hand - it will not follow
# automatically.
EFFECTS_FORCE_CHART_X = 351
EFFECTS_FORCE_CHART_Y = 25 + allEffectsY
EFFECTS_FORCE_CHART_WIDTH = 190    # size, not a coordinate - leaves a gap on both sides before the sliders (x=379) and the gauge (x=592)
EFFECTS_FORCE_CHART_HEIGHT = 286   # size, not a coordinate - matches the slider column's full height (311-25)

# ------------------------------------------------------------------ ReadoutBar
# ReadoutBar (main.py): the VCC/L1/L2/L3/FFB row below the toolbar's Port
# row. Each of the 5 modules is one combined "Label: value" tk/ttk.Label
# (e.g. "VCC: 10.3 V", "L1: 22.0 °C") place()d at its own explicit X/Y
# instead of pack()ed left-to-right - per user request, so any module can
# be freely repositioned just by editing its X/Y here, the same way every
# other element in this app is positioned. WIDTH_PX per module reserves a
# fixed pixel column (label anchor="w") so the row doesn't reflow as a live
# value's text length changes (e.g. "9.9"->"60.0", "-5.0"->"40.0"). L1/L2/L3
# each get their own X/Y/WIDTH_PX (not shared) so they can be rearranged
# independently of each other.
#
# Starting positions below reproduce the previous pack()-based row exactly
# (VCC, L1, L2, L3, FFB left-to-right, same worst-case widths that row was
# sized against - "VCC: 60.0 V"=60px, "L1: -99.9 °C"=60px x3,
# "FFB: +100 %"=64px, 5px gap between) - move any X/Y from here to
# rearrange, nothing else needs to change.
#
# READOUTBAR_WIDTH_PX/HEIGHT_PX size ReadoutBar's own Frame explicitly -
# required because place()d children (unlike pack()/grid()) never
# propagate their size up to the parent, so without this the frame would
# collapse to ~1x1px and none of the 5 modules would be visible.
READOUTBAR_WIDTH_PX = 330
READOUTBAR_HEIGHT_PX = 20

READOUTBAR_VCC_X = 0
READOUTBAR_VCC_Y = 0
READOUTBAR_VCC_WIDTH_PX = 64

READOUTBAR_L1_X = 65
READOUTBAR_L1_Y = 0
READOUTBAR_L1_WIDTH_PX = 60

READOUTBAR_L2_X = 130
READOUTBAR_L2_Y = 0
READOUTBAR_L2_WIDTH_PX = 60

READOUTBAR_L3_X = 195
READOUTBAR_L3_Y = 0
READOUTBAR_L3_WIDTH_PX = 60

READOUTBAR_FFB_X = 260
READOUTBAR_FFB_Y = 0
READOUTBAR_FFB_WIDTH_PX = 70

# -------------------------------------------------------------- Main layout
# The "Inputs" and "Effects" blocks above used to sit in their own bordered
# ttk.LabelFrame boxes ("Inputs"/"Effects" titles), each with an inner
# Canvas/Frame that existed only to give their children a place()
# coordinate origin - both boxes were removed per user request, and their
# children are now placed directly onto App.main_frame instead (see
# App._build_ui() and main.py's PlacedGroup). Every INPUTS_*/EFFECTS_*
# coordinate above is unchanged and still relative to that block's own (now
# virtual) top-left corner - these constants are the only thing that
# translates each block's origin into main_frame's shared coordinate space,
# so the two blocks keep exactly the same pixel arrangement relative to
# each other as before, just without the surrounding box.
MAIN_CONTENT_X = 8        # shared left margin for both blocks - lines up with the toolbar's own "Port:" left edge (see App._build_ui())
MAIN_CONTENT_TOP_Y = 20   # gap between the toolbar and the first content (Accelerate block) - a starting guess, check against a screenshot
MAIN_SECTION_GAP_Y = 20   # gap between the bottom of the Inputs block and the top of the Effects block
MAIN_EFFECTS_BASE_Y = MAIN_CONTENT_TOP_Y + INPUTS_HEIGHT + MAIN_SECTION_GAP_Y  # Effects block's own (0,0), in main_frame's coordinate space

# --------------------------------------------------------- Advanced Tuning
# "Advanced Tuning" tab: just FxTuningPanel (5 response-curve graphs) now -
# Axis info (Pos/Speed/Accel) and Limits/Permanent effects (Speed limit +
# Permanent damper/friction/inertia) moved to the Main tab's EffectsCanvas
# per user request (EFFECTS_SLIDER_SPEEDLIMIT_*/PERM*, above); Axis info
# was removed outright (no longer shown anywhere).
#
# FxTuningPanel no longer sits in its own bordered "Effect response curves"
# box (removed per user request, same treatment as Main's "Inputs"/
# "Effects" boxes) - its content is placed directly onto AdvancedTuningTab
# instead, offset by these two constants (mirrors MAIN_CONTENT_X/TOP_Y).
# Every ADVANCED_FX_* coordinate below is unchanged and still relative to
# the panel's own (now virtual) top-left corner.
ADVANCED_CONTENT_X = 8      # left margin - matches MAIN_CONTENT_X for a consistent look across both pages
ADVANCED_CONTENT_TOP_Y = 20 # gap between the toolbar and the first content (row 1 titles) - matches MAIN_CONTENT_TOP_Y
#
# FxTuningPanel's cards (Spring/Inertia/Expo/Damper/Friction response
# curves, plus the Effect filter profile card) match the official
# OpenFFBoard-Configurator's "Advanced ffb tuning" dialog (res/
# effects_tuning.ui) content-wise - each card's own internal element order
# copied from that file's per-group gridLayout (Graph -> Gain slider ->
# [Smooth, Friction only] -> [Freq/Q, all but Spring]), profile card from
# the same file's QFrame "frame" (filter profile + Restore Default - its
# "Read metrics on axis" axis-selector left out, since Twisty is hardcoded
# single-axis everywhere else in this GUI). Expo (a separate dialog in the
# original, res/expo.ui) is merged into the same panel per user request,
# own internal order copied from that file (Graph -> Slider ->
# Exponent/Reset row). Unlike the reference, every card below has its own
# independent (X, Y, WIDTH, HEIGHT) - see the ADVANCED_CARD_*_X/_Y/_WIDTH/
# _HEIGHT block below - instead of hanging off a shared row/column grid, so
# any one card can be repositioned or resized without affecting the others.
# The chart/slider content inside every card stays a fixed pixel size
# regardless of its card's own width/height (per user request) - resizing a
# card only changes its border box, leaving more/less empty space around
# the (unchanged) content, or clipping it if a card is made too small.
ADVANCED_CHART_WIDTH = 300   # ResponseCurveChart size, not a coordinate - fallback default when a chart is built without an explicit width/height (all 5 Advanced graphs now pass ADVANCED_CARD_CHART_WIDTH/HEIGHT explicitly instead, see below)
ADVANCED_CHART_HEIGHT = 140  # size, not a coordinate
ADVANCED_CHART_BG = "#ffffff"  # shared chart background - was ttk.Style().lookup("TFrame", "background") (followed the OS theme, which turned out dark gray under some Windows themes) - fixed to plain white per user request

# --- FxTuningPanel ---

# All 6 cards (Spring/Inertia/Expo/Damper/Friction response curves, plus the
# Effect filter profile card) share the same bordered "card" look (relief/
# border width/label column) and the same fixed-size content (chart/slider
# pixel dimensions, below) - only each card's own border box (X, Y, WIDTH,
# HEIGHT) is independent, see the per-card block further down.
ADVANCED_CARD_PADDING = 10       # size, not a coordinate - gap between a card's border and its contents (chart/slider/etc.) on every side, so nothing touches the border
ADVANCED_CARD_CHART_WIDTH = 260  # size, not a coordinate - fixed content width for every card's chart/slider, independent of that card's own WIDTH (per user request - a card's own size only changes its border box, not its content)
ADVANCED_CARD_CHART_HEIGHT = 120 # size, not a coordinate - fixed content height, same idea
ADVANCED_CARD_RELIEF = "groove"
ADVANCED_CARD_BORDERWIDTH = 2
ADVANCED_CARD_LABEL_W = 47  # size, not a coordinate - narrow column for the short "Gain"/"Expo"/"Smooth" labels (measured: "Smooth" is the widest at 42px), overrides the shared SLIDER_LABEL_W to pull entry+slider much closer to the label
# No fixed border-fill color constant - a hardcoded hex here (an earlier
# attempt used "#d9d9d9") read as noticeably darker than the rest of the
# GUI, so every card's border bg is instead fetched live via
# ttk.Style().lookup("TFrame", "background") at the point of use in
# main.py (same pattern as EffectsCanvas's force chart background) -
# guaranteed to match the ordinary window background exactly, under
# whatever theme is active.

# Each card's own border box: top-left corner (X, Y) plus its own WIDTH/
# HEIGHT (per user request - previously WIDTH was shared by all 6 and
# HEIGHT came from one of two shared "TALL"/"FRICTION" presets; now every
# card is fully independent). Its title (TITLE_TO_BORDER_DY above the
# border) and every widget inside (chart/slider/etc., placed at a fixed
# DY/DX offset from this same (X, Y) origin, see below) move with it as one
# block when (X, Y) changes. The chart/slider content itself does NOT
# resize with WIDTH/HEIGHT - it stays at ADVANCED_CARD_CHART_WIDTH/HEIGHT
# above; making a card smaller than its content will clip it, making it
# bigger just leaves empty space. Starting values below reproduce the
# layout as last arranged (3 columns x 2 rows, 300px apart horizontally,
# 245px apart vertically; 280 wide; 208 tall for Spring/Damper/Expo, 242
# tall for Inertia/Friction/Profile).
ADVANCED_CARD_TITLE_TO_BORDER_DY = 25  # was a 20px title-to-chart gap; +5px per user request

ADVANCED_CARD_EXPO_X = 10
ADVANCED_CARD_EXPO_Y = 33
ADVANCED_CARD_EXPO_WIDTH = 280
ADVANCED_CARD_EXPO_HEIGHT = 208

ADVANCED_CARD_SPRING_X = 310
ADVANCED_CARD_SPRING_Y = 33
ADVANCED_CARD_SPRING_WIDTH = 280
ADVANCED_CARD_SPRING_HEIGHT = 208

ADVANCED_CARD_DAMPER_X = 610
ADVANCED_CARD_DAMPER_Y = 33
ADVANCED_CARD_DAMPER_WIDTH = 280
ADVANCED_CARD_DAMPER_HEIGHT = 208

ADVANCED_PROFILE_FRAME_X = 10
ADVANCED_PROFILE_FRAME_Y = 278
ADVANCED_PROFILE_FRAME_WIDTH = 280
ADVANCED_PROFILE_FRAME_HEIGHT = 242

ADVANCED_CARD_FRICTION_X = 310
ADVANCED_CARD_FRICTION_Y = 278
ADVANCED_CARD_FRICTION_WIDTH = 280
ADVANCED_CARD_FRICTION_HEIGHT = 242

ADVANCED_CARD_INERTIA_X = 610
ADVANCED_CARD_INERTIA_Y = 278
ADVANCED_CARD_INERTIA_WIDTH = 280
ADVANCED_CARD_INERTIA_HEIGHT = 242


# Vertical offsets from a card's own Y (border top) to its internal rows -
# identical across every card that has that row, since the internal
# chart/gain/freq geometry is the same regardless of which card it's in.
ADVANCED_CARD_CHART_DY = 10            # = CARD_PADDING
ADVANCED_CARD_GAIN_DY = 140            # = CHART_DY + CARD_CHART_HEIGHT + CARD_PADDING - Spring/Inertia/Damper/Friction's Gain slider, also Expo's own -127..127 slider (same row slot)
ADVANCED_CARD_FREQ_DY = 174            # = GAIN_DY + SLIDER_HEIGHT(24) + CARD_PADDING - Inertia/Damper's Freq/Q row, also Expo's Exponent label+value+Reset row (same row slot)
ADVANCED_CARD_FRICTION_SMOOTH_DY = 174 # same row slot as FREQ_DY - Friction has its Smooth slider here instead of Freq/Q
ADVANCED_CARD_FRICTION_FREQ_DY = 208   # = FRICTION_SMOOTH_DY + SLIDER_HEIGHT(24) + CARD_PADDING - Friction's own Freq/Q row, after Smooth

ADVANCED_FX_FREQ_LABEL_DX = 0     # offsets from the card's inner content X (card_x + CARD_PADDING), not absolute coordinates
ADVANCED_FX_FREQ_SPIN_DX = 40
ADVANCED_FX_Q_LABEL_DX = 150
ADVANCED_FX_Q_SPIN_DX = 175

ADVANCED_FX_EXPO_EXPONENT_LABEL_DX = 0   # offsets from the Expo card's inner content X, not absolute coordinates
ADVANCED_FX_EXPO_EXPONENT_VALUE_DX = 65
ADVANCED_FX_EXPO_RESET_BUTTON_DX = 130

# Effect filter profile card - its own bordered card (per user request) at
# ADVANCED_PROFILE_FRAME_X/_Y/_WIDTH/_HEIGHT above, title "Effect Filter
# Profile" above the border like every other card (see
# ADVANCED_CARD_TITLE_TO_BORDER_DY). Interior, top to bottom: a read-only
# glossary table explaining Exponential/Gain/Freq/Q/Smooth, then a
# Default/Custom segmented toggle (2 buttons, no dropdown - see
# ADVANCED_PROFILE_TOGGLE_Y below), then Save/Load (own X/Y, see
# ADVANCED_PROFILE_SAVE_X/_LOAD_X/_SAVE_LOAD_Y further down).

# Glossary text - a single read-only tk.Text (state="disabled"), not a
# table anymore (per user request - plain flowing "Term: Explanation"
# lines instead of column-aligned rows). No fixed font constants either -
# main.py sets font="TkDefaultFont" directly, the same named font every
# ttk.Label/Button in the GUI already uses, so this text matches the rest
# of the interface instead of having its own style.
ADVANCED_PROFILE_TABLE_X = 20                # = card_x(10) + CARD_PADDING(10)
ADVANCED_PROFILE_TABLE_Y = 288               # = card_y(278) + CARD_PADDING(10)
ADVANCED_PROFILE_TABLE_WIDTH = 260           # = card interior width, same as ADVANCED_CARD_CHART_WIDTH
ADVANCED_PROFILE_TABLE_HEIGHT = 153          # fits between the table's own Y and ADVANCED_PROFILE_TOGGLE_Y below, with a 10px gap to spare
# No fixed background-color constant (per user request: the table should
# blend into the ordinary GUI background, not stand out as its own color)
# - main.py fetches it live via ttk.Style().lookup("TFrame", "background")
# instead, same as every card border Frame's own bg (see ADVANCED_CARD_
# RELIEF's comment above for why a hardcoded hex isn't used for this).

# Default/Custom segmented toggle (per user request, replacing the
# dropdown - see main.py's ProfileToggle.TRadiobutton) - own X/Y/size per
# button per user request, independent of the Save/Load buttons below
# (not shared with BUTTON_WIDTH_PX/EFFECTS_INVERT_ROW_HEIGHT either, so
# resizing this pair doesn't affect any other button in the app).
#
# WIDTH is a pixel width applied via place()'s own width= (not a ttk
# char-count width=, unlike every other button in the app) - measured
# live that ProfileToggle.TRadiobutton at the same char-width as
# DegreeButton.TButton still renders 2px wider (98 vs 96px, borrowed
# "clam" Button.border pads a Radiobutton slightly differently than a
# Button), so an exact pixel override is the only way to make the two
# pairs truly the same width instead of just approximately close - which
# is also why X must equal ADVANCED_PROFILE_SAVE_X/_LOAD_X exactly for the
# pair to be centered under Save/Load, not offset by half that 2px gap.
ADVANCED_PROFILE_DEFAULT_X = 48              # = ADVANCED_PROFILE_SAVE_X, so the pair lines up exactly under Save
ADVANCED_PROFILE_CUSTOM_X = 152              # = ADVANCED_PROFILE_LOAD_X, so the pair lines up exactly under Load
ADVANCED_PROFILE_TOGGLE_Y = 451              # = ADVANCED_PROFILE_SAVE_LOAD_Y(484) - ADVANCED_PROFILE_TOGGLE_HEIGHT(23) - 10px gap
ADVANCED_PROFILE_TOGGLE_WIDTH_PX = 96        # = BUTTON_WIDTH_PX, own constant - place() pixel width, not ttk char-width
ADVANCED_PROFILE_TOGGLE_HEIGHT = 23          # place() height= (pixels) - own constant, was EFFECTS_INVERT_ROW_HEIGHT

# Save/Load buttons under the Effect filter profile card - a copy of the
# Main tab's pair (see EFFECTS_SAVE_X/EFFECTS_LOAD_X/EFFECTS_SAVE_LOAD_Y).
#
# Previous values, centered on the profile card itself (anchor="center" in
# main.py) - kept here commented out per user request, not deleted, in
# case this approach is preferred again later:
ADVANCED_PROFILE_SAVE_X = 98
ADVANCED_PROFILE_LOAD_X = 202
ADVANCED_PROFILE_SAVE_LOAD_Y = 514 + allEffectsY
#
# Current approach (per user request): positioned so the buttons land on
# the exact same on-screen spot as the Main tab's Save/Load pair when
# switching tabs, even though the two tabs' own content origins differ
# (MAIN_CONTENT_X/MAIN_EFFECTS_BASE_Y vs ADVANCED_CONTENT_X/_TOP_Y - both
# tab frames occupy the identical on-screen rect, see AdvancedTuningTab/
# App._build_ui()'s "pages" grid). Anchor in main.py is now the default
# top-left (no anchor="center"), matching the Main tab's Save/Load anchor,
# with the same explicit height (EFFECTS_INVERT_ROW_HEIGHT) - so identical
# absolute X/Y here reproduces an identical rendered rectangle, not just a
# matching corner. Expressed as formulas (not literal numbers) so this
# stays correct automatically if the Main tab's Save/Load position, or
# either page's content origin, ever changes.
ADVANCED_PROFILE_SAVE_X = MAIN_CONTENT_X + EFFECTS_SAVE_X - ADVANCED_CONTENT_X
ADVANCED_PROFILE_LOAD_X = MAIN_CONTENT_X + EFFECTS_LOAD_X - ADVANCED_CONTENT_X
ADVANCED_PROFILE_SAVE_LOAD_Y = MAIN_EFFECTS_BASE_Y + EFFECTS_SAVE_LOAD_Y - ADVANCED_CONTENT_TOP_Y


# ------------------------------------------------------------- LabeledSlider
# Internal layout of one slider widget (label -> entry -> slider -> optional
# note), relative to the widget's own top-left corner, not the canvas. Any
# unit (e.g. "%", "°") is folded directly into the entry text - there is no
# separate unit-label column. WIDTH/HEIGHT/LABEL_W/READOUT_W/NOTE_W are
# sizes, not coordinates.
SLIDER_WIDTH = 335
SLIDER_HEIGHT = 24
SLIDER_LABEL_W = 108  # narrowed from 130 per user request (entry sat too far from short labels like "Power") - just fits the widest label ("Permanent Damper", 103px at TkDefaultFont) + a few px margin
SLIDER_READOUT_W = 44  # fits "1600" (the largest value shown, Spring Gain at raw=255) + 10px margin each side
SLIDER_INNER_GAP = 6
SLIDER_NOTE_W = 175  # optional caption column after the slider (e.g. "Multiplies Game Effect") - measured: longest current text ("Active Only Without Game FFB") is 163px at TkDefaultFont, size not a coordinate

# ------------------------------------------------------------------ HSlider
# Single-thumb horizontal value slider (a tk.Canvas that draws its own
# track/thumb, same drawn look as RangeSlider below) - used inside
# LabeledSlider for the 9 EffectsCanvas sliders. All sizes, not coordinates.
HSLIDER_THUMB_HALF_ALONG = 4   # thumb rectangle half-width (along the track)
HSLIDER_THUMB_HALF_ACROSS = 7  # thumb rectangle half-height (perpendicular to the track)
HSLIDER_TRACK_W = 3            # track/highlight line width
HSLIDER_PAD = 8                # left/right padding before the drag range starts

# --------------------------------------------------------------- RangeSlider
# Two-thumb vertical Min/Max calibration slider (a single tk.Canvas that
# draws its own track/thumbs/live-marker) - all sizes, not coordinates.
RANGESLIDER_THICKNESS = 26      # canvas width (the track runs top-to-bottom through its center)
RANGESLIDER_THUMB_HALF_ACROSS = 7  # thumb rectangle half-width (perpendicular to the track)
RANGESLIDER_THUMB_HALF_ALONG = 4   # thumb rectangle half-height (along the track)
RANGESLIDER_TRACK_W = 3            # track/highlight line width
RANGESLIDER_PAD = 8                # top/bottom padding before the drag range starts
