import os

from common.logger import logger


class DocumentJudge():
    # 判断文件是否存在
    def document_exist(self, file_exist):
        try:
            if not os.path.exists(file_exist):
                logger.info("文件不存在01：{}".format(file_exist))
        except Exception as e:
            logger.error("判断文件是否存在的document_exist方法发生错误：{}".format(e))

    # 判断文件内容是否为空
    def document_null(self, file_exist):
        try:
            if not os.path.getsize(file_exist):
                logger.info("这是个空文件01：{}".format(file_exist))
        except Exception as e:
            logger.error("判断文件是否为空的document_null方法发生错误：{}".format(e))

    # 判断文件内容是否存在,文件是否为空
    def all_document_exist(self, file_exist):
        try:
            if not os.path.exists(file_exist):
                logger.info("文件不存在03：{}".format(file_exist))
            else:
                if not os.path.getsize(file_exist):
                    logger.info("这是个空文件04：{}".format(file_exist))
        except Exception as e:
            logger.error("判断文件是否为存在，且是否为空的all_document_exist方法发生错误：{}".format(e))

if __name__ == '__main__':
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 使用os.path.join拼接进入指定文件
    data_file_path = os.path.join(BASE_PATH, "data\\all_storage\\reques_head111", "head_login.yml")
    print("文件判断：",DocumentJudge().document_exist(data_file_path))
    print("空文件判断：",DocumentJudge().document_null(data_file_path))
    print("全部判断：",DocumentJudge().all_document_exist(data_file_path))
