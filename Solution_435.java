class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                if(a[0] != b[0]) return Integer.compare(a[0], b[0]);
                return Integer.compare(a[1], b[1]);
            }
        });
        int end = intervals[0][1];
        int cnt = 0;
        for(int i = 1; i < intervals.length; i++) {
            if(intervals[i][0] >= end) end = intervals[i][1];
            else if (intervals[i][1] > end) {
                cnt++;
            }
            else {
                cnt++;
                end = intervals[i][1];
            }
        }
        return cnt;
    }
}