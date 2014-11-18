
import re

fi=open('data.txt','r')
f=open('score.txt','w')
t=0
j=0
m=0
for li in fi:
	k=li.split()

	for word in k:
		if word=="ITC" or word=="HYATT" or word== "LALIT" or word== "TAJ" or word == "OBEROI":
			if m==0:

				f.write("\n")
				f.write(str(word)+ " ")
				m=1
			else:
				f.write(str(t) + "\n")
				f.write(str(word)+" ")
				
			j=0
			t=0
		elif word=="breakfast" or word=="staff" or word=="service" or word=="location" or  word=="pool" or word == "room":
			
			if j==0:
				f.write(str(word)+" ")
				j=1
			else:
				f.write(str(t) +" " + str(word)+" ")
		
			t=0


		else :	
			print word
			with open('1SentiWordNet_1.0.1.txt', 'r') as inF:
    				for line in inF:
        				
						if re.search( r""+word, line, re.M|re.I):
							#print line
							k=line.split()
							#print k[0] ,k[1]
							t= t+(float(k[0])-float(k[1]))
							print t
							break
   
f.write(" "+str(t))   
fi.close()
f.close()      				