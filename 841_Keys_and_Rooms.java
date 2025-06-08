class Solution {
    public void dfs(List<List<Integer>> rooms, int v, boolean[] visited) {
        visited[v] = true;
        for(int i : rooms.get(v)) {
            if(!visited[i]) {
                dfs(rooms, i, visited);
            }
        }
    }
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        boolean[] visited = new boolean[rooms.size()];
        dfs(rooms, 0, visited);
        for(boolean b : visited) if(!b) return false;
        return true;
    }
}