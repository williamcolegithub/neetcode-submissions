class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for i in freq:
            buckets[freq[i]].append(i)
        result = []
        for bucket in reversed(buckets):
            result.extend(bucket)
        return result[:k]