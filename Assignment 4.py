#Q.1
Lst=[1,2,3,4,5]
Lst.reverse() 
print("Reverse List is:",Lst)

#Q.2
String="Hello To All"
upper=""
for letter in String:
    if letter.isupper():
        upper=upper+letter+','
print("All uppercase letters are:",upper)

#Q.3
value=input("Enter value:")
a=value.split(',')
b=[]
for x in a:
    b.append(int(x))
print(b)


#Q.4
String="level"
rev=String[::-1]
if String==rev:
    print('String is a palindrome')
else:
    print('String is not a palindrome')

#Q.5
import copy as c
l1=[1,2,3,[7,6],5]
l2=c.deepcopy(l1)
l1[3][1]='Hello'
l1[2]='There'
print(l1)
print(l2)

"""
The difference between shallow copy and deep copy:
->is for objects that contains other object like list containing list inside

1.In case of shallow copy, a reference of object is copied in other object. It means that any changes made to a copy of object do reflect in the original object.
A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
In python, this is implemented using “copy()” function.

2.In case of deep copy, a copy of object is copied in other object. It means that any changes made to a copy of object do not reflect in the original object.
A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
In python, this is implemented using “deepcopy()” function.

"""












