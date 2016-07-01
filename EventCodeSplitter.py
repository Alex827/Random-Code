#imports
import sys
import os
#file to split
toSplit = sys.argv[1];
#making three dir: conditions, sightings, efforts
if not os.path.exists("conditions"):
	os.mkdir("conditions");
if not os.path.exists("sightings"):
	os.mkdir("sightings");
if not os.path.exists("efforts"):
	os.mkdir("efforts");
#put the new file into the new dir
conditionsName = "\conditions\\" + str(sys.argv[1]).replace(".csv", "") + "-conditions.csv";
sightingName = "\sightings\\" + str(sys.argv[1]).replace(".csv", "") + "-sightings.csv";
effortName = "\efforts\\" + str(sys.argv[1]).replace(".csv", "") + "-efforts.csv";
#make the new files
conditionsOut=open(conditionsName, 'w+');
sightingsOut=open(sightingName, 'w+')
effortOut=open(effortName, 'w+')
#read the original file
with open(toSplit) as f1:
	for line in f1:
		#split into different types
		if line.startswith('W'):
			conditionsOut.write(line)
		elif line.startswith('S'):
			if line.startswith('ST'):
				effortOut.write(line)
			else:
				sightingsOut.write(line)
		else:
			effortOut.write(line)
#close files
conditionsOut.close();
sightingsOut.close();
effortOut.close();