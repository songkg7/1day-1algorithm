class Solution {
    public int eliminateMaximum(int[] dist, int[] speed) {
        // 몬스터를 다 잡는다면 n 을 리턴, 시작하자마자 lose 라면 1 을 리턴
        // 몬스터가 빨리 도착하는 순서대로 정렬, 정렬된 배열 안에는 turn 이 들어 있다.
        // 현재 turn 과 비교해서 배열 안의 turn 이 작다면 이미 도착한 것
        int turn = 0;
        int cnt = 0;
        
        int[] remainTurns = new int[dist.length];
        for (int i = 0; i < dist.length; i++) {
            int remainTurn = (int) Math.ceil(dist[i] / (speed[i] * 1.0));
            remainTurns[i] = remainTurn;
        }
        Arrays.sort(remainTurns);

        for (int remain : remainTurns) {
            if (remain <= turn) {
                return cnt;
            }
            cnt++;
            turn++;
        }

        return cnt;
    }
}