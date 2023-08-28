def knapsack_solve(wt, val, W, N):
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for w in range(1, W + 1):
            if wt[i] <= w:
                dp[i][w] = max(dp[i - 1][w], val[i] + dp[i - 1][w - wt[i]])
            else:
                dp[i][w] = dp[i - 1][w]
    
    selected = []
    i, w = N, W
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i)
            w -= wt[i]
        i -= 1

    return dp[N][W], selected[::-1]

def main():
    n = int(input("Enter number of items: "))
    weights = [0] + list(map(int, input("Enter weights of items: ").split()))
    values = [0] + list(map(int, input("Enter values of items: ").split()))
    capacity = int(input("Enter knapsack capacity: "))
    
    optimal_value, selected_items = knapsack_solve(weights, values, capacity, n)

    print("Optimal value:", optimal_value)
    print("Selected items:", " ".join(map(str, selected_items)))

if __name__ == "__main__":
    main()
