import os

import requests

from api.user import user
from common.document_judgment import DocumentJudge
from common.read_data import data
import yaml
from common.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# 请求头的生成
class AllHeadsRequest():


    # 登入请求头
    def login_heads_toll(self):
        data_file_path =os.path.join(BASE_PATH,"data\\all_storage\\reques_head","head_login.yml")
        try:
            # 判断文件是否存在
            DocumentJudge().document_exist(data_file_path)
            login_heads =data.load_yaml(data_file_path)
            return login_heads
        except Exception as e:
            logger.error("login登入请求头读取时发生错误：{}".formate(e))

    # 请求头插入到yml，登入的请求透插入
    def login_heads_toll_insert(self,header):
        data_file_path =os.path.join(BASE_PATH,"data\\all_storage\\reques_head","head_login.yml")
        try:
            # 判断文件是否存在
            DocumentJudge().document_exist(data_file_path)
            # 插入方式是先清空原文件的数据，再进行插入
            f =open(data_file_path,'w',encoding='utf-8')
            yaml.dump(header,f)
        except Exception as e:
            logger.error("login登入请求头插入到yml文件时发生错误：{}".format(e))

    # api登入的请求头
    def api_heads_toll(self):
        data_file_path = os.path.join(BASE_PATH,"data\\all_storage\\reques_head","api_token_head.yml")
        try:
            api_heads=data.load_yaml(data_file_path)
            return api_heads
        except Exception as e:
            logger.error("api登入请求头读取时发生错误：{}".format(e))

    # 从head_login.yml文件获取登入的请求头，加入Authorization的标记后，将常用的api请求头插入文件
    def api_heads_toll_insert(self):
        try:
            # 普通api请求头文件
            api_file_path =os.path.join(BASE_PATH,"data\\all_storage\\reques_head","api_token_head.yml")
            DocumentJudge().document_exist(api_file_path)
            # 登入api请求头文件
            login_file_path = os.path.join(BASE_PATH,"data\\all_storage\\reques_head","head_login.yml")
            DocumentJudge().all_document_exist(login_file_path)
            # 登入api请求后，响应数据存储文件
            login_repost_file_path = os.path.join(BASE_PATH,"data\\all_storage\\api_token_storage","admin_token_storage.yml")
            DocumentJudge().all_document_exist(login_repost_file_path)

            access_token =data.load_yaml(login_repost_file_path)["access_token"]
            token_type = data.load_yaml(login_repost_file_path)["token_type"]
            # 拼接成一个完整的Authorization
            Authorization =token_type +' '+access_token
            read_data =data.load_yaml(login_file_path)
            # 将Authorization的数据插入read_data字典中
            read_data["Authorization"] =Authorization
            f = open(api_file_path,'w',encoding='utf-8')
            yaml.dump(read_data,f)
        except Exception as e:
            logger.error("api请求头生成时发生错误：{}".format(e))

AllHeadsRequest =AllHeadsRequest()

if __name__ == '__main__':
    datas = {'client_id': 'pcclient', 'client_secret': 'HdiS&Pc!', 'grant_type': 'HDIS', 'scope': 'api1',
             'username': 'admin', 'password': 'E10ADC3949BA59ABBE56E057F20F883E',
             'instid': '714DBCB5-9C8F-4048-8AAF-DA7549BBF5C0'}

    res = user.api_token(json=datas, headers=AllHeadsRequest.login_heads_toll())
    # 使用os.path.join拼接进入指定文件
    data_file_path = os.path.join(BASE_PATH, "data\\all_storage\\api_token_storage", "admin_token_storage.yml")
    f = open(data_file_path, 'w', encoding='utf-8')
    yaml.dump(res.json(), f)
    print(AllHeadsRequest.api_heads_toll_insert())
    data02 ={
      "cent_id": "0010",
      "id": "8861C3BD-0572-4C80-9280-E5E442C075CC"
    }
    url02 ="http://dev.api.senruisoft.com/api/mr/GetExamineList"
    res02 = requests.post(url=url02,json=data02,headers =AllHeadsRequest.api_heads_toll())
    print(res02.status_code)



