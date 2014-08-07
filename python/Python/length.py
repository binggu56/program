class Length(object):
	convert = dict(mi=621.371e-6, miles=621.371e-6, mile=621.371e-6, yd=1.094, yards=1.094, yard=1.094,
                       ft=3.281, feet=3.281, foot=3.281,
                       inches=39.37, inch=39.37,
                       mm=1000, millimeter=1000, millimeters=1000,
                       millimetre=1000, millimetres=1000,
                       cm=100, centimeter=100, centimeters=100,
                       centimetre=100, centimetres=100,
                       m=1.0, meter=1.0, meters=1.0, metre=1.0, metres=1.0,
                       km=0.001, kilometer=0.001, kilometers=0.001,
                       kilometre=0.001, kilometres=0.001)	
	convert["in"] = 39.37
	numbers = frozenset("0123456789.eE")

	def __init__(self,length=None):
		if length is None:
			self.__amount = 0.0
		else:
			digits = ""
			for i, char in enumerate(length):
				if char in Length.numbers:
					digits += char
				else:
					self.__amount = float(digits)
					unit = length[i:].strip().lower()
					break
			else:
				raise ValueError, "need an amount and a unit"
			self.__amount /= Length.convert[unit]
	
	def set(self,length):
		self.__init__(length)
	def to(self,unit):
		return self.__amount * Length.convert[unit]
