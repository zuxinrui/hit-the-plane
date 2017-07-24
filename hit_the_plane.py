import numpy as np
import matplotlib.pyplot as plt


def hit(N):
    a = np.random.random(2)
    row = np.floor(N * a[0])
    column = np.floor(N * a[1])
    if column == 0:
        column1 = 'A'
    elif column == 1:
        column1 = 'B'
    elif column == 2:
        column1 = 'C'
    elif column == 3:
        column1 = 'D'
    elif column == 4:
        column1 = 'E'
    elif column == 5:
        column1 = 'F'
    elif column == 6:
        column1 = 'G'
    elif column == 7:
        column1 = 'H'
    elif column == 8:
        column1 = 'I'
    elif column == 9:
        column1 = 'J'
    return row, column, column1


def plot(a, b, k):
    str1 = np.zeros((k, k))
    print str1
    str1[b, a] = 1
    plt.pcolor(str1)
    plt.title('the next hitting position:')
    plt.show()

def geneplane(N, k):
    matrix = np.zeros((k, k))
    for i in range(N):
        ran2 = np.random.random_integers(1, 4)
        if ran2 == 1:
            a = np.random.random_integers(0, k-4)
            b = np.random.random_integers(2, k-3)
            matrix[a, b] += 1
            matrix[a+1, b-2:b+3] += 1
            matrix[a+2, b] += 1
            matrix[a+3, b-1:b+2] += 1
        if ran2 == 2:
            a = np.random.random_integers(2, k-3)
            b = np.random.random_integers(0, k-4)
            matrix[a, b] += 1
            matrix[a-2:a+3, b+1] += 1
            matrix[a, b+2] += 1
            matrix[a-1:a+2, b+3] += 1
        if ran2 == 3:
            a = np.random.random_integers(3, k-1)
            b = np.random.random_integers(2, k-3)
            matrix[a, b] += 1
            matrix[a-1, b-2:b+3] += 1
            matrix[a-2, b] += 1
            matrix[a-3, b-1:b+2] += 1
        if ran2 == 4:
            a = np.random.random_integers(2, k-3)
            b = np.random.random_integers(3, k-1)
            matrix[a, b] += 1
            matrix[a-2:a+3, b-1] += 1
            matrix[a, b-2] += 1
            matrix[a-1:a+2, b-3] += 1
    return matrix


if __name__ == '__main__':
    # a, b, c = hit(10)
    # print 'the next hit is in position:', c, 10 - a
    # plot(b, a, 10)
    while True:
        ma = geneplane(3, 10)
        if np.amax(ma) == 1.0:
            break
    plt.pcolor(ma)
    plt.show()
