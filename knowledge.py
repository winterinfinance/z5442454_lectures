# a = 433
# b = 5235
# c = 5355
# print(f'a represents number {a}, b represents number {b}, c represents number {c}.')
# print('a represents number {}, b represents number {}, c represents number {}.'.format(a, b, c))
#
# msg = "Hello World"
# name = "Winter"
# msg = f'Hello {name}'
# print(msg)
#
# #a,b为default parameters, c 为默认参数（1）
# def f(a, b):
#     value = a + b
#     return value
# def func(a, b, c=1):
#     return a + b + c
# print(func(1, 2))
# print(func(1,2,3))
#
# import yfinance
# tic = 'TSLA'
# start = '2023-01-01'
# end = None
# df = yfinance.download(tic, start, end) #download是yfinance中的一个函数
# print(df)  #可以import yfinance as yf改名
# df = df.round(2) #method
#
# from yfinance import download as dl
# df = dl(tic, start, end)
# print(df)
# print(type(df))
# print(df.shape)  #attribute 说明几行几列 有括号
# print(df.columns)
#
# a = 'I have two aPples.'
# a = a.lower()
# print(a)
# print(a. lower())
# print(a)
#
# a = 'I have cndiASNXJI.'
# a = a. lower()
# print(a)
#
# a = ' I have two aPple. '
# print(a)
# a = a.strip()  #strip是将字符串前后空格去掉
# print(a)
# a = a.lower()
# print(a)
# a = a.capitalize()
# print(a)
#
# a = ' I have MONNnjiniucs. '
# a = a.strip().lower().capitalize()
# print(a)
#
# #strip
# txt = ',,,husib,,,cnsini,,,r'
# print(txt)
# x = txt.strip()
# print(x)
# x = txt.strip(',,,hus')
# print(x)
#
# #index slicing
# a = 'how are you?'
# print(len(a))
# # index - string, list, tuple,,,ordered objects []
# print(a[4])
# print(a[11])
# print(a[-1])
# #slicing - <start index>:<end index(the earliest before the positions>)
# print(a[0:5])#不到5 到第四位
# print(a[3:])#从第三位到最后一位
# print(a[:])#从头到尾
#
# #compound types of objects
# #primitive不可改变
# #tuple元组
#
# # List
# L = [1, 2, 3, True, 'hello', None]
# print(L)
#
# # List特征一 ordered structure-index
# List_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# print(type(List_1))
# print(List_1[15])
# print(List_1[1:6])#从第1位到第五位
# print(type(List_1[1:6]))
# print(List_1[:])#全部
# print(List_1[::]) #start:end:interval
# print(List_1)
# print(List_1[1:12:2])
# print(List_1[1:12]) #这一种和下面这一种一样 意味着interval == 1
# print(List_1[1:12:1])
# print(List_1[-1:-10:-2]) #从最后一个到第-9个
#
#
# # List特征二 mutable structure
# # change the list element directly
# List_2 = [1, 2, 3]
# print(List_2)
# List_2[0] = 100
# print(List_2)
#
# # add an element append
# List_2 = [1, 2, 3]
# List_2.append(4)
# print(List_2)
# List_2.append(['hi', 4])
# print(List_2)
# print(len(List_2))
#
# List_2 = [1, 2, 3]
# List_2.extend([4, 2, 5])
# print(List_2)
# print(len(List_2))
#
# #insert 在第1位前面插入
# b = [1, 2, 3]
# b.insert(1, 54)
# print(b)
#
# list_w = [1, 4, 20, 15]
# #方法一
# list_w.sort()
# print(list_w) #sort默认从小到大排序
# list_w.sort(reverse=True) #从大到小排序
# print(list_w)
# list_w.sort(reverse=False)
# print(list_w)
# #方法二
# list_w = sorted(list_w)
# print(list_w)
#
# #字符串排序
# list_s = ['whini', 'apple', 'pear']
# list_s.sort() #方法一
# print(list_s)
# list_s = sorted(list_s) #方法二
# print(list_s)
#
# #reverse
# list_o = [1, 2, 5, 2, 7, 0]
# print(list_o)
# list_o.reverse()
# print(list_o)
#
# #删减element
# list_p = [4, 2, 8]
# list_p.pop()
# print(list_p)
# list_p.pop(1)
# print(list_p)
#
#
# list_1 = [1, 2, 5]
# list_1.pop(-3)
# print(list_1)
# list_1.pop()
# print(list_1)
#
# #空列表
# list = []
# print(list)
# print(len(list))
#
# #tuple
# t = (1, 2, 3, 4)
# print(t[:3])
# #tuple unpacking
# a, b = 1, 2
# print(a)
# print(b)
# a, b = (1, 2)
# (a, b) = 1, 2
# (a, b) = (1, 2)
# print(a)
# print(b)
#
# #set集合
# s = {1, 2, 3}
# print(s)
# s = {1, 1, 4, 5, 3, 3}
# print(s)
# #set没有顺序 不能定位到哪个数字
# s1 = {1, 2, 3}
# s1.add(4)
# print(s1)
# s1.add(3)
# print(s1)
#
#
# s = {2, 3, 4}
# s.remove(2)
# print(s)
#
# #dic字典 - key:value
#
# #无法索引
#
# marksd = {1:23, 2:53, 9:42, 0:23}
# print(marksd[1])
#
# anna = [90, 92, 95]
# ben = [92, 93, 96]
# carol = [96, 94, 98]
# assessment = {'Anna': anna, 'Ben': ben, 'Carol': carol}
# print(assessment)
# print(assessment['Ben'])
# assessment['Ben'][0] = 98 #修改Ben的成绩
# print(assessment)
#
#
# #string.split()method - 括号里default value是' ', 也就是以空格为split条件，返回的是分开string里的单词list
# sentence = 'How are you?'
# sentence_list = sentence.split()
# print(sentence_list)
# print(sentence.split('w'))
#
# #join() convert list of strings to string
# a = ['a', 'b', 'c', 'd', 'e']
# b = ''.join(a)
# print(b)
# c = ' '.join(a)
# print(c)
# d = '1'.join(a)
# print(d)
#
# #list insert()menthod
# list_a = [1, 4, 4]
# list_b = list_a.append(0)
# print(list_a)
# print(list_b)
#
# #instances and copies
#
# #conditional
# a = 1
# b = 2
# if b > a:
#     print('Ok')
# if b < a:
#     print('Y')
#
# #布尔值
# # 隐式判断
# eat = True
# if eat == True: #直接看这个值是不是TRUE
#     print('I have dinner.')
# if eat == False:
#     print('a')
# if eat is True: #is比较的两者是否TRUE/false的值 instance
#     print('I am big')
#
# a = 4
# if a == True:
#     print('IAN') #==判断的是 值本身是否相等
# if a:    #看PPT 逻辑测试 只要a的值不是0 都能打印出
#     print('我是猪')
# if a is True:
#     print('dew') #4是整数不是布尔值 所以二者不一样 看值的类型
#
# a = ()
# if a:
#     print('xdwc') #看表格（PPT)空的都不会打印出来
#
# a = ['hi']
# b = ['hi']
# print(a == b)
# print(a is b)
#
# a = 'hi'
# if a == 'hello':
#     print('hello')
# else:
#     print('hi')
#
# a = 100
# if a == 312:
#     print(323)
# elif a == 309:
#     print(309)
# else:
#     print(a)
#
# a = 1
# if a == 1:
#     print('a is 1')
# elif a + 1 == 2:
#     print('a + 1 = 2')
# else:
#     print(a)
# # 因为python自上而下执行 满足了就会跳出
#
# #loops
# list_q = [1, 2, 3, 4, 5, 6]
# for i in list_q:
#     print(i) #列表是有序的 所以按顺序打印 i是临时变量 也可以是element
#
#     dic_q = {'one': 1, 'two': 2, 'threee': 3}
#     for element in dic_q:
#         print(element)
#     for key in dic_q.keys():
#         print(key)
#     for x in dic_q.values():
#         print(x)
#     print(dic_q['one'])
#
#     for key in dic_q:
#         print(f'{key}: {dic_q[key]}')
#     for i in dic_q.items():
#         print(i)
#     #tuple unpacking
#     for k, v in dic_q.items():
#         print(k, v)
#
#
#     #enumerations
#     a = ['a', 'b', 'c', 'd', 'e', 'f']
#     for i in a:
#         print(i)
#     for i in enumerate(a):
#         print(i) #打印tuple(iteration, element)表示在第几次iteration
#     for i in enumerate(a, start=10):
#         print(i)
#
#
#     #range
#     for i in range(5):
#         print(i)
#     for i in range(2, 42, 6):
#         print(i)
#
#     #while loops
#     i = 0
#     while i < 10:
#         print(i)
#         i = i + 1
#     #break
#     a = [1, 2, 3, 4, 5]
#     for num in a:
#         print(a)
#         if num == 3:
#             break
#
#
# '''comprehension'''
# '''list comprehension'''
# '''target = [item for item in iterable if condition == True]'''
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
# list_append = [i for i in range(1, 31) if i % 2 != 0]
# print(list_append)
#
#
# '''dic.comprehension'''
# dic = {('Ben', 90), ('KAb', 8), ('nobji', 123)}
# asss = {}
# for name, mark in dic:
#     asss.update({name: mark})
#     print(asss)
#     asss[name] = mark
#     print(asss)
#
# dic = {('Ben', 90), ('KAb', 8), ('nobji', 123)}
# update_dic = {name: mark for name, mark in dic}
# print(update_dic)
#
# cbsihd = {"apple": 9, "bnana": 80, "nkbj": 708}
# vcsi = {}
# for key, value in cbsihd.items():
#     if key != "bnana":
#         vcsi[key] = value
#         print(vcsi)
#
#
# cb = {"apple": 9, "bnana": 80, "nkbj": 708}
# bhkvb = {key: value for key, value in cb.items() if key != "nkbj"}
# print(bhkvb)
#
#
# cb = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Sunday': 6}
# cb['Satday'] = 6
# print(cb)
# cb.pop('Sunday')
# print(cb)
#
# #直接一步到位
# cb = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Sunday': 6}
# cb['Saturday'] = cb.pop('Sunday')
# print(cb)
#
# ho = {"one": 1, "two": 2, "three": 3}
# cbn = {key for key in ho.keys()}
# print(cbn)
#
# #函数
# def sum_32(a, b):
#     return a + b
#
# def func1(a):
#     return None
# def func2(a):
#     return
# def func3(a):
#     a = a + 1
# print(func1)
# print(func2)
# print(func3)
#
# #scopes and namespaces
# #特殊字符
# # \t tab
# print('\t apple')
# print('\n banan')
# # \b
# #unicode
# print('\u23ab') #代码
# print(r'u23ab')
# print('The unicode for euro is', r'\u23ab')
#
# a = list
# b = set()
# c = tuple()
# d = dict()
# print(a, b, c, d)
#
# #     '''注释''' 与 # 用法一样
# # 例题1
# # 存储奇数
# odd_list = []
# for i in range(1,31):
#     if i % 2 != 0:
#         odd_list.append(i)
# print(odd_list)
# #comprehensions
# list_i = [i for i in range(1,31) if i % 2 != 0]
# print(list_i)
#
# # 例题2
# cb = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Sunday': 6}
# lisrfd = [key for key in cb.keys()]
# print(lisrfd )
# #如果想对名字排序 则用sorted
# names = sorted([key for key in cb.keys()])
# print(names)
# #摘取字典中的pairs in tuples and put into a list
# cb = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4}
# nj = []
# for key, value in cb.items():
#     nj.append((key, value))
# print(nj)
#
# iji = []
# for item in cb.items():
#     iji.append(item)
# print(iji)
#
# pairs = [(key, value) for key, value in cb.items()]
# print(pairs)
#
#
# #创建一个新的列表在给定其他数据结构
# num_set = [1, 2, 3, 4, 5, 6] #这是set集合
# #创建新的列表是集合里面数的平方
# n = []
# for i in num_set:
#     zae = i ** 2
#     n.append(zae)
# print(n)
# # comprehension
# nu = [i ** 2 for i in num_set]
# print(nu)
#
#
# #1.2 dic comprehension
#
# ##更新字典
# assessment = {} ##空字典
# update =[('Bn', 90), ('KAb', 8), ('nobji', 123)] #以列表方式储存update的元素
# #for name, mark in update:
# #print(name, mark)
# #assessment[name] = mark assessment.update({name, mark})
# #comprehension
# update =[('Bn', 90), ('KAb', 8), ('nobji', 123)]
# updare_1 = {name: mark for name, mark in update}
# print(updare_1)
#
#
#
# #创建新的字典
# price =  {"apple": 9, "bnana": 80, "nkbj": 708}
# njin = {}
# for key, value in price.items():
#     if key != 'apple':
#         njin[key] = value
# print(njin)
# #comprehension
# dh = {key: value for key, value in price.items() if key != 'apple'}
# print(dh)
# #如果你想要同样的变量名
# price = {key: value for key, value in price.items() if key != 'apple'}
# print(price)
#
#
# #例题3
# #改变字典的键和值 将sun改成sat
# days = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Sunday': 6}
# days['Sat'] = 6 #为啥days['Sat'] = ['Sun'] 不行
# print(days)
# days.pop('Sunday')
# print(days)
# #comprehension# #
# #ays['Sat'] = days.pop('Sunday')
# print(days)
#
# #set comprehension
# #ic = {'one': 1, 'two': 2, 'three’: 3}
# #eys = {key for key in dic.keys()}
# #rint(keys)
#
#
#
# ##functions
#
#
# #
# s = 'Hello world'
# s = s.split(' ')
# print(s)
# s = [word.upper() for word in s]
# print(s)
#
# def upper_word(string):
#     string = string.split(' ')
#     string = [word.upper() for word in string]
#     return string
# print(upper_word('hello Wantig'))
#
#
# #在列表中根据索引选择单词
# long_sentence = 'I have a big apple'
# long_sentence = long_sentence.split(' ')
# print(long_sentence)
# dj = [element for index, element in enumerate(long_sentence) if index % 2 != 0]
# print(dj)
# def cndh(string):
#     string = string.split(' ')
#     words = [element for index, element in enumerate(string) if index % 2 != 0]
#     return words
# print(cndh('Hi njnv jnvcjin'))
#
# def sum(n):
#     n = n + 1
#     s = 0
#     for i in range(n):
#         if i % 3 == 0:
#             s = s + i
#     return s
# print(sum(34))
#
# #特殊字符print('\n') print('\t') print('\b') print(r'\cbj')
# #rom utility import sae
#
#
# #week5
# list = ['csv', 'fjsiv', 'daef', 'wffe']
# list_startwith_d = [] #创建空列表 用来储存d开头的单词
# #方法一
# for word in list:
#     if word[0] == 'd':
#         list_startwith_d.append(word)
# print(list_startwith_d)
# #方法二
# for word in list:
#     if word.startswith('d'):
#         list_startwith_d.append(word)
# print(list_startwith_d)
# #修改字典元素
# assessment =  {'John a': 96, 'John b': 98, 'John c': 57, 'John d': None}
# for name in assessment.keys():
#     if not(name.startswith('John') or assessment[name] is None):
#         assessment[name] = 1000
# print(assessment)
#
# #在一个列表中奇数保留 偶数平方
# #基本结构
# l = []
# for i in range(18):
#     if i % 2 != 0:
#         l.append(i)
#     else:
#         l.append(i**2)
# print(l)
#
# #comprehension写法
# l = [i if i % 2 != 0 else i ** 2 for i in range(10)]
# print(l)
#
#
# #os模块 import import os
# # 文本文件 open()
# #open(<file>)
#
# # import yfinance as yf
# # df = yf.download('aapl', start = '2023-01-01')
# # df.to_csv('AAPL_price_csv')
# # file = open('AAPL_price_csv')
# #为何只有文件名，因为默认的working directory是这个folder
#
# #额外知识
# #import os
# #current_directory = os.getcmd() #这个表示每周代码例子的路径
# #print(current_directory)
#
# #用现在的路径想要查看csv文件用os.path.join()连接起来的就是这个文件的绝对路径
# #file = os.path.join(current_directory, 'AAPL_price_csv')
# #print(file)
# #file_object = open(file)
#
#
# #open函数第二个参数mode  r: read mode
# #file_object = open(file='AAPL_price_csv', mode = 'r')
# #mode = 'rt'  t是告诉python 这是一个文本数据 没有specify mode 的话就是默认rt 可以不写
# #mode参数前面是读取/写入模式：’w'是写入模式 'r'是读取模式 'a'append追加模式
# #后面是数据类型 这门课一般是text文本数据
#
# #调用读取这个对象的方法
# #contents = file_object.read()
# #content是字符串 print(len(content)) 为整个股价的字数
#
# #读取完要记得关闭
# #print(file_object.closed) #判断是否关闭的状态 如果真的关闭 会显示True
# #file_object.close() 为真正关闭这个文件
#
# #怎么一行一行的看信息
# #file_object = open('AAPL_price_csv')
# #不能用read 要用for循环
# #for line in file_object:
#     #print(file_object)
# #print出来 每行回空一行 这是因为自带\n
# #vd = [] for line in file_object: print(line) vd.append(line) break 只有第一条行显示出来 因为第一次迭代就结束了
# #如何打印股价出来没有空行
# #file_object = open('AAPL_price_csv')
# #for line in file_object:
# #line = line.strip()
# #print(line) 结果股价之间没有空行
#
#
#
# #next表示对于一个可迭代对象来说， 接下来的信息
# #第一次next代表文件的第一行
# #file_object = open('AAPL_price_csv')
# #cndj = next(file_object)
# #print(cndj)          结果为该股价的第一行数据
#
# #context manager 更安全的方法最后自带close()
# #contents = []
# #with open('AAPL_price_csv') as file_object:
# #    for line in file_object:
# #        line = line.strip()
#          #contents.append(line)
# #print(contents) 顶格为 true 如果与for一样空格 则为false
#
#
# #查看一个文件是否存在
# #import os
# #condition = os.path.exists('cds.csv')
#
#
# #函数
# #f = open('AAPL_price_csv', mode='r')
# #设计一个无聊的函数来打开文件
# #def open_func(pth, mode='rt'):
# #return open(pth, mode) 系统原生的函数
# #f_1 = open.func('AAPL_price_csv', mode = 'r') 函数中返回的open
# #print(f.read() == f_1.read())    返回结果为True
#
# #查看字符串里面是否包含某些字母
# #word = 'abcdefg'
# #a_exist = 'a' in word
# #print('a_exist')
#
# #设计一个只可以读取文件'r'，不能是'w'或者'a'的mode函数
# ##除非文件不存在，或者文件内容是空的，才允许w/a
# #只要函数动用了return指令，整个函数就终止了
#
#
# #Pandas Introduction
# #Pandas series
# #注意要import
# import pandas as pd
# ## simple series
# prices = [775.48, 775.22, 432.432, 53.354, 453.574, 453.754, 534.645, 534.43, 453.6, 542.574]
# dates = ['2021-09-30', '2021-10-01', '2021-10-04', '2021-10-05', '2021-10-06', '2021-10-07', '2021-10-08', '2021-10-11',
# '2021-10-12', '2021-10-13']
# #创建Series对象， 以prices为数据， 以dates为索引 看清楚data和index都是以列表作为参数， 且按照顺序一一对应
# #注意Series首字母要大写
# ser = pd.Series(data=prices, index=dates)
# print(ser)
#
# #attribute
# print(ser.index)
# print(ser.array) #查看data的方式
# print(ser.values)#查看data的方式
#
# #查看单日价格
# print(ser['2021-10-05'])
# #查看连续几天的slicing 要注意series按照index名字slice 切片包含了endpoint的股价数值
# print(ser['2021-10-11': '2021-10-13'])  #这是包含了2021.10.13的数据
#
# # Series without specified index
# num = [100, 200, 300, 400, 500]
# ser = pd.Series(data=num)
# print(ser)
# #默认index从0开始
#
#
# # # 会发现这里的字典例子是以价格作为 key，日期作为 values
# # # 如何把他们的值正确的放到一个 pandas series 里面
# swapped_dic = {775.48: '2021-09-30', 775.22: '2021-10-01', 781.53: '2021-10-04', 780.59: '2021-10-05', 782.75: '2021-10-06'}
# # #
# # # # comprehension 提取
# # 风险——无序结构的陷阱
# # prices = [key for key in swapped_dic.keys()]
# # dates = [date for date in swapped_dic.values()]
# # ser = pd.Series(data=prices, index=dates)
# # print(ser)
# # 稳妥——统一遍历
# mixed = [(key, value) for value, key in swapped_dic.items()]
# print(mixed)
# prices = [t[1] for t in mixed]
# dates = [t[0] for t in mixed]
# print(prices)
# print(dates)
#
#
# # 额外知识点
# a = [1] * 10
# print(a) #相当于extend方法
# data = [1] * 100
# index = [i for i in range(1, 101)]
# ser = pd.Series(data, index)
# print(ser)
#
#
#
# ser = pd.Series(data=prices, index=dates)
# # print(ser)
# # # example
# # # create pandas series
# # # elements from other variables
# assessment = [('Ben', 96), ('Carol', 95), ('Ann', 92), ('ken', 98)]
# #
# # # 因为每个元素都是 tuple(i, j)，所以用到 i, j 两个 variable，只提取 i
# names = [i for i, j in assessment]
# print(names)
# #
# # # 方法 2 - 只用一个 tup 做 variable，每次 iteration 都是一个 tuple(name, mark)，我们提取第一个元素 tup[0]
# names = [tup[0] for tup in assessment]
# print(names)
# #
# # # 选取成绩
# marks = [j for i, j in assessment]
# print(marks)
# #
# # 成绩作为数据，名字作为索引
# assessment_ser = pd.Series(data=marks, index=names)
# print(assessment_ser)
# #
# # # # 简洁的话，直接构造
# assessment_ser = pd.Series(data=[j for i, j in assessment], index=[i for i, j in assessment])
# # print(assessment_ser)
#
#
# #决定tic当努力尝试下载汇率在yfinance
# import yfinance as yf
# df = yf.download('CNY=X', '2023-03-01')
# print(df)
# #tic-外汇的tic要看base是不是美元来决定最后的格式
# #base
# #AAA/BBB 代表AAA货币在BBB里的价格
# #AUD/CNY 代表1澳币在人民币里的价格（1澳币等于多少人民币）
# #AAA是USD 和 AAA不是USD 有不同的区别
# #AAA等于美元情况下 tic-BBB=x
# #也就是说 AAA/BBB 指的是USD/CNY 时 CNY=X
# #当AAA不等于USD时，tic-AAABBB=X
# #看澳元走势时 即AAA是澳元， BBB是人民币
# #AUD/CNY时， tic-AUDCNY=X
#
#
# def f(AAA, BBB):
#     AAA = AAA.strip().upper()
#     BBB = BBB.strip().upper()
#     return
# #先对股票代码清洗调整 清洗完判断AAA是不是美元
# #AAA ！= USD
# #tic = f'{AAA}{BBB}'=x
#
# aud = ' aUd '
# cny = 'cNY '
# tic = f'{aud.strip().upper()}{cny.strip().upper()}=x'
# print(tic)
#
#
#
#
#
#
#
#
#
# # # DataFrame
# # # 我们之前接触的是 yfinance 下载下来的数据成 dataframe 类型
# # # 如何构建 dataframe
# #
# # # 两列的例子
# # # dates 作为 index
# adj_close = [775.48, 775.22, 781.53, 780.59, 782.75, 793.61, 785.49, 791.94, 805.72, 811.08]
# #
# vols = [17956000, 17031400, 30483300, 18432600, 14632800, 19195800, 16711100, 14200300, 22020000, 14068600]
# #
# dates = ['2021-09-30', '2021-10-01', '2021-10-04', '2021-10-05',
# '2021-10-06', '2021-10-07', '2021-10-08', '2021-10-11',
# '2021-10-12', '2021-10-13']
# # # # 注意 data 是一个字典
# # # # 每一个 key 对应 column 名字，value 对应数据列表
# # df = pd.DataFrame(data={'adjusted closing price': adj_close, 'volume': vols}, index=dates)
# # print(df)
# # # 构建 dataframe 的时候
# # # key: value 的 value 不一定要列表，也可以是 Pandas series
# # # 相当于把多个 series 结合一起就变成 dataframe
# #
# # # 分别把上面两个列表都变成 series，以 date 作为 index
# adj_close_ser = pd.Series(data=adj_close, index=dates)
# vols_ser = pd.Series(data=vols, index=dates)
# # # # 这个时候 data 里面的字典 values 是 series，也是可行的
# df = pd.DataFrame(data={'adjusted closing price': adj_close_ser, 'volume': vols_ser}, index=dates)
# # print(df)
#
#
# 第四题
# #t = "aal"
# #track = os.path.join(DATDIR, f'{t}_prc.dat')
# #print(track)
# #l = []
# #with open(track) as f:
#     #for line in file:
#         #line = line.strip()
#         #print(line)
#         #l.append(line)
# #print(l)
# tic = "abbv"
# track = os.path.join(DATDIR, f'{tic}_prc.dat')
# print(track)
# list_1 = []
# with open(track) as f:
#     for line in f:
#         line = line.strip()
#         list_1.append(line)
# print(list_1)
#
#
# def read_dat(tic):
#     track = os.path.join(DATDIR, f'{tic}_prc.dat')
#     l = []
#     with open(track) as f:
#         for line in file:
#             line = line.strip()
#             l.append(line)
#     return l
# #test = 'aapl'
# #print(read_dat(tic))
#
#
#
#
#
#
# 第五题
# d = get_tics(pth)
# q = []
# #q = None q = ['aal']
# if q is not None:
#     if len(q) == 0:
#         raise Exception
#     else:
#         for i in q:
#             if i not in d.keys():
#                 raise Exception
#
#
# def verify_tickers(tic_exchange_dic, tickers_lst=None):
#     if tickers_lst is not None:
#         if len(tickers_lst) == 0:
#             raise Exception
#         else:
#             for i in tickers_lst:
#                 if i not in tic_exchange_dic.keys():
#                     raise Exception
# #verify_tickers(extract_tic(tic), tickers_lst=None) 用空列表 aal试错
#
# def line_to_dict(line):
#     col_val = {}
#     for col_name, col_width in COLWIDTHS.items():
#         col_val = line[:col_width]
#         col_val[col_name] = col_val
#         line = line[col_width:]
#     return col_val
#
#
#
# 第六题
# def verify_cols(col_lst=None):
#     if verify_cols is not None:
#         if len(col_lst) == 0:
#             raise Exception
#         else:
#             for i in col_lst:
#                 if i not in COLUMNS:
#                     raise Exception
#
#
#
#
#
# 第5题
#
# line = '00000000000006 2013-04-110031.4405593872070343.200000743.4190043.709999084472656'
# start = 0
# end = 0
# COLUMNS = ['Volumn', 'Date', 'Adj Close', 'Close', 'Open', 'High']
# COLWIDTHS = {'Volumn': 14, 'Date': 11, 'Adj Close': 19, 'Close': 10, 'Open': 6, 'High': 20}
# r = {}
# for i in COLUMNS:
#     end = end + COLWIDTHS[i]
#     inter = line[start:end] #line[0,14]
#     line[i] = inter
#     start = end
# print(r)
#
#
# def line_to_dict(line):
#     r = {}
#     for i in COLUMNS:
#         inte = line[0:COLWIDTHS[i]]
#         r[i] = inte
#         line = line[COLWIDTHS[i]:]
#
#     return r
# result = line_to_dict(line)
# print(result)

