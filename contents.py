import os

class File:

	def __init__(self, fileName, contents):
		self.fileName = fileName
		self.contents = contents

	def printFile(self):
		print (self.fileName)
		print (self.contents)



bank = []

for filename in os.listdir("."):
	if filename.endswith(".py"):
		continue

	with open(filename, "r") as file:
		bank.append(File(filename, file.read()))

for file in bank:
	file.printFile()
