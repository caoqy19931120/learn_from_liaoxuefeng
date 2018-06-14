# -*- coding: utf-8 -*-
#脚本功能实现，在脚本目录可以搜索关键字文件python locate.py keyword

import os
import sys

def search(key_word,dir):
	all_list = os.listdir(dir)
	for x in all_list:
		new_list = os.path.join(dir,x)
		if os.path.isdir(new_list):
			search(key_word, new_list)
		else:
			if key_word in new_list:
				print(new_list)

key_word = sys.argv[1]
dir = os.getcwd()
search(key_word,dir)
