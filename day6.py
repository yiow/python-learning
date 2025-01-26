"""
#求最大公约数和最小公倍数
def gcd(x,y):
    if x>y:
        f=y
    else:
        f=x
    for i in range(f,0,-1):
        if x%i==0 and y%i==0:
            return i
def lcm(x,y):
    return x*y//gcd(x,y)
"""

"""
#判断是否是回文数字
def is_palindrome(num):
    temp=num
    f=0
    while num>0:
       f=f*10+num%10
       num//=10
    return f==temp
"""

"""
#判断一个数是否是素数
import math
def is_prime(num):
    if num==1:
        return False
    flag=True
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            flag=False
    return flag
"""



if __name__=='__main__':
