#!/usr/bin/python

import fnmatch
import os
from time import sleep
from subprocess import call


app = "/Applications/Subtitles.app/Contents/MacOS/Subtitles"
nome_file = "lista.txt"
lista=[]
in_file = open(nome_file,"r")
while 1:
	in_line = in_file.readline()[:-1]
        if len(in_line) == 0:
            break
	lista.append (in_line)
in_file.close()

while 1:
	for root, dirnames, filenames in os.walk('/Users/giuseppevavala/Movies/SERIE TV'):
  		for filename in fnmatch.filter(filenames, '*'):
      			el = os.path.join(root, filename)
			if not el in lista:
				fileName, fileExtension = os.path.splitext(el)
				if ('.srt' in fileExtension) or (os.path.isfile(fileName + ".srt")):
					in_file = open(nome_file,"a")
					in_file.write(el + "\n")
					in_file.close()
 					lista.append(el)
					print "Aggiunto in lista"
				else:
					call ([app, el])
	sleep (60*5)
