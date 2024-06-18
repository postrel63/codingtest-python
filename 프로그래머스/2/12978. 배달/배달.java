import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

class Node {
        int to;
        int weight;

        public Node(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }

class Solution {


    public int solution(int N, int[][] road, int K) {
        int answer = 0;
        ArrayList<ArrayList<Node>> graph = new ArrayList<>();

        for (int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < road.length; i++) {
            graph.get(road[i][0]).add(new Node(road[i][1], road[i][2]));
            graph.get(road[i][1]).add(new Node(road[i][0], road[i][2]));
        }

        int[] dist = new int[N + 1];

        Arrays.fill(dist, Integer.MAX_VALUE);

        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> o1.weight - o2.weight);
         dist[1] = 0;

        
        pq.add(new Node(1, 0));

        while (!pq.isEmpty()) {
            Node curNode = pq.poll();

            if (dist[curNode.to] < curNode.weight) continue;

            for (int j = 0; j < graph.get(curNode.to).size(); j++) {
                Node adjNode = graph.get(curNode.to).get(j);
                if (dist[adjNode.to] > adjNode.weight + curNode.weight) {
                    dist[adjNode.to] = adjNode.weight + curNode.weight;
                    pq.offer(new Node(adjNode.to, dist[adjNode.to]));
                }
            }
        }

        for (int i : dist) {
            if (i <= K) {
                answer++;
            }
        }


        return answer;
    }}