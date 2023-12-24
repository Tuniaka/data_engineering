import os
import numpy as np

def matrix_filter(path):
    matrix = np.load(path)
    x, y, z = [], [], []

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] > 575:
                x.append(i)
                y.append(j)
                z.append(matrix[i, j])

    np.savez('lab2/result/task2/values.npz', x, y, z)
    np.savez_compressed('lab2/result/task2/compressed.npz', x, y, z)

    size = os.path.getsize('lab2/result/task2/values.npz')
    compressed_size = os.path.getsize('lab2/result/task2/compressed.npz')

    if size > compressed_size:
        print("values.npz больше")
    elif size < compressed_size:
        print("compressed.npz больше")
    else:
        print("файлы одинаковы")



if __name__ == '__main__':
    matrix_filter('lab2/data/matrix_75_2.npy')