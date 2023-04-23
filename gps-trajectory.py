# Trajectory data points reduction
def rdp_with_index(points, indices, epsilon):
    """rdp with returned point indices
    """
    dmax, index = 0.0, 0
    for i in range(1, len(points) - 1):
        d = point_line_distance(points[i], points[0], points[-1])
        if d > dmax:
            dmax, index = d, i
    if dmax >= epsilon:
        first_points, first_indices = rdp_with_index(points[:index+1], indices[:index+1], epsilon)
        second_points, second_indices = rdp_with_index(points[index:], indices[index:], epsilon)
        results = first_points[:-1] + second_points
        results_indices = first_indices[:-1] + second_indices
    else:
        results, results_indices = [points[0], points[-1]], [indices[0], indices[-1]]
    return results, results_indices
