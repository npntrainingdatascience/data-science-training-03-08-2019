a=[1,2,3,4,5,6,7,8]

#def square(n):
#    return n*n

#print(list(map(square,a)))

print(list(map(lambda x:x*x,a)))

print(list(filter(lambda x:x%3==0,a)))

full_name = lambda fname,lname:fname+" "+lname

print(full_name("Rakesh","Sharma"))

#lambda
#lambda x
#lambda x,y
#We can not use lambda for multi line functions

