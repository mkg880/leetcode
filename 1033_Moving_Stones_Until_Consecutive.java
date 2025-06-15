class Solution {
    public int[] numMovesStones(int a, int b, int c) {
        int[] temp = new int[]{a, b, c};
        Arrays.sort(temp);
        a = temp[0];
        b = temp[1];
        c = temp[2];
        int gap1 = b - a;
        int gap2 = c - b;
        int max = (gap2 - 1) + (gap1 - 1);
        int min = 2;
        if(gap1 == 1 && gap2 == 1) min = 0;
        else if(gap1 <= 2 || gap2 <= 2) min = 1;
        return new int[]{min, max};
    }
}