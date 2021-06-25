#!/usr/bin/env python3
from os import remove, listdir
from shutil import rmtree
from os.path import isdir, join
from argparse import ArgumentParser
import threading
from time import sleep, time


def get_args():
	parser = ArgumentParser()
	parser.add_argument("-s", "--search", dest="search",
						help="Folder in which to search", metavar="search")
	parser.add_argument("-f", "--file", dest="file",
						help="File to found", metavar="file")
	parser.add_argument("-e", "--exclude", dest="exclude",
					help="Folder para não procurar.", metavar="exclude", default="")
	parser.add_argument("-R", "--remove", dest="remove",
					help="If enabled, will remove files found", metavar="remove", default=False)
	parser.add_argument("-T", "--threads", dest="threads",
					help="Amount of Threads the program can use", metavar="threads", default=50)
	args = parser.parse_args()
	return args

def recurseFolder(folderToSearch):
	global count, th_count
	count += 1
	print(folderToSearch)
	try:
		for FileOrFolder in [f for f in listdir(folderToSearch) if f.lower() not in exclusions]:
			if fileToSearch.lower() in FileOrFolder.lower():
				found.append(join(folderToSearch, FileOrFolder))
				if remove:
					rmtree(join(folderToSearch, FileOrFolder))

			elif isdir(join(folderToSearch, FileOrFolder)):
				if threading.active_count() < max_threads:
					th = threading.Thread(target = recurseFolder, args = 
						(join(folderToSearch,FileOrFolder),))
					th.start()
					th_count += 1
					threads.append(th)
				else:
					recurseFolder(join(folderToSearch,FileOrFolder))
	except PermissionError:
		pass


def run(args):
	global threads, max_threads, fileToSearch, exclusions
	threads = [threading.Thread(target = sleep, args=(5,))]
	threads[0].start()
	max_threads = int(args.threads)
	fileToSearch = args.file
	remove = args.remove

	exclusions = ["documents and settings", "winsxs", "servicing", "application data", 
				  "$recycle.bin", "sys", "proc", "proton 6.3", "icons"]
	[exclusions := exclusions + [exclusion_file.strip(" ")] for exclusion_file in args.exclude.split("|")]
	threading.Thread(target=recurseFolder, args=(args.search,)).start()
	sleep(2)
	[th.join() for th in threads]


if __name__ == "__main__":
	count = 0
	th_count = 0
	found = []
	args = get_args()
	run(args)

	print(f"""\n\nRecursed over {count} folders and found {len(found)} 
appearances of the word '{args.file}'.
During this time, {th_count} Threads were started.\n""")
	for f in found:
		print(f)
