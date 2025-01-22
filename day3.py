"""
#练习1厘米英寸转换
value=float(input("输入值"))
unit=input("单位")
if unit=='in' or unit=='英寸':
    print('%f英寸=%f厘米'%(value,value*2.54))
elif unit=='cm' or unit=='厘米':
    print('%f厘米=%f英寸'%(value,value/2.54))
else:
    print('请输入有效单位')
"""
from sys import flags

"""
#成绩百分制
score=float(input("输入成绩"))
if score>=90:
    grade='A'
elif score>=80:
    grade='B'
elif score>=70:
    grade='C'
elif score>=60:
    grade='D'
else:
    grade='E'
print("成绩等级是",grade)
"""

"""
#三角形周长和面积计算公式
a=float(input('a'))
b=float(input('b'))
c=float(input('c'))
if a+b>c and a+c>b and b+c>a:
    print('周长:%f'%(a+b+c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积：%f'%area)
else:
    print('不能构成三角形')
"""
