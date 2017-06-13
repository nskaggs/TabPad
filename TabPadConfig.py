#!/usr/bin/python3

# Change Settings in this file

# Position of transparent overlay window in x and y coordinates
overlay_x_position = 0
overlay_y_position = 300

# Width and height of transparent overlay window
overlay_width = 1024
overlay_height = 400

# Set both button_width and button_height to 0 to auto-resize (not recommended).
button_width = 70
button_height = 70

# Change button geometry and color
button_border_size = 1
button_border_radius = 25
button_border_color = "#555555"

# Opacity of buttons in percentage (100 is fully opaque).

button_opacity = 100

# The dictionary below defines your gamepad layout and properties.
# The first value is identification label for your button (before colon).
# The next two numbers are percentages defining position of a button.
# (Depends on overlay width and height mentioned above.)
# E.g. 6,5 will postion a button horizontally at 6% of total width value.
# And vertically at 5% of total height value.
# The second value in square brackets defines command to be executed on button press.
# You can read more about xdotool on Internet.
# The last value defines button color (use only hex color values).

# Creating your own buttons is super easy. Just append your own layout entry in dictionary below.
# Make sure you do it in the format shown below to prevent app crashes.
# Don't forget to put a comma after each entry, except for the last one.

button_layout = {
	"L1": (6, 5, ["xdotool", "key", "q"], "#ff0000"),
	"L2": (14, 5, ["xdotool", "key", "w"], "#ff0000"),
	"R1": (79, 5, ["xdotool", "key", "o"], "#ff0000"),
	"R2": (87, 5, ["xdotool", "key", "p"], "#ff0000"),
	"Up": (10, 53, ["xdotool", "key", "Up"], "#ffffff"),
	"Right": (18, 63, ["xdotool", "key", "Right"], "#ffffff"),
	"Down": (10, 73, ["xdotool", "key", "Down"], "#ffffff"),
	"Left": (2, 63, ["xdotool", "key", "Left"], "#ffffff"),
	"3": (83, 53, ["xdotool", "key", "i"], "#008000"),
	"2": (91, 63, ["xdotool", "key", "l"], "#ffff00"),
	"1": (83, 73, ["xdotool", "key", "k"], "#0000ff"),
	"4": (75, 63, ["xdotool", "key", "j"], "#ffc0cb"),
	"Start": (45, 80, ["xdotool", "key", "v"], "#ffa500"),
	"Select": (55, 80, ["xdotool", "key", "n"], "#800080")
}