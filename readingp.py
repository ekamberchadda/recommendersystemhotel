import nltk
fi=open('ITCMaurya.txt','r')
f1=open('itcpos.txt','w')
f=0
co=0
for line in fi:
	if line[0] == '/' and f==0:
		f=1
		co+=1
	elif line[0]=='R' and f==1:
		f=0
	if f==1:
		#te =  nltk.word_tokenize(line.lower())
		#k=nltk.pos_tag(te)
		
		#print te
		#print k
		from nltk.tokenize import RegexpTokenizer
		tokenizer = RegexpTokenizer(r'\w+')#(r'(?u)\W+|\$[\d\.]+|\S+\w+')#(r'\w+')
		te=tokenizer.tokenize(line.lower())
		k=nltk.pos_tag(te)
		#print k
		f1.write(str(k))
		f1.write("\n")

		#s=" "
		#for wo in k:
			#if wo[1]=='JJ' or wo[1]=='JJR' or wo[1]=='JJS':
			#	s=s +" "+ str(wo[0])
				
		#	if wo[0]=='breakfast':	
			#	print (wo,co)
		#print s
f1.close()	
print co