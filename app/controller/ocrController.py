from flask import Blueprint, request

import os
import sys
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
    imageFile = request.files.get('file')
    if utils.hasNone(imageFile):
        return Result.error(Errors.PARAM_ERROR)

    args = utility.parse_args()
    args.det_model_dir = "./inference/det"
    args.rec_model_dir = "./inference/rec"
    args.use_gpu = False
    args.device_type = str(request.form.get("device_type"))

    result_data = ocrService.get_wrong_data(imageFile, args)
    return Result.ok(result_data)
