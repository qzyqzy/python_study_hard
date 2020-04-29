import logging

# 配置输出的等级
# 或者
# DEBUG || 10

# 输出的文件是gbk格式
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S', filename='logging.log')

logging.debug('debug信息')
logging.info('正常输出信息')
logging.warning('警告信息')
logging.error('错误信息')
logging.critical('严重错误信息')

try:
    num = input('请输入数字：')
    print(int(num))
except Exception as e:
    logging.error(e)
