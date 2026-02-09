# prime number
# n=int(input())
# for i in range(2,n):
#     if n%i==0:
#         print("not a prime number")
#         break
# else:   
#     print("prime number")
# spy number
# number = int(input("Enter a number: "))
# temp = number
# digit_sum = 0
# digit_product = 1
# while temp > 0:
# 	digit = temp % 10
# 	digit_sum += digit
# 	digit_product *= digit
# 	temp //= 10

# if digit_sum == digit_product:
# 	print(f"{number} is a Spy Number")
# else:
# 	print(f"{number} is not a Spy Number")
# armstrong number
# n=int(input())
# sum=0
# temp=n
# while temp>0:
#     digit=temp%10
#     sum+=digit**3 
#     temp//=10
# if sum==n:    
#     print("armstrong number")
# else:     
#     print("not a armstrong number")
# factorial
# n=int(input())
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)
# fibonacci series
# n=int(input())
# a=0
# b=1
# for i in range(n):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c
# reverse a number
# n=int(input())
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# print(rev)
# palindrome number

# n=int(input())
# temp=n
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# if temp==rev:
#     print("palindrome number")
# else:
#     print("not a palindrome number")
# sum of natural number  
# n=int(input())
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)
# sum of digit
# n=int(input())
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n//=10
# print(sum)
# count of digit
# n=int(input())
# count=0
# while n>0:
#     digit=n%10
#     count=count+1
#     n//=10
# print(count)
# count of even and odd digit
# n=int(input())
# even=0
# odd=0
# while n>0:
#     digit=n%10
#     if digit%2==0:
#         even=even+1
#     else:
#         odd=odd+1
#     n//=10
# print("even=",even)
# print("odd=",odd)
# lcm
# n1=int(input())
# n2=int(input())
# if n1>n2:
#     greater=n1
# else:
#     greater=n2
# while True:
#     if greater%n1==0 and greater%n2==0:
#         lcm=greater
#         break
#     greater+=1
# print(lcm)
# gcd
# n1=int(input())
# n2=int(input())
# while n2!=0:
#     n1,n2=n2,n1%n2
# print(n1)
# perfect number
# n=int(input())
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
# if sum==n:
#     print("perfect number")
# else:
#     print("not a perfect number")
# strong number
# n=int(input())
# sum=0
# temp=n
# while temp>0:
#     digit=temp%10
#     fact=1
#     for i in range(1,digit+1):
#         fact=fact*i
#     sum=sum+fact
#     temp//=10
# if sum==n:
#     print("strong number")
# else:
#     print("not a strong number")
# Multiplication table
# print output from n to m
# m=int(input("enter the starting number: "))
# n=int(input("enter the ending number: "))
# for i in range(m,n-1,-1):
# 	if i%2==0:
#     	print(i)
# r=int(input("enter the number of rows: "))
# for i in range(1,r+1):
# 	for j in range(1,i+1):
# 		print(j,end=" ")
# 	print()

# r=int(input("enter the number of rows: "))
# for i in range(1,r+1):
#  	print(str(i)*r)
# a=int(input())
# b=int(input())
# choice=int(input())
# if choice==1:
# 	print(a*b)
# elif choice==2:
# 	print(a-b)
# elif choice==3:
# 	print(a/b)
# else:
# 	print("invalid")
# a=int(input())
# b=int(input())
# choice=int(input())
# match choice:
# 	case 1:
# 		print(a*b)
# 	case 2:
# 		print(a-b)	
# 	case 3:
# 		print(a/b)
# 	case _:
# 		print("invalid")
# a=int(input())
# b=int(input())
# for i in range(a,b+1):
#     if i%2==0 and i%3==0:
#         print(i)
#         break
# l=input("Enter a string: ")
# for i in l:
#     if i.isdigit():
#                 print(i)
#                 break
# n=int(input("Enter a number: "))
# if(n<2):
#     print("Not a prime number")
# else:
#     for i in range(2,n):
#         if(n%i==0):
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")
# a=int(input("Enter the starting number: "))
# b=int(input("Enter the ending number: "))
# for jasvir in range(a,b+1):
#     for sahil in range(2,i):
#         if jasvir%sahil==0:
#              break 
#     else:
#         print(jasvir,end=" ")
# Syntax:def functionname(parameters):
# n=int(input("Enter a number: "))
# def check_even(n):
#     if n&2==0:
#         return "Even number"
#     else:
#        return "Odd number"
# print(check_even(n))

# def check_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact) 
# check_fact(n)
#palindrome string
# s=input("Enter a string: ")
# def check_palindrome(s):
#     if s==s[::-1]:
#         print("palindrome")
#     else:
#         print("not a palindrome")
# check_palindrome(s)
#function is over afetr return statement
# a = 20
# def func():
#     b = 10
#     print("Local variable:", b)
#     print("Global variable:", a)

# func()

# #Recursion:- A function that calls itself is known as a recursive function and the process is called recursion.
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# a = int(input("Enter a number: "))
# print("Factorial:", factorial(a))
#fibonacci series 
# def fibonacci(n):
#     pre=0
#     cur=1
#     if n<=0:
#         return n
#     else:
#         print(pre,end=" ")
#         print(cur,end=" ")
#         for i in range(2,n):
#             nex=pre+cur
#             print(nex,end=" ")
#             pre=cur
#             cur=nex
# n=int(input("Enter the number of terms: "))
# fibonacci(n)
# # fibonacci series using recursion
# def fibonacci(n):
#     if n<=0:  
#         return n
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# n=int(input("Enter the number of terms: "))
# d3={'name':'sachin','role':'actor',1:'movies'}
# for key,val in d3.items():
#     print(f"{key}:{val}")
# print("total",len(d3))
# n=int(input("how many keys do you want to store: "))
# d={input("key"):input("vl: ")for i in range (n)}
# print(d)
# d=dict(item.split(":") for item in input("enter key,vl ,").split(","))
# print(d)
# ls1 = ['game','scor','win']
# ls2 = ['pubg','kd',55]
# d1=dict(zip(ls1,ls2))
# print(d1)
# a={'name':'ashish','subj':'python','cgpa':10}
# b={'age':20,'status':'passed','cgpa':8.5}
# print(a|b)
# merge = {**a,**b}
# print(merge)
# a=[1,2,3,4]
# # for i in a:
# #     b=i**2
# #     print(b)
# # b=[x**2 for x in a]
# # print(b)
# c=[x for x in a if x%2==0]
# print(c)
#----------------RECURSION-------------------    
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# n=int(input("Enter a number: "))
#-----------------recurion reverese string----------------
# def reverse_string(str):
#     if len(str)==0:
#         return str
#     else:
#         return str[-1]+reverse_string(str[:-1])
# str=input("Enter a string: ")
# print("Reversed string:",reverse_string(str))
#------------------MAP FUNCTION-----------------
