import cv2
import time
import numpy as np
from PIL import Image
from ppocr.utils.logging import get_logger
from tools.infer.utility import draw_ocr_box_txt
from tools.infer.predict_system import TextSystem
import os
logger = get_logger()

class OcrService:

    # 获取错误的产品型号数据
    def get_wrong_data(self, imageFile, args):
        text_sys = TextSystem(args)
        is_visualize = True
        font_path = args.vis_font_path
        drop_score = args.drop_score

        img = np.array(Image.open(imageFile))[:, :, :3]
        starttime = time.time()
        # 检测和识别
        dt_boxes, rec_res = text_sys(img)
        elapse = time.time() - starttime
        logger.info("Predict time : %.3fs" % elapse)

        for text, score in rec_res:
            logger.info("{}, {:.3f}".format(text, score))

        txts = ""
        if is_visualize:
            image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            boxes = dt_boxes
            txts = [rec_res[i][0] for i in range(len(rec_res))]
            scores = [rec_res[i][1] for i in range(len(rec_res))]
            # 图上画框
            draw_img = draw_ocr_box_txt(
                image,
                boxes,
                txts,
                scores,
                drop_score=drop_score,
                font_path=font_path)
            draw_img_save = "./inference_results/"
            if not os.path.exists(draw_img_save):
                os.makedirs(draw_img_save)
            cv2.imwrite(
                os.path.join(draw_img_save, os.path.basename("./0727.jpg")),
                draw_img[:, :, ::-1])
            logger.info("The visualized image saved in {}".format(
                os.path.join(draw_img_save, os.path.basename("./0727.jpg"))))

        wrong_boxes = [boxes[i].tolist() for i in range(len(boxes))]
        wrong_scores = [str(scores[i]) for i in range(len(scores))]
        result_data = {"wrong_boxes": wrong_boxes, "wrong_txts": txts, "wrong_scores": wrong_scores}
        print(result_data)

        return result_data
