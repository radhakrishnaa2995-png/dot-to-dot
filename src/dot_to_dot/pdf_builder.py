from reportlab.lib.pagesizes import A4, letter
from reportlab.pdfgen import canvas
from PIL import Image
import os

def create_pdf(pages: List[str], output_path: str, page_size='A4'):
    size_map = {
        'A4': A4,
        'letter': letter,
    }
    size = size_map.get(page_size, A4)
    c = canvas.Canvas(output_path, pagesize=size)

    for page_file in pages:
        c.drawInlineImage(page_file, 0, 0, width=size[0], height=size[1])
        c.showPage()

    c.save()
