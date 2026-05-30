import pytest
import cv2
import numpy as np
from src.dot_to_dot import preprocessing

def test_convert_to_grayscale():
    img = np.zeros((10, 10, 3), dtype=np.uint8)
    gray = preprocessing.convert_to_grayscale(img)
    assert gray.shape == (10, 10)

def test_resize_if_needed():
    img = np.zeros((2000, 2000), dtype=np.uint8)
    resized = preprocessing.resize_if_needed(img)
    assert resized.shape[0] <= 1000 and resized.shape[1] <= 1000

def test_edge_detection():
    img = np.zeros((10, 10), dtype=np.uint8)
    edges = preprocessing.edge_detection(img)
    assert edges.shape == (10, 10)
