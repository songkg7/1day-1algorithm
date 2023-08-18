class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        // graph
        Map<Integer, Set<Integer>> graph = new HashMap<>();
        for (int[] edge : edges) {
            graph.computeIfAbsent(edge[0], k -> new HashSet<>()).add(edge[1]);
            graph.computeIfAbsent(edge[1], k -> new HashSet<>()).add(edge[0]);
        }

        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[n];
        queue.offer(source);
        visited[source] = true;
        
        while (!queue.isEmpty()) {
            int target = queue.poll();
            if (target == destination) {
                return true;
            }

            Set<Integer> nextCandidates = graph.get(target);
            for (int cand : nextCandidates) {
                if (!visited[cand]) {
                    queue.offer(cand);
                    visited[cand] = true;
                }
            }
        }

        return false;
    }
}