def max_antennas(antennas):
    # Sort antennas by finish point
    antennas.sort(key=lambda x: x['finish'])
    
    # Initialize current_antenna to the first antenna
    current_antenna = antennas[0]
    
    # Initialize count to 1
    count = 1
    
    for antenna in antennas[1:]:
        # If the start point of the antenna is greater than or equal to the finish point of current_antenna
        if antenna['start'] >= current_antenna['finish']:
            # Update current_antenna to this antenna
            current_antenna = antenna
            # Increment count
            count += 1

    # Return the maximum number of antennas that can be activated
    return count
