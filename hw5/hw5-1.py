import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force(P):
    min_dist = float('inf')
    for i in range(len(P)):
        for j in range(i+1, len(P)):
            if distance(P[i], P[j]) < min_dist:
                min_dist = distance(P[i], P[j])
                pair = (P[i], P[j])
    return pair[0], pair[1], min_dist

def closest_split_pair(P, delta):
    P.sort(key=lambda x: x[1])  # sort by y coordinate
    min_dist = delta
    pair = None
    for i in range(len(P)):
        for j in range(i+1, len(P)):
            if P[j][1] - P[i][1] >= min_dist:
                break
            elif distance(P[i], P[j]) < min_dist:
                min_dist = distance(P[i], P[j])
                pair = (P[i], P[j])
    return pair[0], pair[1], min_dist

def closest_pair(P):
    n = len(P)
    if n <= 3:
        return brute_force(P)
    mid = n // 2
    Q = P[:mid]
    R = P[mid:]
    (p1, q1, d1) = closest_pair(Q)
    (p2, q2, d2) = closest_pair(R)
    (p3, q3, d3) = closest_split_pair(P, d1 if d1 < d2 else d2)
    if d1 <= d2 and d1 <= d3:
        return p1, q1, d1
    elif d2 <= d1 and d2 <= d3:
        return p2, q2, d2
    else:
        return p3, q3, d3
