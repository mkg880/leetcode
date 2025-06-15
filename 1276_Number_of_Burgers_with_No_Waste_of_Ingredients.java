class Solution {
    public List<Integer> numOfBurgers(int tomatoSlices, int cheeseSlices) {
        List<Integer> list = new ArrayList<Integer>();
        if(tomatoSlices % 2 != 0) return list;
        for(int i = 0; i <= cheeseSlices; i++) {
            int smalls = cheeseSlices - i;
            if(i * 4 + smalls * 2 == tomatoSlices) {
                list.add(i);
                list.add(smalls);
                return list;
            }
        }
        return list;
    }
}