import string
string.punctuation
fi=open('theoberoi.txt','r')
f1=open('theoberoi1.txt','w')

for line in fi:
	if line.strip():
		k= " ".join("".join([" " if ch in string.punctuation else ch for ch in line]).split())
		f1.write(str(k.lower()))
		f1.write("\n")
f1.close()
fi.close()