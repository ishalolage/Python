for i in range(12):
    print("5 *", i, "=", 5 *i+1)
    if(i==10):
        break 
    print("we are out of loop")

for i in range(12):
    if(i==10):
        break
    print("5 *", i+1, "=", 5 *(i+1))
    
# print("we are out of loop")

for i in range(12):
    if(i==10):
        print("skip the iteration")
        continue                #jump on next iteration
    print("5 *",i, "=",5*i)




