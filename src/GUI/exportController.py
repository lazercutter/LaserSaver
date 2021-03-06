from appUtils import *
from exportView import ExportView


class ExportController:
	def __init__(self, master):
		''' The export controller not much here just sets up the export view with the json data

			Args:
				master(Tk object): The toplevel widget of Tk which is the main window of an application
		'''
		self.master = master
		jsonfile = open('final.json')
		json = jsonfile.read()
		self.view = ExportView(master, self ,json)
		self.view.pack(expand=YES,fill=BOTH)
		jsonfile.close()