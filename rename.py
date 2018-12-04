#####################################################################
#####################################################################
# script: rename.py
# author: Lincoln
# date: 12.3.18
#
# Rename merged files
#####################################################################
#####################################################################
import os

currPath = '/home/ubuntu/sandbox_expansion3/171120_concat/concat/'

for file in os.listdir(currPath):
	#try:
	#	fStrip = file.split('-')
	#	toKeep = fStrip[0] + '_' + fStrip[1]
	#	toKeep = toKeep + '.homo.Aligned.out.sorted.merged.bam'
	#	os.rename(file, toKeep)
	#except IndexError:
	#	continue
	
	try:
		fStrip = file.split('.')
		cellName = fStrip[0]
		os.mkdir(currPath + cellName)
		#print(cellName)
		newFile = currPath + cellName + '/' + file
		#print(newFile)
		os.rename(file, newFile)
	except IndexError:
		continue

	#try:
	#	fSplit = file.split('_')
	#	toKeep = fSplit[0] + '_' + fSplit[1]
	#	toKeepStrip = toKeep.strip('concat')
	#
	#	toKeepSplit =  toKeepStrip.split('.')
	#	toKeepSplit1 = toKeepSplit[0]
	#
	#	toKeepSplit2 = toKeepSplit1 + '.homo.Aligned.out.sorted.merged.bam'
	#	os.rename(file, toKeepSplit2)

	#except IndexError:
	#	continue

#####################################################################
#####################################################################
