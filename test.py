
import re
word = 'slow'
with open('1SentiWordNet_1.0.1.txt', 'r') as inF:
		for line in inF:
			s = '\t'+word+'\t'
			t=0
			if re.search( r""+s, line, re.M|re.I):
				print line
				k=line.split()
				print k[0] ,k[1]
				t=float(k[0])+float(k[1])
				print t
				break