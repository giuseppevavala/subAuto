import fnmatch
import os

out_file = open("lista.txt","w")
for root, dirnames, filenames in os.walk('/Users/giuseppevavala/Movies/SERIE TV'):
  for filename in fnmatch.filter(filenames, '*'):
      	el = os.path.join(root, filename)
	out_file.write(el + "\n")
out_file.close()
