import numpy as np
import random


def test_m1():
    # 带边框矩阵
    matrix_size = 10
    border = 3
    a = np.zeros((matrix_size, matrix_size))
    for i in range(matrix_size):
        for j in range(matrix_size):
            if i<border or j<border or (matrix_size-i)<=border or (matrix_size-j)<=border:
                a[i][j] = 1
    print(a)


def test_m2(matrix_size, border, border_density):
    # 带边框矩阵
    style = 0
    a = np.ones((matrix_size, matrix_size))
    for i in range(matrix_size):
        for j in range(matrix_size):
            if i<border or j<border or (matrix_size-i)<=border or (matrix_size-j) <= border:
                # 边框的处理
                a[i][j] = random.randint(0, 1)
            else:
                count = 0
                # 获得周围8个点
                if a[i-1][j-1]==style:
                    count += 1
                if a[i-1][j]==style:
                    count += 1
                if a[i-1][j+1]==style:
                    count += 1
                if a[i][j-1]==style:
                    count += 1
                if a[i][j+1]==style:
                    count += 1
                if a[i+1][j-1]==style:
                    count += 1
                if a[i+1][j]==style:
                    count += 1
                if a[i+1][j+1]==style:
                    count += 1
                if count > border_density:
                    # 随机生成
                    a[i][j] = random.randint(0, 1)
    return a


def test_m3(matrix_size, border, border_density):
    # 带边框矩阵
    style = 0
    a = np.ones((matrix_size, matrix_size))
    for i in range(matrix_size):
        for j in range(matrix_size):
            if i<border or j<border or (matrix_size-i)<=border or (matrix_size-j) <= border:
                # 边框的处理
                a[i][j] = style
            else:
                # 获得周围8个点
                border_box = [a[i-1][j-1], a[i-1][j], a[i-1][j+1], a[i][j+1], a[i+1][j+1], a[i+1][j], a[i+1][j-1], a[i][j-1]]
                count = 0
                max = 0
                for pixel in border_box:
                    if pixel == style:
                        count += 1
                    else:
                        if count > max:
                            max = count
                        count = 0
                if max > border_density:
                    # 随机生成
                    a[i][j] = random.randint(0, 1)
    return a


if __name__=="__main__":
    print(test_m2(100, 1, 1))
