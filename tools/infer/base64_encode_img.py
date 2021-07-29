import base64

if __name__ == "__main__":
    dir = '../../doc/imgs/333.jpg'
    basef = open(dir.split('.')[0] + '_base64.txt', 'w')
    with open(dir, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
        data = 'base64 encode str:%s' % s
        print(data)
        basef.write(s)

    basef.close()