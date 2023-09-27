import fitz  # PyMuPDF

# Function to extract pages within specified ranges
def extract_pages(input_pdf, output_pdf, page_ranges):
    pdf_document = fitz.open(input_pdf)
    output_pdf_document = fitz.open()

    for page_range in page_ranges:
        start, end = map(int, page_range.split('-'))

        # Check for valid page numbers
        if 1 <= start <= end <= len(pdf_document):
            for page_num in range(start - 1, end):
                page = pdf_document.load_page(page_num)
                output_pdf_document.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

    output_pdf_document.save(output_pdf)

if __name__ == "__main__":
    input_pdf = 'input.pdf'
    output_pdf = 'output.pdf'

    # Get user input for page ranges (e.g., "1-3,5-7,10-12")
    page_ranges_input = input("Enter page ranges (e.g., '1-3,5-7,10-12'): ")
    page_ranges = [range.strip() for range in page_ranges_input.split(',')]

    extract_pages(input_pdf, output_pdf, page_ranges)
