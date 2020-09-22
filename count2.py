import string

prv_words=[]
end_word=None

while True:
    end_word=input("please enter a new word , en (ok) to finish:  ")
    if end_word!="ok":
        prv_words.append(end_word)
    else:
        break


fname=input("please entre the file's name : ")
try:
    fhand = open(fname)
except:
    print('File cannot be opened:')
    exit()

han=[]
counts = dict()
for line in fhand:
    line = line.translate(line.maketrans('', '', string.punctuation))
    words = line.split()
    for word in words[5:]:
        han.append(word)

for word in han:
    if word in prv_words:
        continue
    else:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
            

lst=list()


for key,val in counts.items():
	lst.append(  (val , key)  )
	
lst.sort(reverse=True)
del lst[2]
for key  , val in lst[:10]:
	print(  val  , key )


	
	
	
	
	
	
	
	
