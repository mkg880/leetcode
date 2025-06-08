class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        stack<int> stack;
        stack.push(0);
        int res = 0;
        for(int i = 1; i < nums.size(); i++) {
            if(nums[i] < nums[stack.top()]) {
                stack.push(i);
            }
        }
        for(int i = nums.size() - 1; i >= 0; i--) {
            while(!stack.empty() && nums[i] >= nums[stack.top()])  {
                if(i - stack.top() > res) {
                    res = i - stack.top();
                } 
                stack.pop();
            }
        }
        return res;
    }
};