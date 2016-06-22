#initialize directories
toRead = r"D:\old.xml" 
toWrite = r"D:\new.xml"
#initialize arrays to hold stuff
arrOfKeys = []
arrOfTags = []
#initialize array to write
testArr = []

#open first file for reading and parsing
with open(toRead) as f1:
	for line1 in f1:
		#getting the tag names
		index0 = line1.find('Computer')
		index1 = line1.find('">')
		if index0 > 0:
			tagsToFind = line1[index0 : index1+1]
			arrOfTags.append(tagsToFind)	
			
		#getting the keys corresponding to tag names
		if index0 > 0:
			keysToFind = line1[index1 + 2:index1 + 30]
			arrOfKeys.append(keysToFind)

#creating new file to write to
a = open(r"D:\test.xml","w")

#open second file to read and compare to
with open(toWrite, "r+") as f2:
	for line2 in f2:
		#index var
		i = 0
		#finding correct keys
		if (line2.find('8/1/2011') > 0):
			indexEnd = line2.find('">')
			#compare found key to keys in first file
			for keys in arrOfKeys:
				#if keys match, then add tag names
				if (line2.find(keys) > 0):
					line2 = line2[:indexEnd + 1] + ' ' + arrOfTags[i][:-1] + line2[indexEnd:]
				#keeps keys and tags in same order
				i += 1
		#write to new file
		a.write(line2)