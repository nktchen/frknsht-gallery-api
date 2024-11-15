from pdf2image import convert_from_path

for i in range(1, 10):
    pdf_file = f'img/{i}.pdf'
    pages = convert_from_path(pdf_file, dpi=300)
    for j, page in enumerate(pages):
        page.save(f'output_page_{i}_{j + 1}.png', 'PNG')