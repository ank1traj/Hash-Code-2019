
#list for data in dataset 
ds_list=[]

# counting no. of lines and adding each line in ds_list[] from dataset
ds=open("c_memorable_moments.txt","r")

#no. of lines
no_l=0
i=0
for lines in ds:
	no_l+=1
	lines=lines.rstrip('\n')
	ds_list.append(lines)



# no. of pics 
n_pic = int(ds_list[0])

# evaluating no. of H and V pics
nH=0
nV=0
for i in range(1,no_l):
	p=ds_list[i].split(' ')

	if p[0]=="H":
		nH+=1
	else:
		nV+=1

#evaluating no. of slides



hl=[]
vl=[]
for i in range(1,no_l):
	p=ds_list[i].split(' ')

	if p[0]=="H":
		hl.append(i-1)
	else:
		vl.append(i-1)

#final printing....
f=open("aj.txt","w")

ns=nH+(nV//2)
if nV%2==0:
	print(ns)
	f.write(str(ns)+'\n')
else:
	print(str(ns+1))
	f.write(str(ns+1)+'\n')

for i in hl:
	print(i)
	f.write(str(i)+'\n')

for j in range(0,len(vl)-1,2):
	print(str(vl[j]),str(vl[j+1]))
	f.write(str(vl[j])+" "+str(vl[j+1])+'\n')
f.close()
