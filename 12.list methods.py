l=[11,33,22,55,33,44,66]
print(l)
l.append(333)   #add at end
print(l)
l.sort(reverse=False)  #f-ascending,t-decending
print(l)
# l.reverse() #reverse the list
# print(l.index(1))  #gives index no
# print(l)
# print(l.count(33)) #how many times
m=l.copy() #all values of l comes in m
m[0]=0
print(l)


l.insert(1,111)  # insert 111 at index 1
print(l)
m=[78,87]
l.extend(m) #put m in ending of l
k=m+l
print(k) #merge l and m 
print(l)
 
