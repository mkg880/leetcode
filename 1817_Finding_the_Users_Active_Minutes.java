class Solution {
    public int[] findingUsersActiveMinutes(int[][] logs, int k) {
        HashMap<Integer, HashSet<Integer>> map = new HashMap();
        for(int[] a : logs) {
            if(map.get(a[0]) == null) map.put(a[0], new HashSet<Integer>());
            map.get(a[0]).add(a[1]);
        }
        int[] sol = new int[k];
        for (Map.Entry<Integer, HashSet<Integer>> entry : map.entrySet()) {
            HashSet<Integer> value = entry.getValue();
            sol[value.size() - 1]++;
        }
        return sol;
    }
}