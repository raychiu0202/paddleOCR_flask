from flask import Blueprint, request, Response

import os
import sys
import json
import base64
import tools.infer.utility as utility
from ppocr.utils.logging import get_logger
from app.service.ocrService import OcrService
from app.util import utils
from app.util.errors import Errors
from app.util.result import Result

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(__dir__)
sys.path.append(os.path.abspath(os.path.join(__dir__, '../../src')))

os.environ["FLAGS_allocator_strategy"] = 'auto_growth'

ocr = Blueprint("ocr", __name__, url_prefix="/ocr")

ocrService = OcrService()
logger = get_logger()

# 获取特征值
@ocr.route("/wrongData", methods=["POST"])
def wrongData():
    ### 入参校验和处理
    # 采用接收base64字符串的形式接收图片，base64解码成bytes字节流，然后将bytes字节流写入临时图片文件
    # device_type = str(request.args.get("device_type"))
    # device_type = str(request.form.get("device_type"))
    # device_type = str(request.values.get("device_type"))
    # device_type = str(request.json.get("device_type"))
    file_str = str(request.json.get("file"))
    print("request.headers---->", request.headers)
    print("values---->", request.values)
    print("args---->", request.args)
    print("json---->", request.json)
    imageFile = base64.b64decode(file_str)
    with open("./temp.jpg", "wb") as fp:
        fp.write(imageFile)
    # imageFile = request.files.get('file')

    if utils.hasNone(imageFile):
        return Result.error(Errors.PARAM_ERROR)

    args = utility.parse_args()
    args.det_model_dir = "./inference/det"
    args.rec_model_dir = "./inference/rec"
    args.use_gpu = False
    args.device_type = str(request.json.get("device_type"))

    ### 检测和识别
    result_data = ocrService.get_wrong_data("./temp.jpg", args)
    response = Response(get_response_params(args, result_data), mimetype='application/json')
    print("response.headers---->", response.headers)
    print("response.json---->", response.json)
    return response


# 返回参数处理
def get_response_params(args, result_data):
    # 返回的字符、位置、置信度
    describ, position, confidence = result_data["wrong_txts"], result_data["wrong_boxes"], result_data["wrong_scores"]

    # 入参传来的服务器编号、客户主机编号ID、相机编号ID
    serverID, localID, cameraID = args.serverID, args.localID, args.cameraID

    # 识别状态
    resultStatus = "Y"

    resultInfo = {
        "resultStatus": resultStatus,
        "serverID": serverID,
        "localID": localID,
        "cameraID": cameraID,
        "imageTag": "05",
        "busy": "1",
        "imageinfo":  "0,0,3",
        "spendTime": [{
            "queueTime": "10",
            "identifyTime": "30"
        }],
        "serverStatus": [{
            "cpuRate": "30",
            "gpuRate": "40"
        }],
        "resultdata": {
            "describ": describ,
            "Confidence": confidence,
            "Class": "1",
            "resultString": position
        }
    }

    return json.dumps(resultInfo, ensure_ascii=False)