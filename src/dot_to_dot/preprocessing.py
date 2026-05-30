import cv2
import numpy as np

def load_image(path: str) -> np.ndarray:
    return cv2.imread(path)

def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def resize_if_needed(image: np.ndarray, max_size=(1000, 1000)) -> np.ndarray:
    h, w = image.shape[:2]
    max_w, max_h = max_size
    if w > max_w or h > max_h:
        scale = min(max_w / w, max_h / h)
        new_size = (int(w * scale), int(h * scale))
        return cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)
    return image

def edge_detection(image: np.ndarray) -> np.ndarray:
    edges = cv2.Canny(image, threshold1=50, threshold2=150)
    return edges
