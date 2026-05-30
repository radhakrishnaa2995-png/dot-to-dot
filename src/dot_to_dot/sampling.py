import numpy as np
from typing import List, Tuple

def sample_points(contour: List[Tuple[float, float]], num_points: int) -> List[Tuple[float, float]]:
    if len(contour) == 0:
        return []

    pts = np.array(contour, dtype=np.float32)
    distances = np.sqrt(np.sum(np.diff(pts, axis=0, prepend=pts[-1:])**2, axis=1))
    cumulative = np.cumsum(distances)
    total_length = cumulative[-1]
    if total_length == 0:
        # All points are identical
        return [tuple(pts[0]) for _ in range(num_points)]
    spacing = total_length / num_points

    sampled_points = []
    for i in range(num_points):
        d = i * spacing
        index = np.searchsorted(cumulative, d)
        index = min(index, len(pts) - 1)
        sampled_points.append(tuple(pts[index]))
    return sampled_points
