#a=[i+10 for i in range(0,10)]
#print(a)

#a=[i for i in range(2,100) if i%2==0]
#print(a)

keys = ['a','b','c','d','e']
values = [1,2,3,4,5]
#print(dict(zip(keys,values)))
dict1={key:val for (key,val) in zip(keys,values)}
print(dict1)
#myDict = {x: x**2 for x in [1,2,3,4,5]}
#print(myDict)
