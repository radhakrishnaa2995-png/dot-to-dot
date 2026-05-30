import cv2
import numpy as np
from typing import List, Tuple

def extract_contour(edge_image: np.ndarray) -> List[Tuple[float, float]]:
    contours, _ = cv2.findContours(edge_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return []

    main_contour = max(contours, key=cv2.contourArea)
    epsilon = 0.01 * cv2.arcLength(main_contour, True)
    approx = cv2.approxPolyDP(main_contour, epsilon, True)
    points = [tuple(pt[0]) for pt in approx]
    return points
