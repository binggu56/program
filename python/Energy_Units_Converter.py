#!/usr/bin/python
# Filename = Energy_Units_Converter


units = ['m','cm']
print(units[1])
unit = input("The unit you want to convert:")
for term in units:
	if unit == term:
		print("1"+unit+"="+"100"+"cm")
