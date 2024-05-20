def min_cost(users, processes, processors, current_alloc=[], min_alloc=[], min_cost=float('inf')):
    # Base case: no more users or processes to assign
    if not users or not processes:
        current_cost = calc_cost(current_alloc)
        # If the current allocation gives a lower cost, update min_alloc and min_cost
        if current_cost < min_cost:
            return current_alloc, current_cost
        else:
            return min_alloc, min_cost

    # Recursive case: for each user-process pair, assign to each processor
    for i in range(len(users)):
        for j in range(len(processes)):
            for k in range(len(processors)):
                user = users[i]
                process = processes[j]
                processor = processors[k]
                remaining_users = users[:i] + users[i+1:]
                remaining_processes = processes[:j] + processes[j+1:]
                remaining_processors = processors[:k] + processors[k+1:]
                # Assign the user-process pair to the processor
                new_alloc = current_alloc + [(user, process, processor)]
                min_alloc, min_cost = min_cost(remaining_users, remaining_processes, remaining_processors, new_alloc, min_alloc, min_cost)

    return min_alloc, min_cost
