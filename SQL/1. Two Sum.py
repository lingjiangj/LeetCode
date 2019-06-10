""" Method 1 - Brute Force
Time complexity : O(n^2) """
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            pass
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sums = nums[i]+nums[j]
                if sums == target:
                    return [i,j]
                    break
#Run time: 5512ms


""" Method 2 - Two-pass Hash Table
Time complexity : O(n) """
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = {}
        for i in range(len(nums)):
            key = target - nums[i]
            if key not in temp.keys():
                temp[nums[i]] = i
            else:
                return [temp[key],i]
                
#Run time: 640ms            


