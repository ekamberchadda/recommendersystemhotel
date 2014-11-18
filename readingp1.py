import nltk

import os
import nltk

fi=open('theoberoi1.txt','r')
f1=open('oberoipos.txt','w')
f2=open('data.txt','a')
f=0
co=0
for line in fi:
	if len(line) <=6 and line != '\n' and f==0 and line[0]=='r':
		f=1
		co+=1
	elif len(line)<=6 and line != '\n' and f==1 and line[0]=='r':
		f=0

	elif f==1 and line != '\n':
		from nltk.tag.stanford import POSTagger
		os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jre7\bin'
		st = POSTagger('C:\stanford-postagger-2014-08-27\models\english-left3words-distsim.tagger','C:\stanford-postagger-2014-08-27\stanford-postagger.jar')
		print line
		k=st.tag(nltk.word_tokenize(line))
		f2.write("OBEROI ")
		s=" "
		t=0
		p=" "
		for wo in k:
			if (wo[1]=='NN' or wo[1]=='NNS') and t==0 and wo[0]!= 'breakfast':
				s=" "
			elif (wo[1]=='NN' or wo[1]=='NNS') and t==1 and s!=' ':
				f2.write("breakfast "+str(s))
				s=' '
				break
			if wo[1]=='JJ' or wo[1]=='JJR' or wo[1]=='JJS': # or wo[1]=='RBR' or wo[1]=='VBG':
				s=s +" "+ str(wo[0])
			
			if wo[0]=='breakfast' :
				t=1
				
			
				#print wo[0]
				#print s	,co
		s=" "
		t=0	
		
		for wo in k:
			if (wo[1]=='NN' or wo[1]=='NNS') and t==0 and wo[0]!= 'staff':
				s=" "
			elif (wo[1]=='NN' or wo[1]=='NNS') and t==1 and s!=' ':
				f2.write(" staff " +str(s))
				s=' '
				break 	
			if wo[1]=='JJ' or wo[1]=='JJR' or wo[1]=='JJS' : #or wo[1]=='VBG':
				s=s +" "+ str(wo[0])
			
			if wo[0]=='staff' or wo[0]=='staffs':
				t=1
				#print wo[0]
				#print s	,co	
		s=" "
		t=0	
		
		for wo in k:
			if (wo[1]=='NN' or wo[1]=='NNS') and t==0 and wo[0]!= 'service':
				s=" "
			elif (wo[1]=='NN' or wo[1]=='NNS') and t==1 and s!=' ':
				f2.write(" service " +str(s))
				s=' '
				break 	
			if wo[1]=='JJ' or wo[1]=='JJR' or wo[1]=='JJS'  :#or wo[1]=='VBG':
				s=s +" "+ str(wo[0])
			
			if wo[0]=='service' or wo[0]=='services':
				t=1	

		s=" "
		t=0	
		
		for wo in k:
			if (wo[1]=='NN' or wo[1]=='NNS') and t==0 and wo[0]!= 'location' and wo[0]!="area":
				s=" "
			elif (wo[1]=='NN' or wo[1]=='NNS') and t==1 and s!=' ':
				f2.write(" location " +str(s))
				s=' '
				break 	
			if wo[1]=='JJ' or wo[1]=='JJR' or wo[1]=='JJS' : #or wo[1]=='VBG':
				s=s +" "+ str(wo[0])
			
			if wo[0]=='location' or wo[0]=='area':
				t=1	

		s=" "
		t=0	
		
		for wo in k:
			if (wo[1]=='NN' or wo[1]=='NNS') and t==0 and wo[0]!= 'pool':
				s=" "
			elif (wo[1]=='NN' or wo[1]=='NNS') and t==1 and s!=' ':
				f2.write(" pool " +str(s))
				s=' '
				break 	
			if wo[1]=='JJ' or wo[1]=='JJR' or wo[1]=='JJS' : #or wo[1]=='VBG':
				s=s +" "+ str(wo[0])
			
			if wo[0]=='pool' :
				t=1	

		s=" "
		t=0	
		
		for wo in k:
			if (wo[1]=='NN' or wo[1]=='NNS') and t==0 and wo[0]!= 'room' and wo[0]!="rooms":
				s=" "
			elif (wo[1]=='NN' or wo[1]=='NNS') and t==1 and s!=' ':
				f2.write(" room " +str(s))
				s=' '
				break 	
			if wo[1]=='JJ' or wo[1]=='JJR' or wo[1]=='JJS' : #or wo[1]=='VBG':
				s=s +" "+ str(wo[0])
			
			if wo[0]=='rooms' or wo[0]=='room':
				t=1	

		f1.write(str(k))
		f1.write("\n")
		f2.write("\n")	
f1.close()	
f2.close()
fi.close()
print co