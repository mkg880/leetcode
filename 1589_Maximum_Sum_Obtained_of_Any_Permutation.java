class Solution {
    public int maxSumRangeQuery(int[] nums, int[][] requests) {
        int mod = (int)(Math.pow(10, 9) + 7);
        int[] freq = new int[nums.length];
        for(int i = 0; i < requests.length; i++) {
            freq[requests[i][0]]++;
            if(requests[i][1] + 1 < freq.length) {
                freq[requests[i][1] + 1]--;
            }
        }
        for(int i = 1; i < freq.length; i++) {
            freq[i] += freq[i-1];
        }
        Arrays.sort(nums);
        Arrays.sort(freq);
        long total = 0;
        for(int i = 0; i < nums.length; i++) {
            total += ((long) nums[i] * (long) freq[i]) % mod;
        }
        return (int) (total % mod);
    }
}