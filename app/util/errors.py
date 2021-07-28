from enum import Enum


class Errors(Enum):
    PARAM_EMPTY = {-5001: "请求参数为空"}
    PARAM_ERROR = {-5002: "请求参数错误"}
    NO_DATA = {-5003: "未查询到数据"}
    DB_DATA_ERROR = {-5004: "数据库数据有误"}
    IMAGE_ERROR = {-5005: "图片解析失败"}
    NO_FACE = {-5006: "未检测到人脸"}
    MULTI_FACE = {-5007: "检测到多个人脸"}
    SERVER_ERROR = {-5008: "服务器错误"}

    @property
    def code(self):
        return list(self.value.keys())[0]

    @property
    def msg(self):
        return list(self.value.values())[0]
