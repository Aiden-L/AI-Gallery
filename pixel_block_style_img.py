from PIL import Image
import json
from utils.blockbuilder import *

f = open('config.json','r')
js_obj = json.loads(f.read())
f.close()

# matrix = js_obj["matrix"]
# matrix_size = len(matrix)
matrix_size = 100
border = 1
border_density = 0


image_path = "img/example.png"
img = Image.open(image_path)
img.show()
# 变成灰度图
imageArray = np.array(img.convert('L'))

for i in range(len(imageArray)):
    for j in range(len(imageArray[i])):
        if imageArray[i][j] < js_obj["grey_level"]:
            imageArray[i][j] = 255
        else:
            imageArray[i][j] = 0

for i in range(int(len(imageArray)/matrix_size)):
    for j in range(int(len(imageArray[i])/matrix_size)):
        # 更新矩阵
        matrix = test_m3(matrix_size, border, border_density)
        for mx in range(matrix_size):
            for my in range(matrix_size):
                if matrix[mx][my]==0:
                    imageArray[i*matrix_size+mx][j*matrix_size+my] = 255


img2 = Image.fromarray(np.uint8(imageArray))
img2.show()
