class Solution {
public:
    int result(vector<int>& dp,vector<int>& nums, int i){
        if (i<0) return 0;
        if (dp[i]!=-1) return dp[i];
        return dp[i]=max(result(dp,nums,i-2)+nums[i],result(dp,nums, i-1));
    }
    int rob(vector<int>& nums) {
        vector<int> dp(size(nums),-1);
         return(result(dp,nums,nums.size()-1));
    }
};