import os
import pandas as pd
# Pandas Series Example
#exa 1
# data = [100, 200, 300, 400, 500, 600, 700, 800]
# date = ['10-01', '10-02', '10-03', '10-04', '10-05', '10-06', '10-07', '10-08']
# series = pd.Series(data=data, index=date)
# print(series)
#
# #some attribute
# print(series.shape)
# print(series.dtype)
# print(series.index)

# indexing-3 ways: .iloc - index/position based按照位置
# .loc - label based按照index名字
# [] - label position with confusing notations

# print(series)
# Series index - 选择单行 - 第三行
# （1）iloc
# d = series.iloc[2]
# print(d)
# （2）loc
# print(series.loc['10-03'])
# （3）[] 不可用原因：既可以position 又可以lable 会造成困扰
# print(series['10-03'])
# print(series[2])

# print(series.iloc[-2])
# print(series.loc['10-05'])
# print(series.iloc[::-1])

# 选择连续行 选择第2行到第6行 第六行包括
# loc的end value包含其中
# print(series.iloc[1:6])
# print(series.loc['10-02':'10-06'])
# 不建议使用这种方法
# print(series['10-02':'10-06'])

# 选择指定的行 01 03 06
# row_index = [0, 2, 5]
# print(series.iloc[row_index])
# print(series.iloc[[0, 2, 5]])
# print(series.loc[['10-01', '10-03', '10-06']])
# print(series[[0, 2, 5]])不推荐
# print(series.iloc[[2, 0, 5]])


