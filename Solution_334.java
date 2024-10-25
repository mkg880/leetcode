class Solution {
    public boolean increasingTriplet(int[] nums) {
        if(nums.length < 3) return false;
        int[] min = new int[nums.length];
        int[] max = new int[nums.length];
        min[0] = Integer.MAX_VALUE;
        min[1] = nums[0];
        max[nums.length - 1] = Integer.MIN_VALUE;
        max[nums.length - 2] = nums[nums.length - 1];
        for(int i = 2; i < nums.length; i++) {
            min[i] = Math.min(min[i-1], nums[i-1]);
            max[nums.length - i - 1] = Math.max(max[nums.length - i], nums[nums.length - i]);
        }
        for(int i = 1; i < nums.length - 1; i++) {
            if(nums[i] > min[i] && nums[i] < max[i]) return true;
        }
        return false;
    }
}