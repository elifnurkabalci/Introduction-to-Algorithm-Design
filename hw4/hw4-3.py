def Find_Max_Area(f):
    """
    This function finds the interval that produces the maximal total area under the function f(x).

    Parameters:
    f (list): A list of values representing the function f(x) over the interval [0,n]

    Returns:
    tuple: The interval that produces the maximal total area
    """

    max_area = 0
    start = 0
    end = 0

    for i in range(len(f) - 1):
        area = 0
        for j in range(i+1, len(f)):
            area += f[j]
            if area > max_area:
                max_area = area
                start = i
                end = j
    return (start, end)
