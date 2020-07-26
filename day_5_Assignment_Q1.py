list1=[0,1,2,10,4,1,0,56,2,0,1,2,0,56,0,4]
list2=[]
list3=[]

for each in list1:
	if each==0:
		list2.append(each)
	else:
		list3.append(each)

list3.sort()
list4=list3+list2


print(list4)