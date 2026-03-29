class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> d;
        for (int i=0;i<nums.size();i++){
            if (d.contains(nums[i])){
                return {d[nums[i]],i};
            }
            d[target-nums[i]] = i;
        }
    }
};
