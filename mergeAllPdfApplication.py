from PyPDF2 import PdfWriter
import os

pdfFiles = [file for file in os.listdir("pdfFile") if file.endswith(".pdf")]
mergedPdf = PdfWriter()

for file in pdfFiles:
    mergedPdf.append(file)

mergedPdf.write("merged-pdf.pdf")
mergedPdf.close()

