#####################################################################
#####################################################################
# author: Lincoln
# script: move.py
# date: 12.3.18
#
# Move merged files
#####################################################################
#####################################################################
import os
import shutil 

currPath = '/home/ubuntu/sandbox_expansion3/171120_concat/concat/'

with open('171120_cells.csv') as f:
	allCells = f.read()
	for currCell in os.listdir(currPath):
		if currCell in allCells:
			newFile = '/home/ubuntu/sandbox_expansion3/171120_concat/concat1/' + currCell 
			shutil.copytree(currCell, newFile)

#####################################################################
#####################################################################