def knapsack(Weights, Values, Capacity, n):
    if n == 0 or Capacity == 0:
        return 0
    if Weights[n-1] > Capacity:
        return knapsack(Weights, Values, Capacity, n-1)
    include = Values[n-1] + knapsack(Weights, Values, Capacity - Weights[n-1], n-1)
    exclude = knapsack(Weights,  Values, Capacity, n-1)
    return max(include, exclude)
    
Values = [1, 2, 5, 6]
Weights = [2, 3, 4, 53]
Capacity = 8
print(knapsack(Weights, Values, Capacity, len(Weights)))
