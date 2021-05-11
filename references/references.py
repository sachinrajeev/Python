#  print(10/5," -> ",10//5)

# a=int(input("enter no."))
# x,y=input().split() - obtain as string  then
# #x=int(x)
#                       #instead of above. this read no as int , so conversion  ---
# x,y = map(int,input().split())
# or
#  x, y, z = [int(x) for x in input("Enter three value: ").split()]

# print(min(list1))  
# print(max(list2))
# print(abs(list2))

#  num=list(range(20))
#  num1=list(range(20,40,2))
#  print(num)

# list1=list2[2,15,3]   from 2 to 15 with 3 interval

# list1=[2**i for i in range(1,10)]                can remove usage of append
# list1=[i for i in range(1,10) if i%2==0]                can remove usage of append

# print(list1)
# # OP - [2, 4, 8, 16, 32, 64, 128, 256, 512]

#  list1=['a','b','c','d']
#  list1.append('r')
#  list1.insert(1,'bw a & b')
#  print(list1.index('c'))
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# ----------------------------------------------------------------
#                              PRINT
# # print('square of %d is '%i,i)  OP--  square of 16 is  16
# print('hii-','mrng',sep='!')        OP- hii-!mrng
# print('hii-','mrng',end='!')        OP- hii-mrng!


# ----------------------------------------------------------------
#                             LAMBDA

#           # Display the powers of 2 using anonymous function
# terms = 10
#           # Uncomment code below to take input from the user
#            # terms = int(input("How many terms? "))
#            # use anonymous function
# result = list(map(lambda x: 2 ** x, range(terms)))
# print("The total terms are:",terms)
# for i in range(terms):
#    print("2 raised to power",i,"is",result[i])

# or
# result= lambda x: 2**x
# for i in range(10):
#     print(result(i))
# -------------------------------------------------------
#                       MATRIX
# matrix inside dict or key with mul values
# dict1={'a':[1,2],'b':[3,4]}
# print(dict1.items())
# for m,n in dict1.items():
# 	print(m,n)

# OP     dict_items([('a', [1, 2]), ('b', [3, 4])])
#       a [1, 2]
#       b [3, 4]
# -------------------------
#a = []
# mat=[]
# a.append(list(map(int, input().split())))
# a.append(list(map(int, input().split())))
# print(a)
# print(a[0])

# # # OP
# # 1 2
# # 3 3
# # [[1, 2], [3, 3]]
# # [1, 2]
# -------
# n, w = input("Enter a two value: ").split()
# n=int(n)            # to conver fro str to int
# a=[]
# for i in range(0,n):
#     a.append(list(map(str, input().split())))    # str or int depending on question
# -------------------------------------------------------
#                   FILE
# file oper
# f = open("t.txt", "r")   or r+ read and write

# for x in f:
#     print(x)

# ------ read and write curser will point to end of file so seek(0) used
# f=open("demo.txt","a+")
# f.write('\nadding second line')
# f.seek(0)
# print(f.read())
# f.close()

# -------for taking last line
# with open('output.txt', 'r') as f:
#     lines = f.read().splitlines()
#     last_line = lines[-1]
#     print last_line
# OR---------
# for i in range(1,len(lines)):
#      print(lines[-i])
# print(lines[0])


# k=''
# for x in f:
#     k+=x.replace("\n","  ")
# print(k)                                 # revove \n and print in same line

# #if using list  use * for same line
# k=[]
# for x in f:
#     k.append(x.replace("\n",""))
# print(*k)


# or use
# for x in f:
#    print(x.replace("\n",""),end=" ")


#
# for sub in test_list:
#  res.append(re.sub('\n', '', sub))


# -----------------------------------------------
#                            JOIN

#   a =["Geeks", "for", "Geeks"]

# # print the list using join function()
# print(' '.join(a))            #add space bw each elem

# # print the list by converting a list of
# # integers to string
# a = [1, 2, 3, 4, 5]

# print str(a)[1:-1]
# Output:

# Geeks for Geeks
# 1, 2, 3, 4, 5


# --------------------------------------------------------------

#            # Program to count the number of each vowels
#            # string of vowels
# vowels = 'aeiou'
# ip_str = 'Hello, have you tried our tutorial section yet?'
#           # make it suitable for caseless comparisions
# ip_str = ip_str.casefold()
#            # make a dictionary with each vowel a key and value 0
# count = {}.fromkeys(vowels,0)
#            # count the vowels
# for char in ip_str:
#    if char in count:
#        count[char] += 1
# print(count)

