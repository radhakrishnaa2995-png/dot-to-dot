from src.dot_to_dot import renderer

def test_render_dots():
    dots = [(10,10), (50,50), (90,10)]
    img = renderer.render_dots(dots)
    assert img.size[0] > 0 and img.size[1] > 0
    img.save("test_output.png")
