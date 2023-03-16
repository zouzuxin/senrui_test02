

import os

from common.document_judgment import DocumentJudge
from common.read_data import data
import jsonpath
import yaml
from api.user import user

BASE_PATH =os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 登入api通用请求头地址
head_file_path = os.path.join(BASE_PATH, "data\\all_storage\\reques_head", "head_login.yml")
# 登入api通用请求参数地址
data_file_path = os.path.join(BASE_PATH, "data\\all_storage\\api_body", "login_token_body.yml")


class ProduceToken():
        # admin的token生成
    def admin_token(self):
        # 需要存储的ap响应数据的地址
        token_file_path = os.path.join(BASE_PATH, "data\\all_storage\\api_token_storage", "admin_token_storage.yml")
        DocumentJudge().all_document_exist(token_file_path)
        res =user.api_token(json=data.load_yaml(data_file_path)["init_admin_josn"],headers =data.load_yaml(head_file_path))
        f =open(token_file_path,'w',encoding='utf-8')
        yaml.dump(res.json(),f)


      # 医生的token生成
    def doctor_token(self):
        # 需要存储的ap响应数据的地址
        token_file_path = os.path.join(BASE_PATH, "data\\all_storage\\api_token_storage", "doctor_token_storage.yml")
        DocumentJudge().all_document_exist(token_file_path)
        res = user.api_token(json=data.load_yaml(data_file_path)["init_doctor_josn"],
                             headers=data.load_yaml(head_file_path))
        f = open(token_file_path, 'w', encoding='utf-8')
        yaml.dump(res.json(), f)

        # 护士的token生成
    def nurse_token(self):
        # 需要存储的ap响应数据的地址
        token_file_path = os.path.join(BASE_PATH, "data\\all_storage\\api_token_storage", "nurse_token_storage.yml")
        DocumentJudge().all_document_exist(token_file_path)
        res = user.api_token(json=data.load_yaml(data_file_path)["init_nurse_josn"],
                             headers=data.load_yaml(head_file_path))
        f = open(token_file_path, 'w', encoding='utf-8')
        yaml.dump(res.json(), f)

login_token_create=ProduceToken()
if __name__ == '__main__':
    login_token_create.nurse_token()