from pypdf import PdfReader


def read_pdf(file_path: str) -> str:
    """
    Reads a PDF file and extracts all text content from it.
    
    Use this tool when you need to:
    - Read information from PDF attachments
    - Extract text from PDF documents
    - Answer questions about content in PDF files
    - Analyze data in library catalogs, accommodation listings, or any PDF document
    
    Args:
        file_path: The full path to the PDF file to read
    
    Returns:
        A string containing all the text extracted from the PDF,
        or an error message if the file cannot be read
    
    Examples:
        read_pdf("benchmark/attachments/7.pdf") -> "Library Catalog\n..."
        read_pdf("data/report.pdf") -> "Annual Report 2024\n..."
    """
    try:
        # Open and read the PDF file
        reader = PdfReader(file_path)
        
        # Extract text from all pages
        text_content = []
        for page_num, page in enumerate(reader.pages):
            text = page.extract_text()
            text_content.append(text)
        
        # Combine all pages with page separators
        full_text = "\n\n--- Page Break ---\n\n".join(text_content)
        
        if not full_text.strip():
            return "Error: The PDF appears to be empty or contains no extractable text."
        
        return full_text
        
    except FileNotFoundError:
        return f"Error: File not found at path '{file_path}'. Please check the file path."
    except Exception as e:
        return f"Error: Failed to read PDF - {str(e)}"
