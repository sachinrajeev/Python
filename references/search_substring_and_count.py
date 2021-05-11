def fn(list1,s):
    count1=0
    for i in list1:
        ind=s.index(i)
        k=ind+1
        while k<=len(s):
            count1+=s.count(s[ind:k])
            k+=1
    return count1

def minion_game(string):
    v=['a','e','i','o','u']
    listv=[]
    listc=[]
    for i in string:
        if i in v:
            listv.append(i)
        else:
            listc.append(i)
    listc1=[]
    listv1=[]
    [listc1.append(i) for i in listc if i not in listc1]
    [listv1.append(i) for i in listv if i not in listv1]
    c=fn(listc1,string)
    v=fn(listv1,string)
    print(string.count('ana'))
    if c>v:
        print("Stuart ",c)
    else:
        print('Kevin ',v)
#banana


if __name__ == '__main__':
    s = input()
    minion_game(s)



/*

C:\Users\User\myproject\avodha\First>py test2.py
banana
b 1
ba 1
ban 1
bana 1
banan 1
banana 1
n 2
na 2
nan 1
nana 1
a 3
an 2
ana 1
anan 1
anana 1
1

C:\Users\User\myproject\avodha\First>py test2.py
man
m 1
ma 1
man 1
n 1
a 1
an 1
0

C:\Users\User\myproject\avodha\First>py test2.py
man
0
Stuart  4
*/