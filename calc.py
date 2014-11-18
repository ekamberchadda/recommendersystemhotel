fi=open('score.txt','r')
f=open('final.txt','w')
pre="abc"
m=0
for li in fi:
	k=li.split()

	for word in k:
		if word=="ITC" or word=="HYATT" or word== "LALIT" or word== "TAJ" or word == "OBEROI":
			if word != pre:
				if m==0:

					f.write("\n"+word +" ")
					m=1
				else :
					f.write("breakfast "+str(b)+" staff "+str(st)+" service "+str(se)+" location "+str(l)+" pool "+str(p)+" room "+str(r)+"\n"+word+" ")
				b=0
				st=0
				se=0
				l=0
				p=0
				r=0
				fb=0
				fst=0
				fse=0
				fl=0
				fp=0
				fr=0
				pre=word

		elif word=="breakfast":
			fb=1
		elif word=="staff":
			fst=1
		elif word=="service":
			fse=1
		elif word=="location":
			fl=1
		elif word=="pool":
			fp=1
		elif word=="room":
			fr=1
		elif fb==1:
			fb=0	
			b=b+float(word)

		elif fst==1:
			fst=0	
			st=st+float(word)
		elif fse==1:
			fse=0	
			se=se+float(word)
		elif fl==1:
			fl=0	
			l=l+float(word)
		elif fp==1:
			fp=0	
			p=p+float(word)
		elif fr==1:
			fr=0	
			r=r+float(word)
	
f.write("breakfast "+str(b)+" staff "+str(st)+" service "+str(se)+" location "+str(l)+" pool "+str(p)+" room "+str(r))

f.close()
fi.close()