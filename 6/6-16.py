#!/usr/bin/env python
#coding:UTF-8

matrix1 = [[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4]]
matrix2 = [[4,3,2,1], [4,3,2,1], [4,3,2,1], [4,3,2,1]]

def matrix_sum():
    li = []
    for i in range(len(matrix1)):
        li_ = []
        for j in range(len(matrix1[0])):
            li_.append(matrix1[i][j] + matrix2[i][j])
        li.append(li_)
    return li

if __name__ == '__main__':
    print matrix_sum()
            

