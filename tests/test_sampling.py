from src.dot_to_dot import sampling

def test_sample_points():
    contour = [(0,0), (10,0), (10,10), (0,10)]
    points = sampling.sample_points(contour, 4)
    assert len(points) == 4
