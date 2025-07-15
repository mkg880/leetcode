class Solution {
    public double trimMean(int[] arr) {
        Arrays.sort(arr);
        double sum = 0.0;
        for(int i = arr.length / 20; i < 19 * arr.length / 20; i++) {
            sum += arr[i];
        }
        int n = 9 * arr.length / 10;
        return sum / (double) n;
    }
}