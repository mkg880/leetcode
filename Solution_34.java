class Solution {
    public int[] searchRange(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        while(low <= high) {
            int mid = (high + low) / 2;
            if(nums[mid] == target) {
                low = mid;
                high = mid;
                while(low >= 0 && nums[low] == target) low--;
                if(low < 0 || nums[low] != target) low++;
                while(high < nums.length && nums[high] == target) high++;
                if(high == nums.length || nums[high] != target) high--;
                return new int[]{low, high};
            } else if(nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return new int[]{-1, -1};
    }
}