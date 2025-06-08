class Solution {
    public int smallestRangeI(int[] nums, int k) {
        Arrays.sort(nums);
        int diff = nums[nums.length - 1] - nums[0];
        if(diff < k * 2) return 0;
        return nums[nums.length - 1] - k - (nums[0] + k);
    }
}