# -----Set-----

nums = set()    # Creates an empty set
nums.discard(10)    # If 10 is present in set -> removes 10, else -> Ignore . T.C -> O(1)
nums.remove(10) # If 10 is present in set -> removes 10, else -> Throws KeyError . T.C -> O(1)
# Checking if 100 is present in set -> T.C -> O(1)
if 100 in nums :
    print("Present")
else :
    print("not present")
nums.add(100) # Adds 100 to the set if not present, else -> ignore -> T.C -> O(1)
print(nums)
print(type(nums))

# -----Set-----



'''
# -----Dictionary-----
nums = {
    10 : 0,
    20 : 1, 
    40 : 2, 
    300 : 3
}
print(type(nums))
# Checks if elem is present in dict 
if 300 in nums :
    print(nums[300])
else :
    print("Not present")

# nums[30] = 8   # Adds the key value pair to dictionary, if key exists -> update the value
# print(nums[30]) # Returns the value, if key is present, if not present -> Throws KeyError 
# -----Dictionary-----
'''


'''
def c() :
    print("Inside c")

def b() :
    c() 
    print("Inside b")

def a(): 
    b()
    print("Inside a")

a()
print("In line no 14")
b()
'''

# nums = [10, 20, 30, 10, 29]

# nums.sort() # Sort the list -> T.C -> O(n logn)
# print(nums.pop()) # Removes the last element in list, if list is empty -> Throws IndexError. T.C -> O(1)
# print(nums[-1])
# print(nums.index(10))   # Returns the first occurrence of element -> int -> if not present -> Throws ValueError -> T.C -> O(n) 
# print(nums.count(10)) # Returns the number of occurrences of element -> int -> T.C -> O(n)
# nums.insert(0, 40)  # Inserts element at index, if index is not valid -> inserts at last -> T.C -> O(n)
# nums.append(40) # Appends the element to last -> T.C -> O(1)
# print(nums)
# for i in range(len(nums)) :
#     print(i, " : " ,nums[i])

# for i in nums :
#     print(i)
# print(nums, type(nums))
# print(type(nums[2]), type(nums[3]))



'''
n = int(input("Enter n : "))
# Number pattern
end = (2 * n) - 1
for i in range(n) :
    num = (2 * i) + 1
    for j in range(n) :
        print(num, end = " ")
        num += 2
        if num > end :
            num = 1
    print()
'''


'''
# Diamond pattern
# First half
for i in range(1, n + 1) :
    # Spaces -> n - i 
    for j in range(1, n - i + 1) :
        print("_", end = " ")
    # Stars -> 2 * i - 1
    for j in range(1, 2 * i) : 
        print("*", end = " ")
    print()
# Second half
for i in range(n - 1, 0, -1) :
    # Spaces -> n - i 
    for j in range(1, n - i + 1) :
        print("_", end = " ")
    # Stars -> 2 * i - 1
    for j in range(1, 2 * i) : 
        print("*", end = " ")
    print()
'''

'''
for i in range(1, n + 1) :
    print("_" * (n - i), end = "")
    print("*" * i)
    # # Spaces -> n - i 
    # for j in range(1, n - i + 1) :
    #     print("_", end = " ")
    # # Stars -> i 
    # for j in range(1, i + 1) :
    #     print("*", end = " ")
    # print()
'''


'''
if n % 3 == 0 and n % 5 == 0 :
    print("Divisible by 3 and 5")
elif n % 3 == 0 :
    print("Divisible by 3")
elif n % 5 == 0 :
    print("Divisible by 5")
else :
    print("Not divisible")
print("In line no 11")
'''


'''
n = 10
print(n)
print(type(n))
n = [10.5]
print(n)
print(type(n[0]))
'''