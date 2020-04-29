# 输出5-1的数字
count = 5
while count:
    print(count)
    count = count - 1

# 输出5-1之间的数字 数字等于3时停止
print('------------------------')
count = 5
while count:
    if count == 3:
        break
    print(count)
    count = count - 1

# 输出5-1之间的数字 数字等于3时不输出
print('------------------------')
count = 5
while count:
    if count == 3:
        count = count - 1
        continue
    print(count)
    count = count - 1

# while else  在循环条件为 false 时执行 else 语句块
# break 打断时不会执行 else 语句块

n = 0

while True:
    n = n + 1
    print('true1')
    if n > 0:
        break
else:
    print('false1')

while True:
    print('true2')
    break
else:
    print('false2')

while False:
    print('true3')
    break
else:
    print('false3')

n = 0

while n < 4:
    n = n + 1
    print('true5')
else:
    print('false5')
