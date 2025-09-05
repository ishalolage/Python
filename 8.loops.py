                          #for loop -repeating

 #for strings iteration

name ="isha"
for i in name:
    print(i)
    if (i=="h"):
        print("It is something special")

   #for lists
colors=["red","yellow","pink","white"] 
for color in colors:
    print(color)
    # for i in colors:
    #   print(i) 

for k in range(5): #from 0 to 4 
    print(k+1)   # 1 to 5
for k in range(2,9):   # 2 to 8
    print(k)
for k in range (1,13,3):
    print(k)
                         #while loop- execute statement while the condition is true 

i=0
while(i<=5):
    print(i)
    i=i+1
print("we are done")

i=int(input("enter the number"))
while(i<=55):
    i=int(input("enter the number"))
    print(i)

print("we are done")

count=5         #decrementing while loop
while(count>0):
    print(count)
    count=count-1
else:
    print("i am inside else")    

        # do while loop -loop will run whether condition is true or false


#do{
   #loop body;
# }while(condition);

i =0
while True:
    print(i)
    i=i+1
    if(i % 100==0):
        break










      