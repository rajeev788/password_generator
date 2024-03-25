#indexing
'''
a="hello"
print(a[0])
#slicing
b="hello"
print(b[0:4]) 
#negative index can be also done
a="hello world"
print(a[-1])

#gives the total output
a="hello wolrd"
print(a[0:]) #can be done in negative indexing slicing
#indexing in list
a=["hello","world"]
print(a[0]) #slicing and negative indexing and slicing can be also done
 
 #value of list can be changed 
a=["hello"]
a[0]="bye"
print(a)

#make a list of friut and prnt usig while loop
# tip b=lens(a)
print(b)
'''

#tople -immutable group of data

'''
a=(1,2,3,4,4)
b=a[0:2:2]  #the last no. says how many steps to jump
print(b)
#tuple is immutable but how can we still do it? - we can the data type from tuple to list
a=list((1,2,3,4,4))
a[0] =0
b=tuple(a)
print(b)
'''

#set - group of mutable data

'''
a={'1','2','3','4','4'}
 
print(a)
''' #it can give the output in any order because it is unodered data so (no indexing and slicing)

#dictionary
a= {'1':"hello",'2':"world"}
a[0]='apple'
print(a)