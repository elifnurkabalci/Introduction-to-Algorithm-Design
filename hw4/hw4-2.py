def Find_Brightest_Pixel(image):
    """
    This function finds the brightest pixel in a 2D grid of pixels.

    Parameters:
    image (list): A 2D grid of pixels, where each pixel holds a numerical value representing its brightness level

    Returns:
    tuple: The coordinates of the brightest pixel, or (-1, -1) if no brightest pixel is found
    """

    for i in range(1, len(image) - 1):
        for j in range(1, len(image[i]) - 1):
            if (image[i][j] > image[i-1][j] and  # Check top neighbor
                image[i][j] > image[i+1][j] and  # Check bottom neighbor
                image[i][j] > image[i][j-1] and  # Check left neighbor
                image[i][j] > image[i][j+1]):    # Check right neighbor
                return (i, j)
    return (-1, -1)  # return (-1, -1) if no brightest pixel is found
