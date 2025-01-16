# 2 types of function- user defined and built in function 


# def calculategmean(a,b):            #def function_name(parameters)
#     mean=(a*b)/(a+b)                   # pass
#     print(mean)                        #code and statements

# def isgreater(a,b):
#   if(a>b):
#     print("first number is greter")    
#   else:
#     print("second number is greater or equal")    

# def islesser(a,b):
#    pass



# function arguments
# def average(a=2,b=2):
#    print("the average is", (a+b)/2)

# average()
# average(3,3)
# average(5)  #a=5 and b= 2 is by dafault

def average(*numbers):
   print(type(numbers))
   sum=0
   for i in numbers:
      sum=sum+i
   print("average is:", sum/len(numbers))   
   

