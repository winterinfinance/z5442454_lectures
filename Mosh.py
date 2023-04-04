print("Wanting Yan")
print("o----")
print(' ||||')
print('*' * 10)
price = 10
price = 324
print(price)

name = 'John Smith'
age = 20
type = 'new'
print(name, age, type)

full_name = 'John Smith'
age = 20
is_new = True




name = 'wanitng Yankee'
print(name[1:-1])

course = 'wanting Yan'
print(course.find('n')) #定位字符串元素的位置
print(course.find('Yan'))
print(course.replace('Yan', 'Yanshui'))
print(course.replace('t', 'Y'))
print('Yan' in course) #判断字符串是否在变量里面
print(len(course))
print(course.title())
#method: upper lower title find replace, '' in variable


print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 10
x += 3
print(x) # 优先级（次方， 乘除， 加减）
x1 = (10 + 2) * 2 ** 2
print(x1)

#FUNCTION
x = 2.7
print(round(x))
print(abs(-1))

import math
print(math.ceil(1.4)) #向上取整
print(math.floor(1.4))#向下取整

is_hot = True
if is_hot:
    print("It's a hot day")
print("Enjoy your day")

is_hot = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
print("Enjoy your day")

is_hot = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("It's a cold day")
    print("wear warm clothes")
print("Enjoy your day")

is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day!")
    print("Drink lot of water")
elif is_cold:
    print("It's a cold day!")
    print("Wear warm clothes")
else:
    print("It's a lovely day!")
print("Enjoy your day!")

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day!")
    print("Drink lot of water")
elif is_cold:
    print("It's a cold day!")
    print("Wear warm clothes")
else:
    print("It's a lovely day!")
print("Enjoy your day!")

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")


has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print('Eligible for loan')

has_high_income = False
has_good_credit = True
if has_high_income and has_good_credit:
    print('Eligible for loan')
has_high_income = False
has_good_credit = True
if has_high_income or has_good_credit:
    print('Eligible for loan')

has_good_credit = True
has_crime_record = True
if has_good_credit and not has_crime_record:
    print("you are good")


has_good_credit = True
has_crime_record = False
if has_good_credit and not has_crime_record:
    print("you are good")


name = "J"
print(len(name))
if len(name) < 3:
    print("YOu")
elif len(name) > 50:
    print("i")
else:
    print("good")

#1:18
