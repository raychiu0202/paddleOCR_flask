import traceback

from flask import Flask
from flask_mysqldb import MySQL
from werkzeug.exceptions import BadRequestKeyError

import appConfig
from app.util.errors import Errors
from app.util.result import Result


class _App:
    def __init__(self):
        self.flask = Flask(__name__)
        self.config = appConfig.getConfig()
        self.flask.config.from_object(self.config)
        self.mysql = MySQL(self.flask)
        self.logger = self.flask.logger

    # 初始化Controller
    def initController(self):
        from app.controller.ocrController import ocr
        self.flask.register_blueprint(ocr)

    # 启动应用
    def start(self):
        self.flask.run(self.config.HOST, self.config.PORT)


# 初始化App
app = _App()
app.initController()


@app.flask.errorhandler(BadRequestKeyError)
def paramError(e):
    app.logger.error(e)
    return Result.error(Errors.PARAM_ERROR)


@app.flask.errorhandler(Exception)
def serverError(e):
    if app.config.__name__ == "_DevConfig":
        traceback.print_exc()
    else:
        app.logger.error(e)
    return Result.error(Errors.SERVER_ERROR)
