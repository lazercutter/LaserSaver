#!/usr/bin/python
from appUtils import *
from homeController import HomeController

class App:
	def __init__(self, master):
		''' Setting the viewController to HomeViewController
		    
		    Args:
		    	master(Tk object): The top level widget of Tk which is the main window of an application
		'''
		HomeController(master)


#Initializing GUI window
root = Tk()
root.wm_title("LaserSaver")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
#root.geometry('{}x{}'.format(640, 480))
root.minsize(530, 430)
app = App(root)
root.mainloop()