

import os

import jsonpath
import yaml
from api.user import user

# class ProduceToken():
        # admin的token生成
    # def admin_token(self):


      # 医生的token生成
    # def doctor_token(self):


     # 护士的token生成
    # def nurse_token(self):


if __name__ == '__main__':
        datas = {'client_id': 'pcclient', 'client_secret': 'HdiS&Pc!', 'grant_type': 'HDIS', 'scope': 'api1',
                 'username': 'admin', 'password': 'E10ADC3949BA59ABBE56E057F20F883E',
                 'instid': '714DBCB5-9C8F-4048-8AAF-DA7549BBF5C0'}
        header = {
            "Accept":"application/json, text/plain, */*",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "Connection":"keep-alive",
            "Content-Length":"198",
            "Content-Type":"application/json",
            "Host":"dev.api.senruisoft.com",
            "Origin":"http://dev.pad.senruisoft.com",
            "Referer":"http://dev.pad.senruisoft.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        res = user.api_token(json=datas, headers=header)
        BASE_PATH =os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # 使用os.path.join拼接进入指定文件
        data_file_path = os.path.join(BASE_PATH,"data\\all_storage\\api_token_storage","admin_token_storage.yml")
        f = open(data_file_path,'w',encoding='utf-8')
        # Authorization ="Authorization"+":"+ jsonpath.jsonpath(res.json(),"$.token_type")+" "+ jsonpath.jsonpath(res.json(),"$.access_token")
        # yaml.dump(Authorization,f)
        print()