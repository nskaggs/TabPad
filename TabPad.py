#!/usr/bin/python3

# Run command below to install dependencies in Ubuntu.
# sudo apt install python3-pyqt5 xdotool

# Launch TabPad by running command below.
# python3 TabPad.py

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
import subprocess
from TabPadConfig import *

# todo
# implement individual button sizes in dict
# support for fullscreen games
# diagonal movement support
# done: implement button transparency

class TabPad(QWidget):
	def __init__(self):
		super(TabPad, self).__init__()
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint |
							QtCore.Qt.FramelessWindowHint |
							QtCore.Qt.X11BypassWindowManagerHint
							)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.stl = "QWidget {background-color:rgba(0, 0, 0, 0%);border-width:" \
		+ str(button_border_size)  + "px;border-style:solid;border-radius:" \
		+ str(button_border_radius) + "px;border-color:" + str(button_border_color) \
		+ ";}"
		self.setStyleSheet(self.stl)
		self.initUI()

	def initUI(self):
		for k, v in button_layout.items():
			self.createandmove(k, v[0], v[1], v[2], v[3])
		self.createandmove("Quit", 35, 80, [], "#808080")
		self.setGeometry(overlay_x_position, overlay_y_position, overlay_width, overlay_height)
		self.setWindowTitle('TabPad')
		self.show()

	def createandmove(self, label, xper, yper, command, color):
		self.qbtn = QPushButton(label, self)
		self.clr = "background-color:rgba(" + str(self.hextorgb(color)) + "," \
		+ str(button_opacity) + '%);'
		self.qbtn.setStyleSheet(self.clr)
		self.qbtn.clicked.connect(self.keyhandler(label))
		if button_width == 0 and button_height == 0:
			self.qbtn.resize(self.qbtn.sizeHint())
		else:
			self.qbtn.resize(button_width, button_height)
		xpos, ypos = self.percentconvertor(xper, yper)
		self.qbtn.move(xpos, ypos)

	def percentconvertor(self, xpercent, ypercent):
		xpos = int(round((overlay_width * xpercent)/100))
		ypos = int(round((overlay_height * ypercent)/100))
		return xpos, ypos

	def keyhandler(self, lbl):
		def processinput():
			if lbl == "Quit":
				QtCore.QCoreApplication.instance().quit()
				sys.exit(1)
			else:
				cmnd = button_layout[lbl][2]
				subprocess.Popen(cmnd, stdout=subprocess.PIPE)
		return processinput

	def hextorgb(self, hexcolor):
		h = hexcolor.strip('#')
		h = (tuple(int(h[i:i+2], 16) for i in (0, 2 ,4)))
		return (str(h[0]) + "," + str(h[1]) + "," + str(h[2]))

def main():
	app = QApplication(sys.argv)
	ex = TabPad()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()