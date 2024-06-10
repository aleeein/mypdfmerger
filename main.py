import PyPDF2
import os

def list_pdf_files(folder_path):
    return [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

def display_pdf_files(pdf_files):
    for index, file in enumerate(pdf_files, start=1):
        print(f"{index}. {file}")

def get_files_to_merge(pdf_files):
    selected_files = input("Enter the numbers of the PDF files you want to merge, separated by commas: ")
    selected_indices = [int(x.strip()) - 1 for x in selected_files.split(',')]
    return [pdf_files[i] for i in selected_indices]

def get_merged_filename():
    return input("Enter the name of the merged file (without extension): ").strip() + '.pdf'

def main():
    folder_path = input("Enter the folder path containing the PDF files: ").strip()
    
    if not os.path.isdir(folder_path):
        print("Invalid folder path. Please try again.")
        return
    
    pdf_files = list_pdf_files(folder_path)
    if not pdf_files:
        print("No PDF files found in the folder.")
        return
    
    print("Available PDF files:")
    display_pdf_files(pdf_files)
    
    try:
        files_to_merge = get_files_to_merge(pdf_files)
    except (ValueError, IndexError):
        print("Invalid selection. Please try again.")
        return
    
    merged_filename = get_merged_filename()
    merger = PyPDF2.PdfMerger()
    
    print("Merging files: ")
    for file in files_to_merge:
        try:
            file_path = os.path.join(folder_path, file)
            print(f"Appending {file}")
            merger.append(file_path)
        except ValueError as e:
            print(f"Error appending {file}: {e}")
        except Exception as e:
            print(f"Unexpected error with {file}: {e}")
    
    output_path = os.path.join(folder_path, merged_filename)
    merger.write(output_path)
    merger.close()
    print(f"Merge complete. Merged file saved as {output_path}")

if __name__ == "__main__":
    main()