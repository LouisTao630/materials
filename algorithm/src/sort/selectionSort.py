#! /usr/bin/python
#coding=utf-8

# 选择排序算法
def selectionSort(nums):
    for i in range(len(nums)-1):
        minIndex = i
        for j in range(i+1,len(nums)-1):
            if(nums[j]<nums[minIndex]):
                minIndex=j
        temp = nums[i]
        nums[i] = nums[minIndex]
        nums[minIndex] = temp
    return nums

# 测试一下结果
print(selectionSort([45, 32, 8, 33, 12, 22, 19, 97]))