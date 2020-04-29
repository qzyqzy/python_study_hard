import logging

logger = logging.getLogger()

# 创建一个handler，用于写入日志文件

fh = logging.FileHandler('标配版.log', encoding='utf-8')

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 设置总级别 默认输出30
# 如果要修改级别　必须先要设置总级别
logger.setLevel(10)
# 设置文件输入的级别
fh.setLevel(10)

# 设置输出到屏幕的级别
ch.setLevel(40)
# 设置格式
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 绑定
# logger对象可以添加多个fh和ch对象
logger.addHandler(fh)
logger.addHandler(ch)

logger.debug('debug信息')
logger.info('正常输出信息')
logger.warning('警告信息')
logger.error('错误信息')
logger.critical('严重错误信息')

try:
    num = input('请输入数字：')
    print(int(num))
except Exception as e:
    logger.error(e)
