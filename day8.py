"""
#定义类来描述数字时钟
import time
class Clock(object):
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second
    def run(self):
        self.second+=1
        if self.second==60:
            self.second=0
            self.minute+=1
            if self.minute==60:
                self.hour+=1
                self.minute=0
                if self.hour==24:
                    self.hour=0
    def show(self):
        print(f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}')
def main():
    clock1=Clock(16,0,0)
    while True:
        clock1.run()
        clock1.show()
        time.sleep(1)
if __name__=='__main__':
    main()
"""



#定义类描述平面上的点并提供移动点和计算到另一个点距离的方法
import math
class Point():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def move_to(self,x,y):
        self.x=x
        self.y=y
    def move_by(self,dx,dy):
        self.x+=dx
        self.y+=dy
    def distance(self,x,y):
        return math.sqrt((self.x-x)**2+(self.y-y)**2)
    def show(self):
        print(f'x:{self.x} y:{self.y}')
def main():
    point1=Point(0,0)
    point1.show()
    point1.move_to(1,1)
    point1.show()
    point1.move_by(1,1)
    point1.show()
    print(f'distance to (3,3):{point1.distance(3,3)}')
if __name__=='__main__':
    main()