import os
from PyPDF2 import PdfMerger

# Function: Get the order of PDF files from user input
def get_pdf_order():
    # Ask the user to enter PDF filenames separated by commas
    # Example: p1.pdf, p2.pdf, p3.pdf
    pdf_list = input("Enter PDF file names in the desired order (comma-separated): ").split(",")
    # Remove any extra spaces from each filename
    return [pdf.strip() for pdf in pdf_list]

# Function: Check if all the given PDF files exist
def validate_files(pdf_list):
    for pdf in pdf_list:
        if not os.path.exists(pdf):  # Check file existence
            print(f"Error: {pdf} does not exist.")
            return False
    return True  # All files exist

# Function: Merge multiple PDF files into one
def merge_pdfs(pdf_list, output_file):
    merger = PdfMerger()  # Create a merger object
    for pdf in pdf_list:
        merger.append(pdf)  # Add each PDF in order
    merger.write(output_file)  # Save merged PDF
    merger.close()
    print(f"Merged PDF saved as {output_file}")

# Main function: Controls the workflow
def main():
    print("Welcome to the PDF Merger Tool!")
    pdf_list = get_pdf_order()  # Step 1: get files from user
    if validate_files(pdf_list):  # Step 2: check if files exist
        output_file = input("Enter the output file name (e.g., merged.pdf): ")
        merge_pdfs(pdf_list, output_file)  # Step 3: merge

# Run the program only if executed directly
if __name__ == "__main__":
    main()

# Example Usage:
# merge_pdfs(["p1.pdf", "p2.pdf"], "merged.pdf")
# print("PDFs merged successfully!")
