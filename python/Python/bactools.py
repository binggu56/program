# -*- coding: utf-8 -*-
import sys, cmd
class bak(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self) # initialize the base class
	def help_EOF(self):
		print("Quit the program")
	def do_EOF(self, line):
		sys.exit()

	def help_file(self):
		print("The filename ")
	def do_file(self,filename):
		if filename == "":filename = raw_input("输入cdc 文件名:: ")
		print "扫描光盘内容保存到:'%s'" % filename

	def help_dir(self):
		print "指定保存/搜索目录"
	def do_dir(self, pathname):
		if pathname == "": pathname = raw_input("输入指定保存/搜索目录: ")

	def help_find(self):
		print "搜索关键词"
	def do_find(self, keyword):
		if keyword == "": keyword = raw_input("输入搜索关键字: ")
		print "搜索关键词:'%s'" % keyword
if __name__ == '__main__': # this way the module can be
	cdc = PyCDC() # imported by other programs as well
	cdc.cmdloop()
