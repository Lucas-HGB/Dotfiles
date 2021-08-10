#!/usr/bin/env python3
from os import remove, listdir
from shutil import rmtree
from os.path import isdir, join
from argparse import ArgumentParser
import threading
from time import sleep, time
from platform import system as os
from os import system


def get_args():
	parser = ArgumentParser()
	parser.add_argument("-s", "--search", dest="search",
						help="Folder in which to search", metavar="search")
	parser.add_argument("-f", "--file", dest="file",
						help="File to found", metavar="file")
	parser.add_argument("-e", "--exclude", dest="exclude",
					help="Folder para não procurar. Use & para separar mais de 1 folder", metavar="exclude", default="")
	parser.add_argument("-T", "--threads", dest="threads",
					help="Amount of Threads the program can use", metavar="threads", default=3)
	parser.add_argument("-p", "--print", dest="print",
					help="Amount of Threads the program can use", metavar="print", default=False)
	parser.add_argument("-R", "--remove", dest="remove",
					help="If enabled, will remove files found", metavar="remove", default=False)
	args = parser.parse_args()
	return args

def recurseFolder(folder_to_search):
	global count
	count += 1
	if print_text:
		print(folder_to_search)
	try:
		for file_or_folder in [f for f in listdir(folder_to_search) if f.lower() not in exclusions]:
			if file_to_search.lower() in file_or_folder.lower():
				found.append(join(folder_to_search, file_or_folder))
				if remove:
					try:
						if os().lower() == "windows":
							system(f"""powershell -ExecutionPolicy unrestricted -Command "& {{ Remove-Item -Recurse -Force "{join(folder_to_search, file_or_folder)}" }} " """)
						else:
							system(f"""rm -rf "{join(folder_to_search, file_or_folder)}" """)
					except (NotADirectoryError, PermissionError, FileNotFoundError):
						pass

			elif isdir(join(folder_to_search, file_or_folder)):
				if threading.active_count() < max_threads:
					th = threading.Thread(target = recurseFolder, args = 
						(join(folder_to_search,file_or_folder),))
					th.start()
					threads.append(th)
				else:
					recurseFolder(join(folder_to_search,file_or_folder))
	except (PermissionError, FileNotFoundError):
		pass


def run(args):
	global threads, max_threads, file_to_search, exclusions, print_text
	threads = [threading.Thread(target = sleep, args=(5,))]
	threads[0].start()
	max_threads = int(args.threads)
	file_to_search = args.file
	remove = args.remove
	print_text = args.print
	exclusions = ["documents and settings", "winsxs", "servicing", "application data", 
				  r"$recycle.bin", "icons", "appium", "nugetpackages", "uwpnugetpackages", "android"]
	[exclusions := exclusions + [exclusion_file.strip(" ")] for exclusion_file in args.exclude.split("&")]
	threading.Thread(target=recurseFolder, args=(args.search,)).start()
	sleep(0.2)
	while threading.active_count() > 1:
		sleep(0.2)
	return threads


if __name__ == "__main__":
	count = 0
	th_count = 0
	found = []
	args = get_args()
	threads = run(args)
	for f in found:
		print(f)

	print(f"""\n\nRecursed over {count} folders and found {len(found)} 
appearances of the word '{args.file}'.
During this time, {len(threads) - 1} Threads were started.\n""")
