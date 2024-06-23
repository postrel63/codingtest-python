class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        int[][] clone = new int[triangle.length][];
        for (int i = 0; i < triangle.length; i++) {
            clone[i] = triangle[i].clone();
        }
        for (int i = 0; i < triangle.length - 1; i++) {
            for (int j = 0; j < triangle[i].length; j++) {
                if (clone[i + 1][j] < clone[i][j] + triangle[i + 1][j]) {
                    clone[i + 1][j] = clone[i][j] + triangle[i + 1][j];
                }
                if (clone[i + 1][j + 1] < clone[i][j] + triangle[i + 1][j + 1]) {
                    clone[i + 1][j + 1] = clone[i][j] + triangle[i + 1][j + 1];
                }
            }
        }

        for (int i = 0; i < clone[clone.length - 1].length; i++) {
            answer = Math.max(clone[clone.length - 1][i], answer);
        }


        return answer;
    }
}