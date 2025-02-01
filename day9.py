"""
#扑克游戏
from enum import Enum
import random
class Suite(Enum):
    #花色枚举
    SPADE, HEART, CLUB, DIAMOND = range(4)

class Card:
    def __init__(self,suite,face):
        self.suite=suite
        self.face=face
    def __repr__(self):
        suites = '♠♥♣♦'
        faces=['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'
    def __lt__(self, other):
        return self.face<other.face
class Poker:
    def __init__(self):
        self.cards=[Card(suite,face)
                    for suite in Suite
                    for face in range(13)]
        self.current=0
    def shuffle(self):
        #洗牌
        self.current=0
        random.shuffle(self.cards)
    def deal(self):
        #发牌
        card=self.cards[self.current]
        self.current+=1
        return card
    @property
    def has_next(self):
        return self.current<len(self.cards)
class Player:
    def __init__(self,name):
        self.name=name
        self.cards=[]
    def get_one(self,card):
        self.cards.append(card)
    def arrange(self):
        self.cards.sort()
def main():
    poker=Poker()
    players=[Player('东'),Player('西'),Player('南'),Player('北')]
    poker.shuffle()
    for _ in range(13):
        for player in players:
            player.get_one(poker.deal())
    for player in players:
        player.arrange()
        print(player.name,end=' ')
        for card in player.cards:
            print(card,end=' ')
        print()
if __name__=='__main__':
    main()
"""

"""
#工资结算系统
from abc import ABCMeta,abstractmethod
class Employee(metaclass=ABCMeta):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def get_salary(self):
        pass
class Manager(Employee):
    def get_salary(self):
        return 15000
class Programmer(Employee):
    def __init__(self,name,work_time=0):
        super().__init__(name)
        self.work_time=work_time
    def get_salary(self):
        return 200*self.work_time
class Salesman(Employee):
    def __init__(self,name,sales=0):
        super().__init__(name)
        self.sales=sales
    def get_salary(self):
        return 1800+0.05*self.sales
def main():
    employees=[Manager('小李'),Programmer('小刘',200),Salesman('小陈',300000)]
    for employee in employees:
        print(f'{employee.name}salary:{employee.get_salary()}')
if __name__=='__main__':
    main()
"""
