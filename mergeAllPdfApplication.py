import PyPDF2
import os

pdfFiles = os.listdir("pdf")
merger = PyPDF2.PdfMerger()

for file in pdfFiles:
    if file.endswith(".pdf"):
        merger.append(file)

merger.write("merged-pdf.pdf")

