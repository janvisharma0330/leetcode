class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> curr;
        solution(nums, 0, curr, res);
        return res;
        
    }
    void solution(vector<int>& nums, int i, vector<int>& curr, vector<vector<int>>& res){
        res.push_back(curr);
        for (int j=i ; j<nums.size(); j++){
            curr.push_back(nums[j]);
            solution(nums,j+1,curr, res);
            curr.pop_back();
        }
    }
};