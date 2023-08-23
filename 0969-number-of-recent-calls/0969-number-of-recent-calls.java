class RecentCounter {

    TreeMap<Integer, Integer> map = new TreeMap<>();

    public RecentCounter() {
        
    }
    
    public int ping(int t) {
        int startKey = t - 3000;
        map.put(t, t);
        var tailMap = map.tailMap(startKey);
        return tailMap.size();
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */