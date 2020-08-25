import string

try:
    fhand = open('msgs.txt')
except:
    print('File cannot be opened:')
    exit()


wnt_wrd=input('please en word : ')
count=0


for line in fhand:
    line = line.translate(line.maketrans('', '', string.punctuation))
    words = line.split()
    for word in words:
    	if word == wnt_wrd:
    		count+=1
      
	
	
	
print("count of" , wnt_wrd , 'is ',count)
	
	
	
	
