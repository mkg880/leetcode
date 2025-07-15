class Solution {
    public int stoneGameVI(int[] aliceValues, int[] bobValues) {
        int[][] total = new int[aliceValues.length][2];
        for(int i = 0; i < aliceValues.length; i++) {
            total[i] = new int[]{aliceValues[i] + bobValues[i], i};
        }
        Arrays.sort(total, new java.util.Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return -Integer.compare(a[0], b[0]);
            }
        });
        int a = 0;
        int b = 0;
        for(int i = 0; i < aliceValues.length; i++) {
            if (i % 2 == 0)
                a += aliceValues[total[i][1]];
            else
                b += bobValues[total[i][1]];
        }
        if(a > b) return 1;
        if (b > a) return -1;
        return 0;
    }
}