with open('names.txt','r') as myfile:
    lines=myfile.readlines()
     
l=[]
for i in lines:
    #print(i.strip())
    l.append(i.strip())

for _ in sorted(l, reverse=True):
    print(_)

    
