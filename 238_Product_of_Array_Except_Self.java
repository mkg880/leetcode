class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] pre = new int[nums.length];
        int[] suf = new int[nums.length];
        pre[0] = 1;
        suf[nums.length - 1] = 1;
        for(int i = 1; i < nums.length; i++) {
            pre[i] = pre[i-1] * nums[i-1];
            suf[nums.length - i - 1] = suf[nums.length - i] * nums[nums.length - i];
        }
        int[] res = new int[nums.length];
        for(int i = 0; i < nums.length; i++) {
            res[i] = pre[i] * suf[i];
        }
        return res;
    }
}