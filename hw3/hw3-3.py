def min_energy(parts, current_seq=[], min_seq=[], min_energy=float('inf')):
    # Base case: no more parts to assemble
    if not parts:
        current_energy = calc_energy(current_seq)
        # If the current sequence gives a lower energy cost, update min_seq and min_energy
        if current_energy < min_energy:
            return current_seq, current_energy
        else:
            return min_seq, min_energy

    # Recursive case: for each part, choose to assemble it next
    for i in range(len(parts)):
        part = parts[i]
        remaining_parts = parts[:i] + parts[i+1:]
        # Choose to assemble the part next
        new_seq = current_seq + [part]
        min_seq, min_energy = min_energy(remaining_parts, new_seq, min_seq, min_energy)

    return min_seq, min_energy
