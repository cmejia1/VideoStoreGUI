"""
program: videostoreGUI.py
author: chris 7/18/2023

GUI based version of the vidostore project from chapter 2

NOTE: the file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# other imports go here

# class header 
class VideoStore(EasyFrame):
	# definition of our class constructor method
	def __init__(self):
		EasyFrame.__init__(self, title = "Five Star Video", width = 300, height = 180, resizable = False, background = "lightyellow")
		self.normalFont = Font(family = "Tahoma", size = 16)

		# add the various components to the window
		self.addLabel(text = "Five Star Video", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "darkred", foreground = "lightyellow", font = Font(family = "Arial", size = 26))
		self.addLabel(text = "New Rentals : $3.00\n Old Rentals: $2.00", row = 1, column = 0, columnspan = 2, sticky = "NSEW", background = "lightyellow", font = self.normalFont)
		self.addLabel(text = "# of New Rentals:", row = 2, column = 0, sticky = "NE", background = "lightyellow", font = self.normalFont)
		self.newRentals = self.addIntegerField(value = 0, row = 2, column = 0, sticky = "NW", width = 4)
		self.addLabel(text = "# of Old Rentals", row = 3, column = 0, sticky = "NE", background = "lightyellow", font = self .normalFont)
		self.oldRentals = self.addIntegerField(value = 0, row = 3, column = 1, sticky = "NW", width = 4)

		self.button = self.addButton(text = "Calculate Total", row = 4, column = 0, columnspan = 2, command = self.calculate)
		self.addLabel(text = "The total for the order is: ", row = 5, column = 0, sticky = "NE", background = "darkred", foreground = "white", font = self.normalFont)
		self.total = self.addFloatField(value = 0.0, row = 5, column = 1, sticky = "NW", precision = 2, state = "readonly", width = 10)

	# definition of the calculate() function
	def calculate(self):
		# grab the user input from the GUI window
		new = self.newRentals.getNumber()
		old = self.oldRentals.getNumber()

		# processing phase 
		result = (new * 3.00) + (old * 2.00)

		# output phase
		self.total.setNumber(result)

# definition of the main() method
def main():
	VideoStore().mainloop()

# global call to main() for program entry
if __name__ == '__main__':
	main()