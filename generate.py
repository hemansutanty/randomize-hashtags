import random
import sys
import argparse


# Parse commadn line args with flags
parser = argparse.ArgumentParser()
parser.add_argument("-cat", "--category", help="Category Type")
parser.add_argument("-no", "--number", help="Number of Tags")
args = parser.parse_args()

# Setting total number of arguments
numberOfTags=int(args.number)

# Choose category file
fileName = args.category
fileName = fileName+".txt"

lineList = [line.rstrip('\n') for line in open(fileName)]
randomSample = random.sample(lineList, numberOfTags)
tags = ""
for i in randomSample:
	tags+=(" "+i)
print(tags) 
