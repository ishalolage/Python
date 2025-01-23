dict ={
    "name":"isha",
    "std":5,
    "eligible":True
}   

print(dict["name"])
print(dict.get("name"))
print(dict.get("name2"))   # not throws error
print(dict.keys())
print(dict.values())
for key in dict:
    print(key)



    