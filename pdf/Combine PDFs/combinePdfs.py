#! python3
# combinePdfs.py - Combines all the PDFs in the current working directory into 
# a single PDF.

import PyPDF2, os

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort()

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Loop through all the pages and add them.
    for pageNum in range(0, pdfReader.numPages): # If the first page is cover and you want to remove it, just change 0 to 1.
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open('result/result.pdf', 'wb') # To avoid the error, the example result is stored in another folder.
pdfWriter.write(pdfOutput)
pdfOutput.close()
