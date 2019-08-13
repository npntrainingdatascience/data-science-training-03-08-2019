def square(a):
    return a**2

list1=[1,2,3,4]
print(list(map(square,list1)))

def even(a):
    if a%2==0:
        return a

print(list(filter(even,list1)))

lambda x: x**2