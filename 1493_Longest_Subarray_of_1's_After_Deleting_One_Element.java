class Solution {
    public int longestSubarray(int[] nums) {
        // int cur = 0;
        int saved = 0;
        int max = 0;
        boolean z = false;
        boolean gap = false;
        for(int i = 0; i < nums.length; i++) {
            if(!z && nums[i] == 0) z = true;
            if(i > 0 && i < nums.length - 1 && nums[i] == 0 && nums[i-1] == 1 && nums[i+1] == 1) {
                gap = true;
            }
            if(nums[i] == 1) {
                int cnt = 0;
                while( i < nums.length && nums[i] == 1) {
                    i++;
                    cnt++;
                }
                i--;
                if(gap) {
                    max = Math.max(max, saved + cnt);
                    saved = cnt;
                    gap = false;
                } else {
                    saved = cnt;
                    max = Math.max(max, cnt);
                }
            }
        }
        if(!z) return nums.length - 1;
        return max;
    }
}