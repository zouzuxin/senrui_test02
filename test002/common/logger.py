import logging
import os
import time



# 获取当前文件夹的上上层目录的路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# BASE_PATH1 = os.path.dirname(os.path.realpath(__file__))
#  os.path.join()函数用于路径拼接文件路径
LOG_PATH = os.path.join(BASE_PATH,"log")
# 定义日志文件路径，如果存在则不做改变,不存在生成文件log
# os.path.exists()就是判断括号里的文件是否存在的意思，括号内的可以是文件路径
if not os.path.exists(LOG_PATH):
    # 文件不存在，则根据LOG_PATH路径生成log文件
    os.mkdir(LOG_PATH)



class Logger():

    def __init__(self):
        #在LOG_PATH的地址上，拼接当前时间的路径，日期精确到天，
        # time.strftime()是将时间戳转换成相应的日期格式
        # format()函数简单的格式形式就是‘{}’.format()。
         # 它是通过引号中间包含花括号（'{}'）的形式通过点（.）format()形式进行函数调用
        self.lognme = os.path.join(LOG_PATH,"{}.log".format(time.strftime("%Y%m%d")))
        # logger.getlogger (name) 来实例化,使用相同的名称多次调用 getLogger() 总是会返回对相同
        self.logger = logging.getLogger("log")
        # 设置日志的级别为DEBUG，DEBUG：详细信息
        self.logger.setLevel(logging.DEBUG)
        #  Formatter 格式器用来最终设置日志信息的顺序，结构和内容
        # %(asctime)s:日志产生的时间，默认格式为msecs2003-07-0816:49:45,896
        # %(filename)s:生成日志的程序名
        # %(lineno)d:日志所针对的代码行号（如果可用的话）
        # %(levelname)s	:日志级別( DEBUG,INFO, WARNING, 'ERRORCRITICAL)
        # %(message)s:具体的日志信息
        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s'
        )
        # FileHandler类型：将日志保存到磁盘文件的处理器
        self.filelogger = logging.FileHandler(self.lognme,mode='a',encoding="utf-8")
        # 能够将日志信息输出到sys.stdout, sys.stderr 或者类文件对象（更确切点，就是能够支持write()和flush()方法的对象）
        self.console = logging.StreamHandler()
        #  设置consol的日志级别为DEBUG，即只有日志级别大于等于DEBUG的日志才会输出
        self.console.setLevel(logging.DEBUG)
        self.filelogger.setLevel(logging.DEBUG)
        # 设置filelogger的格式内容
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)
        # 将filelogger日志处理程序添加到记录器addHandler
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)


logger = Logger().logger

if __name__ == '__main__':
    # print(BASE_PATH)
    # print('\n',BASE_PATH1)
    # print(LOG_PATH)
    # print(logger)
    logger.info("------测试开始------")
    logger.debug("--------测试结束-------")