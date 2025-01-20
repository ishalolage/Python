    # lists  ---can be changed      tuple-cannot be chaged
marks=[3,6,9,"isha"]  #------- length-4,index3
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[-2]) #negative indexing
print(marks[ len(marks)-2]) #positive indexing 
print(marks[ 4-2]) 
print(marks[ 2]) 
if 6 in marks:
    print("yes")
else:
    print("no")   
