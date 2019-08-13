a={"id":[1,2,3,4], "marks":["80","90","100","95"]}
for k,v in a.items():
    value = v
    for i in range (len(value)):
        value[i]=int(value[i])+10
print(a)