st='''jimin rm 
  jungkook
  taeyung
    jin'''
print(st)

name= "isha"   #name='isha' 
print("hello, " + name)
print(name[0])
print(name[1])
print(name[2])
print(name[3])

name ="i am a student of aids "   #for loop
for character in name:
    print(character)


# strings slicing and 
fruit= "mango"
len1= len(fruit)
print("the value mango is" ,len1)
print(fruit[0:3]) #last 3 is not printed only 0,1,2
print(fruit[:4]) 
print(fruit[0:-1]) #print(fruit[0:len(friut)-1])= 0-(5-1)=0-4=0,1,2,3
print(fruit[-2:-1]) #print(3:4)

# string operations - strings are immutable but new strings can be created by them
a="isha!!!!!!! 111111 isha "
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!")) #removes !
print(a.replace("isha" ,"shreyash"))
print(a.split()) #list of each group
blogheading="introduction to js "
print(blogheading.capitalize())  #first letter capital

str1="welcome to the console"
print(len(str1))
print(len(str1.center(40)))
print(a.count("isha"))
str2="hello all the ppl??"
print(str2.endswith("??")) #asks question
print(str2.endswith("all" ,4,9))  #indexing
print(str2.find("all "))
print(str2.find("yo")) #error

str3="IshaIsGirl66"
print(str3.isalnum()) #entire string consist of a-z,A-Z,0-9 amd it gives true and if other punctions or characters are present then return false 
print(str3.isalpha()) #it has A-Z,a-z

str4= "hello world"
print(str4.islower)
print(str4.startswith("hello"))
print(str4.swapcase()) #swaps
print(str4.title())  #makes first letter capital
print(str4.istitle()) #first letter capital-T or F



# str5="      "
# print(str5.isspace())













