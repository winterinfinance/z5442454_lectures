def qan_tic():
    tic = "Qan.Ax"
    return tic
    print(tic)
res = qan_tic()
print(res)

def qan_tic():
    tic = "Qan.Ax"
    print(tic)
    return tic
res = qan_tic()
print(res)


def qan_tic():
    tic = "Qan.Ax"
    print(tic)
res = qan_tic()
print(res)      #没有return

def qan_tic():
    tic = "QAN.AX"
    print(tic)
    return tic
print(qan_tic) #显示出function qan_tic 的储存位置

def qan_tic():            # (1)
    tic = "QAN.AX"        # (2)
    print(tic)            # (3)
    return tic            # (4)

print("tic")

def qan_tic():
    tic = "QAN.AX"        # <-- local
    print(tic)
    return tic

tic = "WES.AX"       # global

def qan_tic():            # (1)
    tic = "QAN.AX"        # (2)
    print(tic)            # (3)
    return tic            # (4)

tic = "WES.AX"            # (5)
print(tic)          #global 先打印出global 再bulin
qan_tic()          #local 先找local



def qan_tic():            # (1)
    print(tic)            # (3)
    return tic            # (4)

tic = "WES.AX"            # (5)
print(tic)          #global 先打印出global 再bulin
qan_tic()


# LEGB 顺序

def mk_csv_name(tic, show=True):                   # (1)
    tic = tic.lower()                   # (2)
    tic_base = tic.split('.')[0]        # (3)
    return f'{tic_base}_stk_prc.csv'    # (4)

name = mk_csv_name('QAN.AX')            # (5)
print(name)



list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 29, 30, 31]

def is_even_num(numbers):
    list_1 = []
    for n in numbers:
        if n % 2 == 0:
            list_1.append(n)
    return(list_1)

print(is_even_num(list))

# This function returns an `int` instance
def add(a,b):
    return a + b

# This function returns a `NoneType` instance
def useless( ):
    pass

# This function returns a `list` instance
def mk_a_list(a, b):
    return [a, b]

list_1 = [2, 3, 10, 14, 20, 21, 25, 13, 15]
list_2 = []
for x in list_1:
    i = x ** 2
    list_2.append(i)
print(list_2)

list_1 = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
new_list = [i for i in set(list_1) if i % 2 == 0]
print(new_list)