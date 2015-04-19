#!/usr/bin/env python
#coding:UTF-8

matrix1 = [[1,2,3,4], [1,2,3,4],[1,2,3,4],[1,2,3,4]]
matrix2 = [[1,2,3,4], [1,2,3,4],[1,2,3,4],[1,2,3,4]]

def matrix_multi():
    li = []
    for i in range(len(matrix1)):
        li_ = []
        for j in range(len(matrix2[0])):
            s = 0
            for k in range(len(matrix1[0])):
                s += matrix1[i][k] * matrix2[k][j]
            li_.append(s)
        li.append(li_)
    return li

if __name__ == '__main__':
    print matrix_multi()
