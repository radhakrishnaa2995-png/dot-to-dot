from src.dot_to_dot import pdf_builder

def test_create_pdf():
    # create dummy images
    from PIL import Image
    img1 = Image.new('RGB', (595, 842), 'white')  # A4 size
    img1_path = 'test_page1.png'
    img1.save(img1_path)
    output_pdf = 'test_output.pdf'
    pdf_builder.create_pdf([img1_path], output_pdf)
    import os
    assert os.path.exists(output_pdf)
    # cleanup
    import os
    os.remove(img1_path)
    os.remove(output_pdf)
