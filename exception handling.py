# try:
#     numerator = 1
#     denominator =0
#     res = numerator /denominator
#     print(f"result is : {res}")

# except  ZeroDivisionError:
#     print("Error:Division by zero is not allowed")
# else:
#      print("division done successfully")
# finally:
#     print("execution is completed")  



class Logininfo(Exception):

    def validate_info(self, password ,username ):
        correctuser ="admin"
        correctpass = "password"
        if username == correctuser and password == correctpass:    
            print("login successfully")
        else:
            raise Logininfo("user or password invalid")
    



try:
    login= Logininfo()
    login.validate_info("password","admin")
except Logininfo:
    print("login failed try again")    
else:
    print("login successful")         
finally:
    print("welcome to our site")    















