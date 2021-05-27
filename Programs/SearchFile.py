#!/usr/bin/env python3
from os import remove, listdir
from os.path import isdir, join
from argparse import ArgumentParser

def get_args():
	parser = ArgumentParser()
	parser.add_argument("-s", "--search", dest="search",
						help="search", metavar="search")
	parser.add_argument("-f", "--file", dest="file",
						help="file", metavar="file")
	parser.add_argument("-e", "--exclude", dest="exclude",
					help="exclude", metavar="exclude", default="")
	args = parser.parse_args()
	return args

def recurseFolder(folderToSearch, fileToSearch, exclusion = []):
	global count
	count += 1
	print(folderToSearch)
	try:
		for FileOrFolder in [f for f in listdir(folderToSearch) if f.lower() not in exclusion]:
			if fileToSearch.lower() in FileOrFolder.lower():
				found.append(f"Found '{FileOrFolder}' at folder '{folderToSearch}'")

			elif isdir(join(folderToSearch, FileOrFolder)):
				recurseFolder(join(folderToSearch,FileOrFolder), fileToSearch, exclusion)
	except PermissionError:
		pass



if __name__ == "__main__":
	count = 0
	found = []
	args = get_args()
	recurseFolder(folderToSearch=args.search, fileToSearch=args.file, exclusion=["documents and settings", "winsxs", "servicing", "application data", "$recycle.bin", "sys", "proc", args.exclude.lower()])
	print(f"\n\nRecursed over {count} folders and found {len(found)} appearances of the word '{args.file}'")
	for f in found:
		print(f)



