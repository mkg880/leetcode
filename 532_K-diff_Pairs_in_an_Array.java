class Solution {
    public int findPairs(int[] nums, int k) {
        int count = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }
        for(Map.Entry<Integer, Integer> e : map.entrySet()) {
            if(k == 0) {
                if(e.getValue() > 1) count++;
            }
            else if(map.containsKey(e.getKey() + k)) {
                count++;
            }
        }
        return count;
    }
}