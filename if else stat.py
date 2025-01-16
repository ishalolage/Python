    #if else statement                   conditional operators - [>,<,>=,<=,==,!=]
a= int(input("enter your age"))
print("your age is: ",a)
if(a>18):
    print("u can drive")
else:
    print("u cannot drive")
 
#     #elif statement

a= int(input("enter your number"))

if(a<0):
    print("number is negative")     #indendation-space before print
elif(a==0):
    print("number is zero")    
elif(a==555):   
    print("number is special")
else:
    print("u cannot drive")
print("i am finally happy")   

      #nested statement 
num=int(input("enter your number"))
if(num<0):
    print("number is negative") 
elif(num>0):
    if(num<=10):
        print("number is between 1-10")  
    elif(num>10 and num<=20):
        print("number is betwen 11 to 20")    
    else:
        print("number is greater than 20")
else:
    print("number is zero")


print("i am done")    
