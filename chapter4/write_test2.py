import os
os.chdir('F:\HeadFirstPython\Chapter3\chapter3\Mine')

import sys

def print_lol(the_list, indent = False, level = 0, f = sys.stdout):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item, indent, level+1 , f)
		else:
			if indent:
				for tab_stop in range(level):
					print("\t",end = '',file = f)
			print(each_item,file = f)
			
try:
	with open('man_data.txt') as man, open('other_data.txt') as other , open('man_file.txt','w') as man_file, open('other_file.txt','w') as other_file:
		print_lol(man,True , 1,f = man_file)
		print_lol(other,True,1,f = other_file)
except IOError as err:
	print('error: '+str(err))
