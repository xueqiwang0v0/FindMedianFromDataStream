#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:56:49 2020

用堆(Heap)来实现找到中位数

@author: xueqiwang
"""
import heapq
    
def getNumbers(file):
    f = open(file)
    nums = list(map(int, f.readlines()))
    f.close()
    return nums

class dynamicMedian:
    def __init__(self):
        self.count = 0
        self.minHeap = []
        self.maxHeap = [] # 元素为tuple，因为默认为最小堆
    
    def plugIn(self, num):
        self.count += 1
        heapq.heappush(self.minHeap, num)
        minHeap_min = heapq.heappop(self.minHeap)
        heapq.heappush(self.maxHeap, (-minHeap_min, minHeap_min))
        
        if self.count % 2 == 1:
            maxHeap_max = heapq.heappop(self.maxHeap)[1]
            heapq.heappush(self.minHeap, maxHeap_max)
    
    def getMedian(self):
        if self.count % 2 == 1:
            return self.minHeap[0]*1.
        else:
            return (self.minHeap[0] + self.maxHeap[0][1])/2


nums = [5,4,3,2,1]
medians = []
heap = dynamicMedian()

for num in nums:
    heap.plugIn(num)
    medians.append(heap.getMedian())

print(medians)