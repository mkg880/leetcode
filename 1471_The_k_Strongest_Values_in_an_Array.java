class Solution {
    public int[] getStrongest(int[] arr, int k) {
        int[] nums = new int[k];
        Arrays.sort(arr);
        int m = arr[(arr.length - 1) / 2];
        int r = arr.length - 1;
        int l = 0;
        for(int i = 0; i < k; i++) {
            if(Math.abs(arr[l] - m) > Math.abs(arr[r] - m)) {
                nums[i] = arr[l];
                l++;
            } else {
                nums[i] = arr[r];
                r--;
            }
        }
        return nums;
    }
}