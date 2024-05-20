def max_discount(stores):
    n = len(stores)
    table = [0 for _ in range(n)]
    
    # Initialize the first entry
    table[0] = calc_discount([stores[0]])
    
    for i in range(1, n):
        max_discount = 0
        for j in range(i+1):
            # Calculate discount for each combination
            discount = calc_discount(stores[j:i+1])
            if discount > max_discount:
                max_discount = discount
        table[i] = max_discount

    # The maximum achievable discount is the maximum value in the table
    return max(table)
