var1 = ['a']
var2 = ['a']
var3 = ['a']
var4 = ['a']
print(var1)

lst1 = ['a']
print(f'This is lst1: {lst1}')

lst2 = ['b', lst1]
print(f'This is lst2: {lst2}')

lst2[1].append('c')
print(f"This is lst2 after modifying it: {lst2}")

print(f"This is lst1 after modifying lst2: {lst1}")

happy = False
if happy is True:
    print("I am happy")

print("This will print regardless of the value of happy")

happy = True
if happy is True:
    print("I am happy")

print("This will print regardless of the value of happy")

happy = 10
if happy:
    print("I am happy")

# not and or




var1 = 'a'
var2 = 'a'
var3 = ['a']
var4 = ['a']
print(var1 is var2)
print(var1 == var2)
print(var3 == var4)

a = 0
b = True
if a != 0:
   print("a is non-zero")
elif b is True:
   print("b is True")
elif a < 0 and b is True:
   print("a is negative and b is True")
else:
   print("None of the conditions above hold")

a = -1
b = True
if a != 0:
   print("a is non-zero")
elif b is True:
   print("b is True")
elif a < 0 and b is True:
   print("a is negative and b is True")
else:
   print("None of the conditions above hold")

import yfinance

start = '2020-01-01'
end = None

tickers = ["QAN.AX", "WES.AX"]
for tic in tickers:
    df = yfinance.download(tic, start, end, ignore_tz=True)
    print(df)
    tic_base = tic.lower().split('.')[0]
    df.to_csv(f'{tic_base}_stk_prc.csv')

tic = 'QAN.AX'
tic_base = tic.lower().split('.')[0]
print(tic_base)

#d.value , items
a, b, c = 1, 2, 3

list = [3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15]



for i in range(1, 4):
    for j in range(1,4):
        if i <= j:
            print(i, j)

for even in range(0, 10, 2):
    if even > 2:
        continue
print(even)

for even in range(0, 10, 2):
    if even > 2:
        continue
    print(even)
