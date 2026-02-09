# class ashish:
#     def __init__(a,name):
#         a.name=name
#     def getname(a):
#         return a.name
# obj=ashish("ashish kumar")
# print(obj.getname())
#----------------------------------------------
# class Understand:
#     def setvar(a,name,age=15):
#         a.name=name
#         a.age=age
#     def getvar(a):
#         return a.name,a.age
# n="Ashish Pratap Singh"
# obj1=Understand()e
# obj1.setvar(n,22)
# print(obj1.getvar())
#----------------------------------------------
# class Lol:
#     def receivedata(self):
#         name=input("Enter your name:")
#         section=input("Enter your section:")
#         self.name=name
#         self.section=section
#     def show_details(self):
#         print("Name:", self.name)
#         print("Section:", self.section)
# obj=Lol()
# obj.receivedata()
# obj.show_details()
#----------------------------------------------
# class Book:
#     name = "Abrar Ahmed Raza"
#     def __init__(self):
#         self.title  = input("Enter book title: ")
#         self.author = input("Enter book author: ")
#     def __str__(self):
#         return f"Book Title: {self.title}, Author: {self.author}, Name: {Book.name}"
# ob = Book()
# print(ob)
#----------------------------------------------
# class Bank_Account:
#     def Acc_details(self):
#         self.name=input("Enter your name:")
#         self.acc_no=int(input("Enter your account number:"))
#         self.__balance=0
#     def Savings(self):
#         self.depoist=int(input("Enter amount to be deposited:"))
#         self.__balance+=self.depoist
#     def Withdraw(self):   
#         self.withdraw= int(input("Enter amount to be withdrawn:"))
#         if self.withdraw>self.__balance:
#             print( "Insufficient balance")
#         else:
#             self.__balance-=self.withdraw
#     def display_balance(self):
#         print("Balance: ",self.__balance)
# obj=Bank_Account()
# obj.Acc_details()
# obj.Savings()
# obj.Withdraw()
# obj.display_balance()
#--------------------------------------------------
# def f(a):
# 	b=a
# 	b.append(7)
# 	return a
# print(f([1,2,3]))