x=int(input("enter the value of x:"))
#x is the variable to match
match x:
    #if x is 0
    case 0:
        print("x is zero")
    # case with f-condition    
    case 4:
        print("case is 4")
    # case _:    #default value
        # print(x)       

    case _ if x!=90:
        print("x is not 90")
    case _ if x!=80:
        print("x is not 80")   
    case _:   
        print(x)

    

