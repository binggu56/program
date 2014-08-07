class Rectangle(object):
	def __init__(self,width,height):
		self.height = height
		self.width = width

	def _area(self):
		return self.width*self.height
	
	area = property(fget=_area)

#	def getWidth(self):
#		return self.width
#
#	def setWidth(self,width):
#		self.width = width
#
#	def getHeight(self):
#			return self.height
#	
#	def setHeight(self,height):
#		self.height = height
#	
#	def area(self):
#		return self.getWidth()*self.getHeight()


rect = Rectangle(50,10)
print(rect.area)
		
