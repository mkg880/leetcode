class Solution {
    public boolean DFS(int[][] graph, int s, int[] visited) {
        if(visited[s] != 0) {
            return visited[s] == 1;
        }
        visited[s] = 2;
        for(int n : graph[s]) {
            if(!DFS(graph, n, visited)) {
                return false;
            }
        }
        visited[s] = 1;
        return true;
    }
    public List<Integer> eventualSafeNodes(int[][] graph) {
        List<Integer> a = new ArrayList<>();
        int[] visited = new int[graph.length];
        for(int i = 0; i < graph.length; i++) {
            if(DFS(graph, i, visited)) a.add(i);
        }
        return a;
    }
}