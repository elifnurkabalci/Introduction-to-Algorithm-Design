import math

def distance(A, B, C):
    # Distance of point C from line AB
    return abs((C[1] - A[1]) * (B[0] - A[0]) - (B[1] - A[1]) * (C[0] - A[0]))

def is_left(A, B, C):
    # Check if point C is on left of line AB
    return ((B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])) > 0

def hull_points(S, A, B, convex_hull):
    if not S:
        return
    # Find point P in S that is farthest from line AB
    P = max(S, key=lambda point: distance(A, B, point))
    # Add P to convex hull
    convex_hull.append(P)
    # Discard points inside triangle ABP
    S1 = [point for point in S if is_left(A, P, point)]
    S2 = [point for point in S if is_left(P, B, point)]
    # Find hull points from both subsets
    hull_points(S1, A, P, convex_hull)
    hull_points(S2, P, B, convex_hull)

def quick_hull(P):
    if len(P) <= 3:
        return P
    convex_hull = []
    # Find leftmost and rightmost points
    A = min(P, key=lambda point: point[0])
    B = max(P, key=lambda point: point[0])
    # Add A and B to convex hull
    convex_hull.extend([A, B])
    # Split remaining points into two subsets
    S1 = [point for point in P if point not in [A, B] and is_left(A, B, point)]
    S2 = [point for point in P if point not in [A, B] and not is_left(A, B, point)]
    # Find hull points from both subsets
    hull_points(S1, A, B, convex_hull)
    hull_points(S2, B, A, convex_hull)
    return convex_hull
