class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 1
        for i in range(len(nums)-1):
            if nums[slow] == nums[fast]:
                fast+=1
            else:
                nums[slow+1] = nums[fast]
                fast +=1
                slow +=1
        return slow+1

        