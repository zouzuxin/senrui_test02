import json
import os
from configparser import ConfigParser

import yaml

from common.logger import logger


class MyConfifParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self,defaults=None):
        ConfigParser.__init__(self,defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr

class ReadFileData():

    def __init__(self):
        pass

    def load_yaml(self,file_path):
        # 调用logger方法
        # format()函数简单的格式形式就是‘{}’.format()。
        # 它是通过引号中间包含花括号（'{}'）的形式通过点（.）format()形式进行函数调用，一个参数就需要一个{}
        logger.info("加载{}文件。。。".format(file_path))
        # 循环读取yml文件中的数据
        with open(file_path,encoding='utf-8') as f :
            data = yaml.safe_load(f)
        logger.info("读取数据 ==>> {}".format(data))
        return data

    def load_json(self,file_path):
        logger.info("加載{}文件....".format(file_path))
        # 循环读取yml中的数据
        with open(file_path,encoding='utf-8')as f:
            data=json.load(f)
        logger.info("读到数据==>> {}".format(data))
        return data

    def load_ini(self,file_path):
        logger.info("加載{}文件....".format(file_path))
        # 实例化ConfigParser对象，来处理ini文件
        config = MyConfifParser()
        # 调用 read() 函数逐个字节（或者逐个字符）读取文件中的内容
        # read方法接受ini文件路径，也可以指定编码格式
        config.read(file_path,encoding='utf-8')
        # 将config里取出来的参数转换成功dict字典格式
        data =dict(config._sections)
        return data

data = ReadFileData()

if __name__ == '__main__':
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    data_file_path = os.path.join(BASE_PATH, "data", "test002.yml")
    yaml_data1 = ReadFileData().load_yaml(data_file_path)
    print(BASE_PATH)
    print(data_file_path)
    # print(yaml_data1)
    print("+++++++++++++++++++++++++++++++++++++++++++")
    data_file_pata1= os.path.join(BASE_PATH,"config","setting.ini")
    data2 = data.load_ini(data_file_pata1)["sqlserver"]
    print(data_file_pata1)
    print(data2)
    print(data2["SQLSERVER_HOST"])