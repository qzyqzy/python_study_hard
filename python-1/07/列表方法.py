# sort() 
# list.sort(cmp=None, key=None, reverse=False)
# reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
age=[13,4,15,16,18]
age.sort()
print(age)  # [4, 13, 15, 16, 18]

# reverse
age=[1,3,2,6]
age.sort(reverse=True)
print(age)  # [6, 3, 2, 1]

# reverse()
# 用于反向列表中元素
age=['1','age','2']
age.reverse()
print(age)  # ['2', 'age', '1']


