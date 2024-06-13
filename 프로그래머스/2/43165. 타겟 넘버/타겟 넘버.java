
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution(new int[]{1, 1, 1, 1, 1}, 3));
    }

    public int solution(int[] numbers, int target) {
        int answer = 0;
        int[] nums = new int[numbers.length + 1];
        nums[0] = 0;
        for (int i = 0; i < numbers.length; i++) {
            nums[i + 1] = numbers[i];
        }
        Deque<Integer> deque = new ArrayDeque<>();
        deque.push(0);
        for (int i = 1; i < nums.length; i++) {
            int size = deque.size();
            for (int j = 0; j < size; j++) {
                int poll = deque.pollFirst();
                deque.addLast(poll + nums[i]);
                deque.addLast(poll - nums[i]);
            }
        }

        while (!deque.isEmpty()) {
            int poll = deque.poll();
            if (poll == target) {
                answer++;
            }
        }
        return answer;
    }


}
