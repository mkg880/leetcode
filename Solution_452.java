class Solution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                if(a[0] != b[0]) return Integer.compare(a[0], b[0]);
                return Integer.compare(a[1], b[1]);
            }
        });
        int i = 0, cnt = 0;
        while(i < points.length) {
            int j = i + 1;
            int min = points[i][1];
            while(j < points.length && points[j][0] <= min) {
                min = Math.min(min, points[j][1]);
                j++;
            }
            i = j;
            cnt++;
        }
        return cnt;
    }
}