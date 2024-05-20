def Find_Flawed_Fuse(fuses):
    """
    This function finds the broken fuse in a list of fuses.

    Parameters:
    fuses (list): A list of fuses, where each fuse is either 'working' or 'broken'

    Returns:
    int: The index of the broken fuse, or -1 if no broken fuse is found
    """

    for i in range(len(fuses)):
        if fuses[i] == 'broken':
            return i
    return -1  # return -1 if no broken fuse is found
