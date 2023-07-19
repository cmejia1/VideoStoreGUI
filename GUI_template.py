"""
program: GUI_template.py
author: chris 7/10/2023

template for all GUI-based examples for chapter 8

NOTE: the file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!
"""

from breezypythongui import EasyFrame
# other imports go here

# class header 
class ApplicationName(EasyFrame):
	# definition of our class constructor method
	def __init__(self):
		EasyFrame.__init__(self)

# definition of the main() method
def main():
	ApplicationName().mainloop()

# global call to main() for program entry
if __name__ == '__main__':
	main()