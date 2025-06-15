class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        int[] a = new int[arr.length];
        int u = 0;
        for(int i = 0; i < arr.length; i++) { 
            if(!map.containsKey(arr[i])) {
                map.put(arr[i], i);
                u++;
            }
            a[map.get(arr[i])]++;
        }
        Arrays.sort(a);
        int i = 0;
        while(a[i] == 0) {
            i++;
        }
        int num = a[i];
        while(k - num >= 0) {
            u--;
            k -= num;
            i++;
            if(i == a.length) break;
            num = a[i];
        }
        return u;
    }
}