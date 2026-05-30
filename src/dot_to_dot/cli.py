import argparse
from .batch import process_images, build_pdf

def main():
    parser = argparse.ArgumentParser(description='Dot-to-dot book generator')
    subparsers = parser.add_subparsers(dest='command')

    # process command
    process_parser = subparsers.add_parser('process', help='Process images to generate pages')
    process_parser.add_argument('--input', type=str, default='input_images', help='Input images folder')
    process_parser.add_argument('--output', type=str, default='output', help='Output folder')
    process_parser.add_argument('--page-size', type=str, default='A4', help='Page size (e.g., A4, letter)')
    process_parser.add_argument('--dots', type=int, default=100, help='Number of dots per shape')

    # build-pdf command
    build_parser = subparsers.add_parser('build-pdf', help='Build PDF from pages')
    build_parser.add_argument('--pages', type=str, default='output/pages', help='Folder with PNG pages')
    build_parser.add_argument('--pdf', type=str, default='output/final_book.pdf', help='Output PDF filename')

    args = parser.parse_args()

    if args.command == 'process':
        process_images(input_dir=args.input, output_dir=args.output, page_size=args.page_size, dot_count=args.dots)
    elif args.command == 'build-pdf':
        build_pdf(pages_folder=args.pages, output_pdf=args.pdf)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
