class Solution {
    public int findBestValue(int[] arr, int target) {
        Arrays.sort(arr);
        int val = Math.min(target / arr.length, arr[arr.length - 1]);
        long min = Long.MAX_VALUE;
        int min_val = -1;
        int index = 0;
        long running_sum = 0;
        while(val <= arr[arr.length - 1]) {
            while(arr[index] < val) {
                running_sum += arr[index];
                index++;   
            }
            long sum = running_sum;
            sum += (arr.length - index) * val;
            long diff = Math.abs(target - sum);
            if(diff < min) {
                min = diff;
                min_val = val;
            }
            val++;
        }
        return min_val;
    }
}