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
	if filename == "contents.py":
		continue

	try:

		with open(filename, "r") as file:
			bank.append(File(filename, file.read()))


	except (IsADirectoryError, PermissionError):
		continue

for file in bank:
	file.printFile()
