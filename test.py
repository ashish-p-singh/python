# --------------------------------------
# n=int(input())
# a=str(n)
# b=a[::-1]
# if(a==b):
#     print("true")
# else:
#     print("false")
# ---------------------------------------------------
# strs=input().split(",")
# t=[]

# b=strs[0]
# for j in range(len(strs)-1):
#     u=[]
#     c=strs[j+1]
#     for k in range(min(len(b),len(c))):
#         if (j==0):
#             if b[k]==c[k]:
#                 t.append(k)
#             else:
#                 break
#         else:
#             if b[k]==c[k]:
#                 if k in t:
#                     u.append(k)
#                 else:
#                     break
#             else: 
#                 break
#     if j!=0:
#         t=u.copy()

# if len(strs)==1:
#     print(b)
# elif u:
#     d=u[-1]+1
#     print(b[0:d])
# else:
#     print("")
#----------------------------------------------------------
# s=input().strip()
# t=[]
# for i in range(len(s)):
#         if(s[i]=="("):
#             t.append("(")
#         elif(s[i]=="{"):
#             t.append("{")
#         elif(s[i]=="["):
#             t.append("[")
#         elif(s[i]==")"):
#             if t:
#                 if t[-1]=="(":
#                     t.pop()
#                 else:
#                     print("false")
#                     exit()
#             else:
#                 print("false")
#                 exit()
#         elif(s[i]=="}"):
#             if t:
#                 if t[-1]=="{":
#                     t.pop()
#                 else:
#                     print("false")
#                     exit()
#             else:
#                 print("false")
#                 exit()  
#         elif(s[i]=="]"):
#             if t:
#                 if t[-1]=="[":
#                     t.pop()
#                 else:
#                     print("false")
#                     exit()
#             else:
#                 print("false")      
#                 exit()    
# if not t:
#     print ("true")
# else:
#     print("false")
#------------------------------------------------------------------
# nums=list(map(int,input().split()))

# for i in range(len(nums)):
#     t=[0]
#     for j in range(len(nums)):
#         if nums[i]==nums[j]:
#             t[0]+=1
#     if t[0]==1:
#         print(nums[i])
#         break
# s=input()
# roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
# t=0
# p=0
# for x in s[::-1]:
#     l=roman[x]

#     if l < p:
#             t-=l
#             p=l
#     else:
#             t+=l
#             p=l
# print(t)
#--------------------------------------------
# nums=list(map(int,input().split()))
# b=len(nums)
# for i in range(len(nums)+1):
#     if i not in nums:
#         print(i)
#----------------------------------------------
# haystack=input()
# needle=input()
# if not needle:
#     print(0)
# a=needle[0]
# b=None
# for i in range(len(haystack)):
#     if haystack[i]==a:
#         b=i
#         k=i
#         for j in range(len(needle)):
#             if k>len(haystack)-1:
#                 b=None
#                 break
#             if(haystack[k]!=needle[j]):
#                   b=None
#                   break
#             else:
#                  k+=1
#         else:
#             break

# if b==None:
#     print(-1)
# else:
#     print(b)
#-----------------------------
# t=int(input())
# ab=[]
# for k in range(t):
#     n,h,l=map(int,input().split())
#     a=list(map(int,input().split()))
#     a.sort()
#     ans=0
#     i=0
#     j=len(a)-1
#     if h>=l:
#         while(i<j):
#             if (a[i]<=l and a[j]<=h):
#                 i+=1
#                 j-=1
#                 ans+=1
#             elif(a[i]>l and a[j]<=h):
#                 i+=1
#             else:
#                 j-=1
#     else:
#         while(i<j):
#             if (a[i]<=h and a[j]<=l):
#                 i+=1
#                 j-=1
#                 ans+=1
#             elif(a[i]>h and a[j]<=l):
#                 i+=1
#             else:
#                 j-=1
#     ab.append(ans)
# for x in ab:
#     print(x)
#----------------------------------------------
# a=input()
# b=input()
# a=a.lower()
# b=b.lower()
# if a<b:
#     print(-1)
# elif a==b:
#     print(0)
# elif a>b:
#     print(1)
#-------------------------------------------------
# a=input()
# b=0
# c=[]
# for x in a:
#     if x not in c:
#         c.append(x)
#         b+=1
# if b%2==0:
#     print("CHAT WITH HER!")
# else:
#     print("IGNORE HIM!")
#-------------------------------------------------------
def incre(age):
    age+=1
    return age
age=12
incre(age)
print(age)