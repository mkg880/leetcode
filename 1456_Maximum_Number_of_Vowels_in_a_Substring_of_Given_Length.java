class Solution {
    public int maxVowels(String s, int k) {
        HashSet<Character> vowels = new HashSet<Character>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
        int i = 0, j = 0, curr = 0;
        while(j < k) {
            if(vowels.contains(s.charAt(j))) {
                curr++;
            }
            j++;
        }
        int max = curr;
        while(j < s.length()) {
            if(vowels.contains(s.charAt(j))) curr++;
            if(vowels.contains(s.charAt(i))) curr--;
            max = Math.max(max, curr);
            i++;
            j++;
        }
        return max;
    }
}