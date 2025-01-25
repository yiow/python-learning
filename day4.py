"""
#判断一个数是否是素数
from math import sqrt
num=int(input('请输入一个数'))
end=int(sqrt(num))
is_prime=True
if num<=1:
    print("%d不是素数"%num)
else:
    for i in range(2,end+1):
        if num%i==0:
            is_prime=False
            break
    if not is_prime:
        print("%d不是素数"%num)
    else:
        print("%d是素数"%num)
"""

"""
#计算两个数的最大公约数和最小公倍数
num1=int(input("输入第一个数"))
num2=int(input("输入第二个数"))
if num1<num2:
    mini=num1
else:
    mini=num2
for i in range(mini,0,-1):
    if num1%i==0 and num2%i==0:
        print("%d和%d最大公约数是%d"%(num1,num2,i))
        print("%d和%d最大公倍数是%d"%(num1,num2,num1*num2//i))
        break
"""

"""
#打印一定的三角形图案
row=int(input("请输入行数"))
for i in range(row):
    for j in range(i+1):
        print("*",end='')
    print()

for i in range(row):
    for j in range(row-i-1):
        print(" ",end='')
    for k in range(i+1):
        print("*",end='')
    print()

for i in range(row):
    for j in range(row-i-1):
        print(" ",end='')
    for k in range(2*i+1):
        print("*",end='')
    print()
"""
