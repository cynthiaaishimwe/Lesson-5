# list : they are enclosed in square braces
# lists can also contain different types of elements

# tuple :a list of items separated by a comma 
# this is enclosed in rounded braces and these are immutable ()

# dictionaries : these are enclosed using curly braces
# they holds keys and values

# set:they enclosed using  curly brackets

# list
list1 = ["Laptops","television","camera","printer",90,70,50]
list1[0] = "PC"
print(list1)

list2 = ["cables","speakers","other appliances"]
print(list1 + list2)

list3 = [8,3]
print(list3 * 3)

animals = ["Dog","cat","puppies","kitten"]
print("Dog" in animals)

nums = [7,9,3]
for x in nums:
 print(x*3)
 print(len(nums))

# list

# .insert an element passed at a position passed in
x = [5,3,8,6]
x.insert(3,8)
print(x)
#  .pop removes the last element from the list and returns it.
x = [4,6,7,2,5,10]
print(x.pop())
# .remove a specific element passed to it

y = [20,10,50,40,78,30]
(y.remove(10))
(y.reverse())
print()
print(y)


# tuple, when a tuple is just one it can be represented by a , at the end
classmates = ("Veronica","Aluel","Winnie","Regina","marion")
print(classmates)

# Write a program to copy elements 44 and 55 from the following
# tuple into a new tuple.

num2 = (11, 22, 33, 44, 55, 66)
num3 = num2[3:-1]
print(num3)



# set
set1 = {"cynthia","cedrick","bruce","baby","keza"}
print(set1)

#  Write a program to add all its elements into a given set.
sec_colors = {"Yellow", "Orange", "Black"}
pri_colors = {"Blue", "Green", "Red"}
sec_colors.update(pri_colors)
print(sec_colors)


# dictionary 
# dictionaries doesn't allow duplicates
dict1 = {

    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
}
print(dict1)

# Write a Python program to check if value 200 exists in the following dictionary.

dict1 = {'a': 100, 'b': 200, 'c': 300}
if 300 in dict1.values():
 print("300 present")
