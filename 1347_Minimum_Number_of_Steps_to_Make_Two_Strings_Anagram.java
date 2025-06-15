class Solution {
    public int minSteps(String s, String t) {
        HashMap<Character, Integer> map = new HashMap<>();
        for(char c : s.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        int cnt = 0;
        for(char c : t.toCharArray()) {
            if(map.getOrDefault(c, 0) == 0) cnt++;
            else map.put(c, map.get(c) - 1);
        }
        return cnt;
    }
}