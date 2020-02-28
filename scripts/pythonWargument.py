#!/usr/bin/evn python3
import argparse
import sys


class WESsample(object):
	def __init__(self):
		self.platform = "Illumina"
		self.seqLen = "15"


def createScript (scriptName, sample):
	print ("hello world")


def runBWA(firstPair, secondPair):
	print ("This is the first pair" + firstPair)
	print ("This is the second pair" + secondPair)
	print ("Will issue some command")

def collectFiles (inPath):
	import os
	files = os.system("ls -al ")
	return(files)

fileDir = "x:\\project2017\\SEQC2_TGSWG2\\WES1"
print(collectFiles (fileDir))

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser = argparse.ArgumentParser(description='Launch BWA alignment.')

	parser.add_argument('--FirstPair',  '-1' , type=str, help='The first sequence read')
	parser.add_argument('--SecondPair', '-2' , type=str, help='The second sequence read')
	parser.add_argument('--fdr', default=None, type=float,
                        help='set read threshold by FDR (FLOAT) (Default \
                        method: less than 0.001)')

	args = parser.parse_args()
	print(args.FirstPair)
	print(args.SecondPair)
#	runBWA(args.FirstPair,args.SecondPair)

