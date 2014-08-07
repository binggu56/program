# -*- coding: utf-8 -*-
import sys,cmd
from cdctools import *

class bak(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self)
		self.CDROM = '/media/cdrom()'
		self.CDDIR = 'cdc/'
		self.prompt=">>>"
		self.intro = '''PyCDC0.5 Instructions:
dir dir_name 		# default cdc
walk file_name 		# default *.cdc
find keywords		# keywords
?			# find
EOF			# quit
	'''
	def help_EOF(self):
		print("quit")
	def do_EOF(self,line):
		sys.exit()

	def help_walk(self):
		print("walk cd and export into *.cdc")
	def do_walk(self,filename):
		if filename == "":filename == raw_input("cdc filename:")
		print("save to %s" %(filename))
		cdWalker(self.CDROM,self.CDDIR+filename)

	def help_dir(self):
		print("dir_name:")
	def do_dir(self,pathname):
		if pathname == "":pathname= raw_input("Enter dir_name:") 
		self.CDDIR = pathname
		print("Dir_name: '%s'; Default:'%s'" %(pathname,self.CDDIR))
	def help_find(self):
		print("keyword")
	def do_find(self,keyword):
		if keyword == "":keyword=raw_input("Enter keyword")
		print("keyword: '%s'" %(keyword))
if __name__=='__main__':
	backup = bak()
	bak.cmdloop()
#	CDROM = '/media/cdrom()'
#	cdWalker(CDROM,"cdc/cdctools.cdc")
