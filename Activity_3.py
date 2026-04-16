# Sort an array (Merge Sort)
def sortArray(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = sortArray(nums[:mid])
    right = sortArray(nums[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result + left[i:] + right[j:]

# Top K frequent elements
from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    return [item[0] for item in count.most_common(k)]

# Median from data stream
import heapq

class MedianFinder:
    def _init_(self):
        self.small = []  # max heap
        self.large = []  # min heap

    def addNum(self, num):
        heapq.heappush(self.small, -num)

        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2

# Course Schedule
from collections import defaultdict

def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[a].append(b)

    visited = [0] * numCourses

    def dfs(node):
        if visited[node] == 1:
            return False
        if visited[node] == 2:
            return True

        visited[node] = 1
        for nei in graph[node]:
            if not dfs(nei):
                return False
        visited[node] = 2
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False

    return True

# Merge intervals
def merge(intervals):
    intervals.sort()
    result = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])

    return result
