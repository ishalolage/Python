x=5 #global varible
def my_function():
    global x
    x=777

    y=2  #local var
    print(y)
my_function()
print(x)  