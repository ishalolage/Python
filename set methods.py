s1={1,2,3,4}
s2={4,5,6,7}
print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1,s2)
# s1.update(s2)
print(s1.symmetric_difference(s2))
print(s1.difference(s2))

t1={9,8,7,6,2,3,4,5}
t2={2,3,4,5}
print(t1.isdisjoint(t2))  #no intersecttion
print(t1.issuperset(t2))  #t1 super set of t2 ,t2 is subset of t1
print(t2.issubset(t1))
#for adding values
t1.add(666)
print(t1)
#for removing values
t1.remove(7)
print(t1)
item=t1.pop() #pop any values
print(item)

if 2 in t1:
    print("yes")
else:
    print("no")    