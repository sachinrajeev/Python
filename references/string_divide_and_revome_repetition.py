string1=input()
k=int(input())
i=0
a=[]
while i<len(string1):
    k1=""
    k1+=string1[i:i+k]
    a.append(k1)
    i+=k
a2=[]
print(a)
for i in a:
    k1=""
    for j in i:
        if j in k1:
            continue
        k1+=j
    a2.append(k1)
for i in a2:
    print(i)

/* OP
C:\Users\User\myproject\avodha\First>py test.py
AAABCADDE
3
['AAA', 'BCA', 'DDE']
A
BCA
DE

C:\Users\User\myproject\avodha\First>py test.py
AABCAAADA
3
['AAB', 'CAA', 'ADA']
AB
CA
AD
*/