# -----------------------------------------------------------
# class and returning multiple values
# class Test:
#     def __init__(self):
#         self.str = "geeksforgeeks"
#         self.x = 20

#               # This function returns an object of Test
# def fun():
#     return Test()
# def arr():
#     ab=["a",1,2]
#     return ab
#               # Driver code to test above method
# t = fun()
# print(t.str)
# print(t.x)
# print(arr())      #return ab

# --------------------------------------------------
# to print in same line   print(a),
#                       print(b)

# -------------------------------------------------
#         DICTIONARY
# a={2:'a',3:'b'}
# b={7:'n'}
# a.update(b)

# -----------------------------------------------------------------
#               SORT

#                # take second element for sort
# def takeSecond(elem):
#     return elem[1]

#                # random list
# random = [(2, 2), (3, 4), (4, 1), (1, 3)]
#               # sort list with key
# random.sort(key=takeSecond,reverse=True)
#               # print list
# print('Sorted list:', random)

# Output
# Sorted list: [(4, 1), (2, 2), (1, 3), (3, 4)]
# ---------------------------

# def myFunc(e):
#   return e['year']

# cars = [
#   {'car': 'Ford', 'year': 2005},
#   {'car': 'Mitsubishi', 'year': 2000},
#   {'car': 'BMW', 'year': 2019},
#   {'car': 'VW', 'year': 2011}
# ]

# cars.sort(key=myFunc)

# print(cars)
#op  -[{'car': 'Mitsubishi', 'year': 2000}, {'car': 'Ford', 'year': 2005}, {'car': 'VW', 'year': 2011}, {'car': 'BMW', 'year': 2019}]

# --------------------------
#  sort according to the occurance  then sort word of same occurance alphbetically  BOTH IN ACSENDING

# dict1={'buz':2,'fiz':4,'hao':1,'cat':2,'a':2}
# li=[]

# for m,n in dict1.items():
#     li.append([m,n])
# print(li)

# def takeSecond(elem):
#     return (elem[1],elem[0])

# li.sort(key=takeSecond)
# print(li)

#op - [['hao', 1], ['a', 2], ['buz', 2], ['cat', 2], ['fiz', 4]]
# ------------------
#  OCCUR IN DESCENING AND WORD IN ACSENDING

# dict1={'buz':2,'fiz':4,'hao':1,'cat':2,'a':2}
# li=[]

# for m,n in dict1.items():
#     li.append([m,n])
# print(li)

# def takeSecond(elem):
#     return (-elem[1],elem[0])

# li.sort(key=takeSecond)
# print(li)

# OP  - [['fiz', 4], ['a', 2], ['buz', 2], ['cat', 2], ['hao', 1]]

# ----------------------------------------------------------------
# DICT
# dict1.get(6,"key not found")    #search key with value 6 if not found print msg

# dict1.popitem()  last elem in dict
# dict1.pop()      first elem

# dict2=dict1.copy()
# del dict1[key]
# ------------------------------------------------------------------------------------

#                                       STRING
# numbers=[11,22,33,44,55]
# string1="numbers are:{0},{1},{2}".format(numbers[0],numbers[2],numbers[4])
# print(string1)
# OP-  numbers are:11,33,55

# str1="this is CAPITAL in line"
# print(str1)
# print(str1.capitalize())
# print(str1.casefold())  # remove case changes to lower case
# print(str1.center(30,'-'))  # place string in center then use character to fill rest
# print(str1.count("i"))
# print(str1.endswith('line'))   # OP- True
# print(str1.startswith("this"))  #OP- True

#------------------------------------------------------
#               CARTESIAN PRODUCT

# from itertools import product
# l=[[2,3],[4,5,6],[1,7,8,9]]
# a=[1,2,3]
# b=[4,5]
# print(list(product(l[0],l[1],l[2])))
#OP - [(2, 4, 1), (2, 4, 7), (2, 4, 8), (2, 4, 9), (2, 5, 1), (2, 5, 7), (2, 5, 8), (2, 5, 9), (2, 6, 1), (2, 6, 7), (2, 6, 8), (2, 6, 9), (3, 4, 1), (3, 4, 7),
# (3, 4, 8), (3, 4, 9), (3, 5, 1), (3, 5, 7), (3, 5, 8), (3, 5, 9), (3, 6, 1), (3, 6, 7), (3, 6, 8), (3, 6, 9)]