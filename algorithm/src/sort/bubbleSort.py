#! /usr/bin/python
#coding=utf-8

# 准备练习写一个冒泡排序算法
# 两两比较，大的替换位置，直到所有的都比较完成。
def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

# 测试一下结果
print(bubble_sort([45, 32, 8, 33, 12, 22, 19, 97]))