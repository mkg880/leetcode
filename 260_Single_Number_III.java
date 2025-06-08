class Solution {
    public int[] singleNumber(int[] nums) {
        HashSet<Integer> set = new HashSet<Integer>();
        for(int i : nums) {
            if(set.contains(i)) set.remove(i);
            else set.add(i);
        }
        int[] res = new int[2];
        int i = 0;
        for(int num : set) {
            res[i] = num;
            i++;
        }
        return res;
    }
}