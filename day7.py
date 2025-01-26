"""
#显示跑马灯文字
import os
import time
def main():
    content="Hello World"
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.5)
        content = content[1:] + content[0]
if __name__=='__main__':
    main()
"""
from operator import index

"""
#产生指定长度的验证码
import random
def produce_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code=""
    for i in range(code_len):
        code+=all_chars[random.randint(0,len(all_chars)-1)]
    return code
if __name__=='__main__':
    print(produce_code())
"""

"""
#输出文件后缀名
def get_suffix(filename,has_dot=False):
    pos=filename.rfind('.')
    if 0<pos<=len(filename)-1:
        if has_dot:
            return filename[pos:]
        else:
            return filename[pos+1:]
    else:
        return ''
if __name__=='__main__':
    print(get_suffix("temp1.py",True))
"""

"""
#返回一个列表中最大和次大的数
def max_1(x):
    m1,m2=(x[0],x[1]) if x[0]>x[1] else (x[1],x[0])
    for i in x[2:len(x)]:
        if i>m1:
            m2=m1
            m1=i
        elif i>m2:
            m2=i
    return m1,m2
def max_2(x):
    Max1=x[0]
    for i in x[1:len(x)]:
        if i>Max1:
            Max1=i
    x.remove(Max1) # 全局删掉了最大的元素
    Max2=x[0]
    for i in x[1:len(x)]:
        if i>Max2:
            Max2=i
    return Max1,Max2
if __name__=='__main__':
    num_list=[1,2,3,4,5,6,7,8]
    print(max_1(num_list))
    print(max_2(num_list))
    print(num_list)
"""

"""
#指定年月日看是这年的哪一天
def is_leap(year):
    return year%4==0 and year%100!=0 or year%400==0
def which_day(year,month,day):
    day_of_month=[
        [31,28,31,30,31,30,31,31,30,31,30,31],
        [31,29,31,30,31,30,31,31,30,31,30,31]
        ][is_leap(year)]
    total=0
    for i in range(month-1):
        total+=day_of_month[i]
    total+=day
    return total
if __name__=='__main__':
    print(which_day(2025,2,25))
"""

"""
#打印杨辉三角
def cmn(m,n):
    if m==0:
        return 1
    else:
        m_=1
        n_=1
        mn_=1
        for i in range(1,m+1):
            m_*=i
        for i in range(1,n+1):
            n_*=i
        for i in range(1,m-n+1):
            mn_*=i
        return m_/(n_*mn_)
def print_pascal_triangle(row):
    yh=[[] for _ in range(row)]
    for i in range(row):
        for j in range(i+1):
            yh[i].append(int(cmn(i,j)))
        replace_str=''
        for k in yh[i]:
            replace_str+=str(k)
            replace_str+=" "
        print(replace_str)

def main():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()
if __name__=='__main__':
    main()
    print_pascal_triangle(5)
"""

"""
#双色球案例
from random import randint, sample
def display(balls):
    #输出列表中的双色球号码
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    #随机选择一组号码
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('机选几注: '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()
"""

"""
#约瑟夫环
#有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
def main():
    persons=[True]*30
    counter,number,index=0,0,0
    while counter<15:
        if persons[index]:
            number += 1
        if number==9:
            persons[index]=False
            counter+=1
            number=0
        index+=1
        index%=30
    for person in persons:
        print('基'if person else '非',end='')
if __name__=='__main__':
    main()
"""

"""
#井字棋游戏
def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def win_lose(board):
    if board['TL']==board['TM']==board['TR'] and board['TL']!=' ':
        return board['TL']
    if board['ML']==board['MM']==board['MR'] and board['ML']!=' ':
        return board['ML']
    if board['BL']==board['BM']==board['BR'] and board['BL']!=' ':
        return board['BL']
    if board['TL'] == board['ML'] == board['BL'] and board['TL'] != ' ':
        return board['TL']
    if board['TM']==board['MM']==board['BM'] and board['TM']!=' ':
        return board['TM']
    if board['TR']==board['MR']==board['BR'] and board['TR']!=' ':
        return board['TR']
    if board['TL'] == board['MM'] == board['BR'] and board['TL'] != ' ':
        return board['TL']
    if board['BL']==board['MM']==board['TR'] and board['BL']!=' ':
        return board['BL']
    return ' '

def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        print_board(curr_board)
        while counter < 9 and win_lose(curr_board)==' ':
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            print_board(curr_board)
        if win_lose(curr_board)==' ':
            print("平局")
        else:
            print("%s胜利"%win_lose(curr_board))
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'
if __name__ == '__main__':
    main()
"""