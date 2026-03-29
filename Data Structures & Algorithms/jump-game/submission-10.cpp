auto static const _ = [](){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    return nullptr;
}();

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int goal=nums.size()-1;
        for(int i=nums.size()-1;i>=0;i--){
            if ((goal-i)<=nums[i]){
                goal=i;
            }
        }
        return goal==0;
    }
};
