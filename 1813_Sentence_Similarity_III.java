class Solution {
    public int numSimilar(String[] s1, String[] s2, int iter) {
        int i = iter == 1 ? 0 : s1.length - 1;
        int j = iter == 1 ? 0 : s2.length - 1;
        int total = 0;
        while(i >= 0 && i < s1.length && s1[i].equals(s2[j])) {
            total++;
            i += iter;
            j += iter;
        }
        return total;
    }
    public boolean areSentencesSimilar(String sentence1, String sentence2) {
        String[] s1 = sentence1.split(" ");
        String[] s2 = sentence2.split(" ");
        int front = 0;
        int back = 0;
        if(s1.length <= s2.length) {
            front = numSimilar(s1, s2, 1);
            back = numSimilar(s1, s2, -1);
        }
        else {
            front = numSimilar(s2, s1, 1);
            back = numSimilar(s2, s1, -1);
        }
        return front + back >= Math.min(s1.length, s2.length);
    }
}