```python
#创建一个字典students，key是学好，value是姓名
#学生信息在.csv里，从文件中读取并保存
file=open(r'C:\Users\Administrator\Desktop\stundents.csv','r')
```


```python
# 读取文件内容
lines = flie.readlines()
```


```python
lines
```


```python
#抽取每行de学好和姓名，保存到字典
students ={}
for line in lines:
    tmp_list=line.split(',')
    xuehao=tmp_list[0]
    xingming=tmp_list[1]
    students[xuehao]=xingming
    
print(students)    
```


```python
#从学好中随机抽取n个学好
import random

num=int(input("输入你要抽取的人数"))


#如何把字典中胡学好取成列表
xuehao_list=random.sample(students.keys(),num)

xuehao_list
```