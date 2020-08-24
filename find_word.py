import string

#try:
#    fhand = open('msgs.txt')
#except:
#    print('File cannot be opened:', fhand)
#    exit()

fhand = open('msgs.txt')    
wnt_wrd=input('please en word')
count=0


for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
    	if word == wnt_wrd:
    		count+=1
      
	
	
	
print("count of" , wnt_wrd , 'is ',count)
	
	
	
	
