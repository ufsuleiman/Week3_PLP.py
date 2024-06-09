# x=[1,2,3,4,5,6,7,8,9]
# print(x)
# print(x[5])
# print(x[::-1])
# print(x[0::2])
# print(x[1::2])
# for pnt in x:
#     print(pnt, x[5])
# x.remove(9)
# print(x)
# x.append(13)
# print(x)
# y=int(input('enter an intege'))
# print('%d this an integer'%y)

# create a list from 1-10 and split the list into odd and even numbers
# z=[1,2,3,4,5,6,7,8,9,10]
# print(z)
# zeven=print(z[1::2])
# zodd=print(z[0::2])

x={'kastina' : 'bakori', 'kano' : 'dawanau', 'bauchi':{'jos' : 'gora'}}
print(x['bauchi'])
y={}
y={'nigeria' : 'abuja', 'kenya' : 'nairobi'}
print(y)
del y
# print(y)
del x['kastina']
print(x)
z=set()
print(type(z))
z={1,2,3,4,5}
print(z)
w={3,7,5,1,10,2,4}
union=w not in z
print(union)
e=()
print(type(e))
print(e)
e=(1,2,3,4,5)
print(e)
g=[1,2,3,4,5,6,7,8,9]
print(type(g))
g=tuple(g)
print(type(g))
g=[1,2,3,4,5,6,7,8,9,(10,12,13)]
print(g)
e=([1,2,3,4,5], [6,7,8,9,10])
print(e)
create=(1,2,3,4,5,6,7,8,9)
create2=create +(10,)
print(create2)
final=create + create2[::-1]
print(final)