# ---- STRINGS ----
s1 = "abba1" 
i = 0
j = len(s1) - 1
flag = True 
while i < j :
    if s1[i] != s1[j] :
        print("Not a palindrome")
        flag = False
        break 
    i += 1 
    j -= 1
if flag : 
    print("Palindrome")

# print(s1.find("are"))  # Returns the first occurrence of substring, if not present return -1 

# s1 = s1.replace("are", "or") # Replaces the substring with new string -> T.C -> O(n)

# s1 = s1.strip() # Returns a string after removing trailing spaces at left and right -> T.C -> O(n)

# s1 = s1.rstrip() # Returns a string after removing trailing spaces at right -> T.C -> O(n)

# s1 = s1.lstrip() # Returns a string after removing trailing spaces at left -> T.C -> O(n)

# print(s1.index("all")) # Returns the index of first occurrence of the substring. if not present -> Throws IndexError. T.C -> O(n)

# print(s1.count("are"))  # Returns the number of occurrences of a substring -> T.C -> O(n)

# words = s1.split(" ") # Returns a list of strings, with separator as the delimiter -> T.C -> O(n) 
# print(words)

# print(s1[2].isalnum())  # Returns a boolean, if string is alphanumeric or not -> T.C -> O(n)

# s1 = s1.lower() # Returns a string after converting all alphabets into lowercase -> T.C -> O(n)

# s1 = s1.upper()    # Returns a string after converting all alphabets into uppercase -> T.C -> O(n)

# print(s1[ : 5]) # Returns a substring from start till end. end -> exclusive -> T.C -> O(n)
# print(s1[2 : ]) # Returns a substring from index start till end of string , start -> inclusive -> T.C -> O(n)
# print(s1[0 : 4])    # Returns a substring, start -> inclusive, end -> exclusive -> T.C -> O(n)
# print(len(s1), s1[100]) # Returns the length of string. Returns the character at index, if index is not valid -> Throws IndexError -> len(s1) T.C -> O(n), s1[9] -> T.C -> O(1)
# print(s1)

# s = "12321"

# num = 0
# i = 0
# while i != len(s) :
#     num = (num * 10) + int(s[i]) 
#     i += 1
# print(num, type(num)) 



# ---- STRINGS ----

# nums = list(map(int, input().split()))
# print(nums)
"""
rows = int(input("Enter rows : "))
matrix = [] 
for i in range(rows) :
    print("Enter elements at ", i, " row : ", end = "")
    matrix.append(list(map(int , input().split())))
    
print(matrix)
"""
# cols = int(input("Enter cols : "))
# matrix = [] 
# for i in range(rows) :
#     nums = [] 
#     for j in range(cols) :
#         print("Enter ", i, j, " : ", end = "")
#         num = int(input())
#         nums.append(num)
#     matrix.append(nums)

# print(matrix)
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# nums = [65,56,89,12]
# matrix.append(nums)
# print(matrix)

# for row in matrix :
#     for col in row :
#         print(col, end = " ")
#     print()

# for i in range(len(matrix)) :
#     print(i, " row : ", end = "")
#     for j in range(len(matrix[i])) :
#         print(matrix[i][j] , end = " ")
#     print()
# print(matrix, type(matrix))



'''
def firstOccurrence(nums, element, i) :
    if i == len(nums) :
        return -1
    if nums[i] == element :
        return i
    return firstOccurrence(nums, element, i + 1)

def lastOccurrence(nums, element, i) :
    if i == len(nums) :
        return -1
    if nums[i] != element :
        return lastOccurrence(nums, element, i + 1)
    else :
        ans = lastOccurrence(nums, element, i + 1) 
        if ans != -1 :
            return ans
        else :
            return i
        
def lastOccurrence1(nums, element, i, ans) :
    if i == len(nums) :
        return ans
    if nums[i] == element :
        ans = i
    return lastOccurrence1(nums, element, i + 1, ans)

def printN(n) :
    if n == 0 :
        return
    printN(n - 1)
    print(n, end = " ")
    

printN(5)

# nums = [10, 20, 20]
# print(lastOccurrence1(nums, 20, 0, -1))
# print(firstOccurrence(nums, 200, 0))
# print(lastOccurrence(nums, 200, 0))
'''


'''
def fact(n) :
    if n == 1 :
        return n
    smallOutput = fact(n - 1)
    return n * smallOutput

n = 4
print(fact(n))
'''