##Pandas Series Indexing
# exm 2 index values include integers
# data = [100, 200, 300, 400, 500, 600, 700, 800]
# ind = [1, 2, 3, 4, 5, 6, 7, 8]
# ser = pd.Series(data=data, index=ind)
# print(ser)

#[]困惑的原因
# print(ser[0]) 报错原因：没有0这个标签（从1开始的标签）
# print(ser[1])
# print(ser.iloc[1]) #position
# print(ser.loc[1]) #label
#
# 选择第二行到第四行
# print(ser.iloc[1:4])
# print(ser.loc[2:4])
# print(ser[1:4])

# 选择具体的行
# index label(并非positional index) 选择1，3，4行
# print(ser.iloc[[0, 2, 3]])
# print(ser.loc[[1, 3, 4]])
# print(ser[1, 3, 4])

#Pandas Series without specific indices
# Exa 3
# data = [100, 200, 300, 400, 500, 600, 700, 800]
# ser = pd.Series(data=data)
# print(ser)
# 选择第二行
# print(ser.iloc[1])
# print(ser.loc[1])
# print(ser[1])

# 切片第二到第四 loc： end value包含
# print(ser.iloc[1:4])
# print(ser.loc[1:3])


# Pandas DataFrame
# 与Series不一样： df里面的column是有column name
# ex 1
# data_1 = [10, 20, 30 ,40, 50]
# data_2 = [100, 200, 300, 400, 500]
# data_3 = [1000, 2000, 3000, 4000, 5000]
# data_4 = [10000, 20000, 30000, 40000, 50000]
# index = ['a', 'b', 'c', 'd', 'e']
# df = pd.DataFrame(data={'first': data_1, 'second': data_2, 'third': data_3, 'fourth': data_4}, index=index)
# print(df)

