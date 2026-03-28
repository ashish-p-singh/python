# a=int(input())
# l=[]

# for k in range(a):
#     s,r,c= map(int,input().split())
#     arr=list(map(int,input().split()))
#     arr.sort()
#     i=0
#     temp=0
#     while(i<s-1):
#         if(arr[i]<=r and arr[i+1]<=c):
#             temp+=1
#             i+=2
#         else:
#             i+=1  
#     l.append(temp)
# for x in l:
#     print(x)
#--------------------------------------
n=int(input())
a=str(n)
b=a[::-1]
if(a==b):
    print("true")
else:
    print("false")