class Solution {
    public int heightChecker(int[] heights) {
        int[] temp = new int[heights.length];
        for(int i = 0; i < heights.length; i++) temp[i] = heights[i];
        Arrays.sort(temp);
        int cnt = 0;
        for(int i = 0; i < heights.length; i++) if(temp[i] != heights[i]) cnt++;
        return cnt;
    }
}