# same distribute
# print(df.index)
# print(df.columns)
# print(df.size)
# print(df.shape)

# Pandas I/O - save csv file
# import toolkit_config as cfg
# data_dir = os.path.join(cfg.DATADIR, 'data')
# print(data_dir)
# pth = os.path.join(data_dir, "hd_example_1.csv")
# print(pth)
# df = pd.read_csv(pth)
# print(df)

# 查看单独的对象 200
# print(df.iloc[1, 1])
# print(df.loc['b', 'second'])

# slicing
# 一列里面多行 b到d行
# print(df.iloc[1:4, 2])
# print(df.loc['b':'d', 'third'])
# # 一行多值
# print(df.iloc[2, 1:4])
# print(df.loc['c', 'second':'fourth'])
# 选择行和列 选择'a'到'c'行 'first' 到‘third’列（包含）
# print(df.iloc[0:3, 0:3])
# print(df.iloc[:3, :3])
# print(df.loc[:'c', :'third'])

# 选择所有行 只有一列
# print(df.iloc[:, 1])
# 三种表达一个意思 只选择第二行的元素
# print(df.iloc[1, ])
# print(df.iloc[1])
# print(df.iloc[1, :])

# print(df.loc[:, 'second'])
# print(df.iloc[:, 1])
# print(df['second']) 唯一推荐用[]的地方

