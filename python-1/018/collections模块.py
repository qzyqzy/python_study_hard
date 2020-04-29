# 在内置数据类型（dict、list、set、tuple）的基础上，collections模块还提供了几个额外的数据类型：Counter、deque、defaultdict、namedtuple和OrderedDict等

# namedtuple: 生成可以使用名字来访问元素内容的tuple

# 我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成
# p = (1, 2)
# 但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的
import collections

Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p, p.x)  # Point(x=1, y=2) 1

# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# 除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素

q = collections.deque([1, 2, 3, 4])
q.append(5)
q.appendleft(0)
print(list(q))  # [0, 1, 2, 3, 4, 5]

# OrderedDict
#   要保持Key的顺序，可以用OrderedDict
#   OrderedDict的Key会按照插入的顺序排列，不是Key本身排序

# defaultdict
#   使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
dic = collections.defaultdict(lambda: 5)
print(dic['a'])  # 5

c = collections.Counter('aabbbcccc')
print(c, c.get('a'))  # Counter({'c': 4, 'b': 3, 'a': 2}) 2
