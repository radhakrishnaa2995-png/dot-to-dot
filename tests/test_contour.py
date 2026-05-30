import pytest
import numpy as np
from src.dot_to_dot import contour

def test_extract_contour_with_circle():
    # create a circle edge image
    size = 100
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.circle(img, (size//2, size//2), 30, 255, 2)
    points = contour.extract_contour(img)
    assert len(points) > 0
