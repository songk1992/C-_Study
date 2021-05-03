import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args)  throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int maxTime = Integer.parseInt(st.nextToken());
		int subNo = Integer.parseInt(st.nextToken());
		
		int[] subTime = new int[subNo + 1];
		int[] subVal = new int[subNo + 1]; 
		int[] dp = new int[maxTime + 1];
		
		
		for (int i = 1; i <= subNo; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			subVal[i] = Integer.parseInt(st.nextToken());
			subTime[i] = Integer.parseInt(st.nextToken());
		}
		
		myFn(maxTime, subTime, subVal, subNo, dp);
		
	}

	private static void myFn(int maxTime, int[] subTime, int[] subVal, int subNo, int[] dp) {
		for (int i = 1; i <= subNo; i++) {
			
			for (int j = maxTime; j - subTime[i] >= 0; j--) {
				dp[j] = Math.max(dp[j], dp[j - subTime[i]] + subVal[i]);
			}
		}
		System.out.println(dp[maxTime]);
	}

}
