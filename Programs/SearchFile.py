from os import remove, listdir
from os.path import isfile, join

count = 0
found = []
def recurseFolder(folderToSearch, fileToSearch):
	global count
	count += 1
	print(f"Recursing over {folderToSearch}")
	try:
		for FileOrFolder in listdir(folderToSearch):
			if fileToSearch in FileOrFolder:
				found.append(f"Found File on {folderToSearch}\\{FileOrFolder}")

			elif not isfile(join(folderToSearch, FileOrFolder)):
				recurseFolder(join(folderToSearch,FileOrFolder), fileToSearch)
	except PermissionError:
		pass
			
folderToSearch = input("Insert folder to search\n")
fileToSearch = input("Insert file to find\n")

recurseFolder(folderToSearch=folderToSearch, fileToSearch=fileToSearch)

print(f"\n\nRecursed over {count} folders!")
for f in found:
	print(f)
