#! /usr/bin/python
#coding=utf-8

# 插入排序
def insertionSort(arr):
    i=1
    for i in range(len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex>=0 and arr[preIndex]> current :
            arr[preIndex+1] = arr[preIndex]
            preIndex = preIndex-1
        arr[preIndex+1] = current
    return arr

# 测试一下结果
print(insertionSort([45, 32, 8, 33, 12, 22, 19, 97]))