# 选多列 第一 三四列
# col = ['first', 'third', 'fourth']
# print(df.loc[:, col])
# print(df[col])
# int = [0, 2, 3]
# print(df.iloc[:, int])

# 选择具体的值 a c 行 第一 四列
# iloc
# row = [0, 2]
# col = [0, 3]
# print(df.iloc[row, col])
# print(df.iloc[[0, 2], [0, 3]])

# loc
# ro = ['a', 'c']
# se = ['first', 'fourth']
# print(df.loc[ro, se])
#
# print(df.loc['a':'z'])
# print(df.loc['0':'z'])
# print(df.loc['0':'c'])


# ex2
# data_1 = [10, 20, 30 ,40, 50]
# data_2 = [100, 200, 300, 400, 500]
# data_3 = [1000, 2000, 3000, 4000, 5000]
# data_4 = [10000, 20000, 30000, 40000, 50000]
# index = ['b', 'd', 'e', 'c', 'a']
# df = pd.DataFrame(data={'first': data_1, 'second': data_2, 'third': data_3, 'fourth': data_4}, index=index)
# print(df)
# print(df.loc['a':'c'])
# print(df.loc['e': 'a'])



# ex3
# numpy库也是一个非常常见的数据处理工具
# not-a-number介绍一种特殊值， 背后也是float类型 当我们数据处理时，会遇到数据缺失的问题， 可以使用np.nan
# import numpy as np
# num = np.nan
# print(num)
# print(type(num))

