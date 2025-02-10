"""
#简单文件读写
file=open('day10.txt','a+',encoding='utf-8')
file.seek(0)

for line in file:
    print(line,end='')

lines=file.readlines()
for line in lines:
    print(line,end='')

print(file.read())

file.seek(0,2)

file.write('thanks')
file.close()
"""
"""
#文件读取异常
file=None
try:
    file=open('day10.txt','r',encoding='utf-8')
    print(file.read())
except FileNotFoundError:
    print('无法打开指定文件')
except LookupError:
    print('指定未知编码')
except UnicodeDecodeError:
    print('解码失败')
finally:
    file.close()
"""
"""
#自定义异常类型
class InputError(ValueError):
    pass
def fac(num):
    if num<0:
        raise InputError
    if num in (0,1):
        return 1
    return fac(num-1)*num
def main():
    flag=True
    while flag:
        num=int(input('输入一个数'))
        try:
            print(f'{num}的阶乘为{fac(num)}')
        except InputError:
            flag=False
if __name__=='__main__':
    main()
"""
"""
#读写二进制文件
try:
    with open('1.png','rb') as file1,open('2.png','wb') as file2:
        data=file1.read(512)
        while data:
            file2.write(data)
            data=file1.read(512)
except FileNotFoundError:
    print('无法打开指定文件')
except IOError:
    print('文件读写出现问题')
"""
"""
#序列化和反序列化
#序列化
import json
dic={
    'name':'zhr',
    'age':19,
    'cars':[
        {'brand':'BMW','max_speed':200},
        {'brand':'BYD','max_speed':190},
        {'brand':'Benz','max_speed':220}
    ]
}
print(json.dumps(dic))
with open('data.json','w') as file:
    json.dump(dic,file)
#反序列化
import json
with open('data.json','r') as file:
    dic=json.load(file)
    print(type(dic))
    print(dic)
"""
"""
#调用API
import requests
import json
response=requests.get('https://apis.tianapi.com/esports/index?key=d5fdb9942f9adf36ded1fde7d4fa8bcc&num=2')
if response.status_code==200:
    result=response.json()
    for news in result['result']['newslist']:
        print(news['ctime'])
        print(news['title'])
        print(news['description'])
        print(news['source'])
"""