import string

try:
    fhand = open('msgs.txt')
except:
    print('File cannot be opened:')
    exit()

counts = dict()
for line in fhand:
    line = line.translate(line.maketrans('', '', string.punctuation))
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
            

lst=list()


for key,val in counts.items():
	lst.append(  (val , key)  )
	
lst.sort(reverse=True)
del lst[8]
for key  , val in lst[:10]:
	print(  val  , key )


	
	
	
	
	
	
	
	
