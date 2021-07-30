

#### 电容型号OCR识别接口

**METHOD:** `POST`

**URL:** `http://192.168.1.201:5000/ocr/wrongData`
    
**参数：** 

| 参数 |  位置 |  说明 |
| ----- | ---- | ---- |
| file | body | 图片文件，必填 |
| device_type | body | 当前批次型号，必填 |

**返回值：**
{
    "code": 0,
    "msg": "success",
    "data": {
        "wrong_boxes": [
            [
                [
                    9.0,
                    78.0
                ],
                [
                    230.0,
                    76.0
                ],
                [
                    231.0,
                    101.0
                ],
                [
                    10.0,
                    103.0
                ]
            ]
        ],
        "wrong_txts": [
            "35V470uF35y470F35"
        ]
    }
}