import java.io.*;
import java.util.*;

public class BOJ_1208 {

    static int upperBound(int left, int right, int target, int[] memo) {

        while(left < right) {
            int middle = (left + right) / 2;
            if(memo[middle] > target) {
                right = middle;
            } else {
                left = middle + 1;
            }
        }
        return left;
    }

    static int lowerBound(int left, int right, int target, int[] memo) {

        while(left < right) {
            int middle = (left + right) / 2;
            if(memo[middle] >= target) {
                right = middle;
            } else {
                left = middle + 1;
            }
        }
        if(left < memo.length && memo[left] == target) {
            return left;
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());
        int[] nums = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        long answer = 0;

        int[] memo = new int[1 << (n / 2)];
        memo[0] = -4000001;
        for(int i = 1; i < 1 << (n / 2); i++) {
            int tmp = 0;
            for(int j = 0; j < n / 2; j++) {
                if((i & (1 << j)) > 0) {
                    tmp += nums[j];
                }
            }
            memo[i] = tmp;
            if(tmp == s) {
                answer += 1;
            }
        }
        Arrays.sort(memo);

        for(int i = 1; i < 1 << (n - (n / 2)); i++) {
            int tmp = 0;
            for(int j = 0; j < n - (n / 2); j++) {
                if((i & 1 << j) > 0) {
                    tmp += nums[n / 2 + j];
                } 
            }
            if(tmp == s) {
                answer += 1;
            }
            int startIdx = lowerBound(1, 1 << (n / 2), s - tmp, memo);
            if(startIdx == -1) {
                continue;
            }
            answer += upperBound(1, 1 << (n / 2), s - tmp, memo) 
                        - startIdx;
        }

        System.out.println(answer);
    }    
}
