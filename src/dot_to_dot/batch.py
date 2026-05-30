import os
import json
from typing import List
from . import preprocessing, contour, sampling, renderer

def process_images(input_dir: str, output_dir: str, page_size: str='A4', dot_count: int=100):
    os.makedirs(output_dir, exist_ok=True)
    pages_dir = os.path.join(output_dir, 'pages')
    os.makedirs(pages_dir, exist_ok=True)
    manifest = []

    files = sorted([f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

    for filename in files:
        input_path = os.path.join(input_dir, filename)
        print(f"Processing {filename}...")
        try:
            # Preprocess
            image = preprocessing.load_image(input_path)
            gray = preprocessing.convert_to_grayscale(image)
            resized = preprocessing.resize_if_needed(gray)
            preprocessed = preprocessing.edge_detection(resized)

            # Contour extraction
            contour_points = contour.extract_contour(preprocessed)

            if not contour_points:
                print(f"Warning: No valid contour found for {filename}")
                continue

            # Sampling
            dots = sampling.sample_points(contour_points, dot_count)

            # Rendering
            page_image = renderer.render_dots(dots, image_size=page_size)
            output_filename = f"{os.path.splitext(filename)[0]}_dots.png"
            output_path = os.path.join(pages_dir, output_filename)
            page_image.save(output_path)

            # Save manifest
            manifest.append({
                'filename': filename,
                'page_image': output_filename,
                'dot_count': len(dots),
                'status': 'success'
            })

        except Exception as e:
            print(f"Error processing {filename}: {e}")
            manifest.append({
                'filename': filename,
                'page_image': None,
                'dot_count': 0,
                'status': f'failed: {e}'
            })

    # Save manifest
    manifest_path = os.path.join(output_dir, 'manifest.json')
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)

def build_pdf(pages_folder: str, output_pdf: str):
    from reportlab.lib.pagesizes import A4, letter
    from reportlab.pdfgen import canvas
    from PIL import Image
    import os

    # Determine page size
    size_map = {
        'A4': A4,
        'letter': letter,
    }
    size = size_map.get('A4', A4)

    c = canvas.Canvas(output_pdf, pagesize=size)

    pages = sorted([f for f in os.listdir(pages_folder) if f.lower().endswith('.png')])

    for page_file in pages:
        img_path = os.path.join(pages_folder, page_file)
        c.drawInlineImage(img_path, 0, 0, width=size[0], height=size[1])
        c.showPage()

    c.save()
    print(f"PDF saved to {output_pdf}")
