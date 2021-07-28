import os


class _BaseConfig:
    print("base config")


class _DevConfig(_BaseConfig):
    HOST = "0.0.0.0"
    PORT = 5000
    DEBUG = True
    print("dev")

class _ProdConfig(_BaseConfig):
    HOST = "0.0.0.0"
    PORT = 5000
    DEBUG = True
    print("prod")

# 根据环境变量获取配置
def getConfig():
    if os.getenv("env") == "prod":
        print("active config : prod")
        return _ProdConfig

    print("active config : dev")
    return _DevConfig
