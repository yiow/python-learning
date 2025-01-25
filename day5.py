"""
#水仙花数
for num in range(100,1000):
    sum=0
    f=num
    for i in range(3):
        sum=sum+(f%10)**3
        f//=10
    if sum==num:
        print("%d"%num,end=' ')
"""
from imaplib import Flags

"""
#正整数反转
num=int(input("输入一个数"))
reverse_num=0
while num>0:
    f=num%10
    reverse_num=reverse_num*10+f
    num//=10
print(reverse_num)
"""

"""
#百钱白鸡问题
for i in range(20):
    for j in range(33):
        k=100-i-j
        if 5*i+3*j+k/3==100:
            print("%d公鸡%d母鸡%d小鸡"%(i,j,k))
"""

"""
#CRAPS赌博游戏
from random import randint
money=1000
while money>0:
    need_go_on=True
    print("你的总资产%d"%money)
    while True:
        debt=int(input('请下赌注'))
        if 0<debt<=money:
            break
        print("余额不足")
    first=randint(1,6)+randint(1,6)
    print("摇出点数%d"%first)
    if first==7 or first==11:
        print("玩家胜利")
        money+=debt
        need_go_on=False
    elif first==2 or first==3 or first==12:
        print("庄家胜利")
        money-=debt
        need_go_on=False
    else:
        print("游戏继续")
    while need_go_on:
        num=randint(1,6)+randint(1,6)
        print("摇出点数%d"%num)
        if num==7:
            print("庄家胜利")
            money-=debt
            need_go_on=False
        elif num==first:
            print("玩家胜利")
            money+=debt
            need_go_on=False
        else:
            print("游戏继续")
print("破产游戏结束")
"""

""""
#生成斐波那契数列
pre1=0
pre2=1
for i in range(20):
    pre1,pre2=pre2,pre1+pre2
    print(pre1,end=' ')
"""

"""
#10000以内的完美术
for i in range(2,10000):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum+=j
    if sum==i:
        print(i,end=' ')
"""

"""
#100以内的素数
import math
for i in range(2,100):
    flag=True
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            flag=False
            break
    if flag:
        print(i,end=" ")
"""