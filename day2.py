"""
#练习1华氏度与摄氏度转换
f=float(input("输入华氏温度"))
c=(f-32)/1.8
print(f'{f:.1f}华氏度={c:.1f}摄氏度')
"""

"""
#练习2半径计算圆的周长和面积
r=float(input('输入半径'))
print(f'周长{2*3.1415926*r:.2f}，面积{3.1415926*r*r:.2f}')
"""

"""
#练习3判断是否是闰年
year=int(input("输入年份"))
flag=year%4==0 and year%100!=0 or year%400==0
print("是否是闰年：",flag)
"""