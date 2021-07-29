import base64

if __name__ == "__main__":
    f = open('./_base64.txt', 'rb')
    f_read = f.read()
    # f_read_decode = f_read.decode('该文件的编码方式')
    print(f_read)

    imageFile = base64.b64decode(f_read)
    print(type(imageFile))
    with open("./temp.jpg", "wb") as fp:
        fp.write(imageFile)