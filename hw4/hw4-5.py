def Max_Min_Resources(tasks):
    """
    This function finds the tasks demanding the maximum and minimum resources.

    Parameters:
    tasks (list): A list of tasks, where each task is a tuple containing the task name and the resources it demands

    Returns:
    tuple: The tasks demanding the maximum and minimum resources
    """

    if len(tasks) == 1:
        return tasks[0], tasks[0]

    mid = len(tasks) // 2
    left_max, left_min = Max_Min_Resources(tasks[:mid])
    right_max, right_min = Max_Min_Resources(tasks[mid:])

    max_task = left_max if left_max[1] > right_max[1] else right_max
    min_task = left_min if left_min[1] < right_min[1] else right_min

    return max_task, min_task
