from PIL import Image, ImageDraw, ImageFont
from typing import List, Tuple

def render_dots(dots: List[Tuple[float, float]], image_size='A4', margin=50, dot_radius=4, font_size=12):
    from reportlab.lib.pagesizes import A4, letter
    size_map = {
        'A4': A4,
        'letter': letter,
    }
    page_size = size_map.get(image_size, A4)

    img = Image.new('RGB', (int(page_size[0]), int(page_size[1])), 'white')
    draw = ImageDraw.Draw(img)

    # Draw lines
    if len(dots) > 1:
        draw.line(dots, fill='black', width=2)

    # Draw dots and numbers
    font = ImageFont.load_default()

    for i, (x, y) in enumerate(dots, start=1):
        draw.ellipse((x - dot_radius, y - dot_radius, x + dot_radius, y + dot_radius), fill='black')
        # Draw number
        draw.text((x + 5, y - 5), str(i), fill='black', font=font)

    return img
