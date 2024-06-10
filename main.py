import PyPDF2
import os

merger = PyPDF2.PdfMerger()
pdf_files = [file for file in os.listdir(os.curdir) if file.endswith('.pdf')]

print("Merging files: ")
for file in pdf_files:
    try:
        print(f"Appending {file}")
        merger.append(file)
    except ValueError as e:
        print(f"Error appending {file}: {e}")
    except Exception as e:
        print(f"Unexpected error with {file}: {e}")

merger.write('merged.pdf')
merger.close()
print("Merge complete.")