# # numpy的强大
# numbers = [1, 2, 3, 4, 5, 6]
# # array构造一个numpy array，输入参数是一个数字列表
# numbers = np.array(numbers)
# # 常见求平均值的方法
# mean = np.mean(numbers)
# print(numbers)
# print(mean)

# 有数据缺失的时候， 用np.nan代替
# numbers = [1, 2, 3, 4, np.nan, 6]
# mean = np.nanmean(numbers)
# print(mean)


# data_1 = [10, 20, 30 ,40, 50]
# data_2 = [100, 200, np.nan, 400, 500]
# data_3 = [1000, 2000, 3000, np.nan, 5000]
# data_4 = [10000, 20000, 30000, 40000, 50000]
# index = ['a', 'b', 'c', 'd', 'e']
# df = pd.DataFrame(data={'first': data_1, 'second': data_2, 'third': data_3, 'fourth': data_4}, index=index)
# print(df)
# 把缺失数据的地方赋值
# df.loc['c', 'second'] = 300
# df.loc['d', 'third'] = 4000
# print(df)
# df.iloc[2, 1] = 300
# df.iloc[3, 2] = 4000
# print(df)

# import yfinance as yf
# df = yf.download('aapl', start='2023-03-01', end='2023-03-26')
# print(df)
# df = df.round(2)
# print(df)
# select = ['Open', 'Close']
# df = df[select]
# print(df)

# # 区分SEries和DAtaframe 有没有那个标题
# ser = df['Close']
# df = df[['Close']]
# print(ser)
# print(df)