age=23
if(age<14):
    print("minor")
elif(age>14 and age<=34):
    print("working professionals")
else:
    print("seinor citizen")




strl=['a','b','c','d']
dict={}
for  i in strl:
 if i not in dict.keys():
    dict[i]=0
dict[i]+=1
print('aplhacon',dict)



import numpy as np
import time
import sys

s = range(1000)

print(sys.getsizeof(5) * len(s))
D = np.arange(1000)

print(D.size * D.itemsize)