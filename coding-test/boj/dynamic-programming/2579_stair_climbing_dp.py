'''
BOJ 2579 - Stair Climbing
Category: Dynamic Programming
Approach: Bottom-Up 
* Bottom-up
- for문으로 i= 1 -> N까지 순서대로 채움
*Top-Down
- 재귀 + 메모이제이션 
- Top-Down은 "전체 상태 공간"을 채우려는 것이 아니라, "정답을 구성하는 데 실제로 필요한 상태만" 호출합니다.
- 정답을 만들기 위한 하위 문제를 요청합니다. 
'''

'''
문제 힌트 
dp[i][cnt] = i번째 계단에 있고, 연속으로 cnt번 밟은 상태에서 얻을 수 있는 최대 점수 
'''

import sys 

def solve():   # 총 점수의 최댓값 구하기
    N = int(sys.stdin.readline())
    table = [0] + [int(sys.stdin.readline()) for _ in range(N)]
    dp = [[0]*3 for _ in range(N+1)] 

    dp[1][1] = table[1]
    if N >= 2:
        dp[2][1] = table[2]
        dp[2][2] = table[1] + table[2]

    for i in range(3, N+1):  # 3부터 N까지
        # 1칸 올라갔을 때 
        dp[i][2] = dp[i-1][1] + table[i]
        # 2칸 올라갔을 때
        dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + table[i]

    print(max(dp[N][1], dp[N][2]))
solve()


