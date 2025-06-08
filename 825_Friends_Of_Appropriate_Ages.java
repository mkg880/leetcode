class Solution {
    public int numFriendRequests(int[] ages) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i : ages) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }
        int count = 0;
        for(Integer i : map.keySet()) {
            for(Integer j : map.keySet()) {
                if(i > 0.5 * j + 7 && i <= j && !(i > 100 && j < 100)) {
                    if(i == j) {
                        count += map.get(i) * (map.get(i) - 1);
                    } else {
                        count += map.get(i) * map.get(j);
                    }
                }
            }
        }
        return count;
    }
}