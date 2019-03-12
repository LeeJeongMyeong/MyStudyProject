"""it is answer
		but not my code..."""
		
n = int(input())

tmp = input().split()
cost = [[0 for i in range(n)] for i in range(3)]

cost[0][0] = int(tmp[0])
cost[1][0] = int(tmp[1])
cost[2][0] = int(tmp[2])


for i in range(n-1):
	temp = input().split()
	
	cost[0][i+1] = int(temp[0]) + min(cost[1][i], cost[2][i])
	cost[1][i+1] = int(temp[1]) + min(cost[0][i], cost[2][i])
	cost[2][i+1] = int(temp[2]) + min(cost[0][i], cost[1][i])
	
print(min(cost[0][n-1], cost[1][n-1], cost[2][n-1]))


"""
public class BOJ1149 {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int N = scanner.nextInt();
    int[][] cost = new int[3][N];
    int r, g, b;
     
    cost[0][0] = scanner.nextInt();
    cost[1][0] = scanner.nextInt();
    cost[2][0] = scanner.nextInt();
     
    for(int i = 1; i < N; i++) {
      r = scanner.nextInt();
      g = scanner.nextInt();
      b = scanner.nextInt();
       
      cost[0][i] = r + Math.min(cost[1][i-1], cost[2][i-1]);
      cost[1][i] = g + Math.min(cost[0][i-1], cost[2][i-1]);
      cost[2][i] = b + Math.min(cost[0][i-1], cost[1][i-1]);
    }
    System.out.println(Math.min(cost[0][N-1], Math.min(cost[1][N-1], cost[2][N-1])));
    scanner.close();
  }
}


출처: https://spillmoon.tistory.com/176 [정리를 하는 블로그]

"""