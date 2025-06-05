class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        for(int i = 0; i < nums.length; i++) {
            if(i != 0 && nums[i] == nums[i-1]) continue;
            int j = i + 1;
            int k = nums.length - 1;
            while(j < k) {
                if(nums[i] + nums[j] + nums[k] == 0) {
                    result.add(new ArrayList<>(List.of(nums[i], nums[j], nums[k])));
                    j++;
                    while (j < k && nums[j] == nums[j - 1]) j++;
                } else if(nums[i] + nums[j] + nums[k] < 0) {
                    j++;
                } else k--;
            }
        }
        return result;
    }
}