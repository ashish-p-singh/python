#----------------way too long words---------------
# n=int(input())
# l=[]
# for i in range(n):
#     a=input()
#     b=len(a)
#     f=str(b-2)
#     if(b>10):
#         c=a[0]
#         d=a[b-1]
#         e=c+f+d
#         l.append(e)
#     else:
#         l.append(a)
# for x in l:
#     print(x)
#------------Bit++---------------
# a=int(input())
# x=0
# for i in range(a):
#     b=input()
#     if "++" in b:
#         x+=1
#     elif "--" in b:
#         x-=1
# print(x)
#------------------magic matrix------------------------------
# arr=[]
# for i in range(5):
#     temp=[]
#     temp=list(map(int,input().split()))
#     arr.append(temp)
# for i in range(5):
#     for j in range(5):
#         if(arr[i][j]==1):
#             r=i
#             c=j
# if(r!=2 or c!=2):
#     p=r-2
#     q=2-c
#     t=abs(p)+abs(q)
#     print(t)
# else:
#     print(0)
#---------------------------next round ------
# n,k=map(int,input().split())
# l=list(map(int,input().split()))

# b=l[k-1]
# d=0
# for x in l:
#     if(x>=b and x>0):
#         d+=1
# print(d)
#--------------------------------------
import random

choices = ["rock", "paper", "scissors"]

def get_winner(user, computer):
    if user == computer:
        return "Draw 🤝"
    
    if (user == "rock" and computer == "scissors") or \
       (user == "paper" and computer == "rock") or \
       (user == "scissors" and computer == "paper"):
        return "You Win 🎉"
    
    return "Computer Wins 💻"

def play():
    print("Welcome to Rock Paper Scissors!")
    
    while True:
        user = input("Enter rock, paper, or scissors (or 'q' to quit): ").lower()
        
        if user == 'q':
            print("Game Over 👋")
            break
        
        if user not in choices:
            print("Invalid choice, try again ❌")
            continue
        
        computer = random.choice(choices)
        
        print(f"You chose: {user}")
        print(f"Computer chose: {computer}")
        
        result = get_winner(user, computer)
        print(result)
        print("-" * 30)

play()