#!/usr/bin/env python3
import os
import threading
from difflib import SequenceMatcher
from argparse import ArgumentParser
from platform import system
from time import sleep
from timeit import default_timer as timer


def get_args():
	parser = ArgumentParser()
	parser.add_argument("-s", "--search", dest="folder_to_search",
						help="Folder in which to search", metavar="folder_to_search")
	parser.add_argument("-f", "--file", dest="file_to_find",
						help="File to find", metavar="file_to_find")
	parser.add_argument("-e", "--exclude", dest="excluded_folders",
					help="Folder para não procurar. Use & para separar mais de 1 folder", metavar="excluded_folders", default=None)
	parser.add_argument("-t", "--threads", dest="max_threads",
					help="Amount of Threads the program can use", metavar="max_threads", default=3)
	parser.add_argument("-r", "--remove", dest="remove_if_found",
					help="If enabled, will remove files found", metavar="remove_if_found", default=False)
	parser.add_argument("-m", "--match", dest="match_ratio",
					help="Match ratio to the word passed as arg", metavar="match_ratio", default=0.35)
	args = parser.parse_args()
	return args

class Recurser:

	def __init__(self, file_to_find, folder_to_search, max_running_threads, 
		match_ratio, exclusions=[], remove_if_found=False):
		self.match_ratio = match_ratio
		self._data = {}
		self.file_to_find = file_to_find
		self.exclusions = exclusions
		self.max_running_threads = max_running_threads
		self.found = {}
		self.removed_amount = 0
		self.recursion_amount = 0
		self.threads = []
		self.start_time = timer()
		self._start_thread(folder_to_search)
		[t.join() for t in self.threads]
		self._filter()
		if remove_if_found:
			self._remove_matches()
		self.end_time = timer()

	def recurse(self, folder_to_search):
		self.recursion_amount += 1
		print(folder_to_search)
		try:
			for obj in [f for f in os.listdir(folder_to_search) if f.lower() not in self.exclusions]:
				full_path = os.path.join(folder_to_search, obj)
				self._collect_data(obj, full_path)
				if os.path.isdir(full_path):
					if threading.active_count() < self.max_running_threads:
						self._start_thread(full_path)
					else:
						self.recurse(full_path)
		except PermissionError:
			return

	def _collect_data(self, file_name, path):
		self._data[path] = SequenceMatcher(None, self.file_to_find.lower(), file_name.lower()).ratio()

	def _start_thread(self, path):
		th = threading.Thread(target=self.recurse, args=(path,))
		self.threads.append(th)
		th.start()		

	def _filter(self):
		separator = "\\" if system().lower() == "windows" else "/"
		for path, match_ratio in self._data.items():
			if match_ratio >= self.match_ratio:
				if separator.join(path.split(separator)[:-1]) in [k[1] for k in self.found.keys()]:
					continue
				self.found[(path, match_ratio)] = f"{path} - {round(match_ratio, 2)}% match"

	def _remove_matches(self):
		for path in self.found.keys():
			self.removed_amount += 1
			if system().lower() == "windows":
				command = f"""powershell.exe  -ExecutionPolicy unrestricted -command "& {{ Remove-Item -Recurse -Force '{path}' -erroraction -silentlycontinue }}" """
			else:
				command = f""" rm -rf "{path}" """
			os.system(command)

	def __str__(self):
		frase = f"Recursed over {self.recursion_amount} folders and found {len(self.found)} matches \
of the word '{self.file_to_find}':\n"
		
		frase += "\n".join(
			# Orders by match ratio
			[i[1] for i in sorted({key[1]:value for key, value in self.found.items()}.items())]
			)
		if self.removed_amount == 1:
			frase += f"\n1 file was deleted"
		elif self.removed_amount > 1:
			frase += f"\n{self.removed_amount} files were deleted"
		frase += f"\nDuring the {round(self.end_time - self.start_time, 3)} seconds of execution, \
{len(self.threads)} threads were started"
		return frase


if __name__ == "__main__":
	args = get_args()
	exclusions = ["documents and settings", "winsxs", "servicing", "application data", 
				  r"$recycle.bin", "icons", "appium", "nugetpackages", "uwpnugetpackages", "android"]
	if args.excluded_folders is not None:
		[exclusions := exclusions + [exclusion_file.strip(" ")] for exclusion_file in args.excluded_folders.split("&")]
	recurser = Recurser(
		file_to_find=args.file_to_find,
		folder_to_search=args.folder_to_search,
		exclusions=exclusions,
		remove_if_found=args.remove_if_found,
		max_running_threads=int(args.max_threads),
		match_ratio=float(args.match_ratio)
		)
	print("\n\n\n")
	print(recurser)