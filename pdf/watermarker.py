import PyPDF2

file = open('meetingminutes.pdf', 'rb') # change the filename
pdfReader = PyPDF2.PdfFileReader(file)

# only add the watermark to the first page
firstPage = pdfReader.getPage(0)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb')) # change the watermark pdf name if needed
firstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(firstPage)

# merge the rest pages to the first watermarked page
for i in range(1,pdfReader.numPages):
	pageObj = pdfReader.getPage(i)
	pdfWriter.addPage(pageObj)

resultPdfFile = open('watermarkerCover.pdf','wb')
pdfWriter.write(resultPdfFile)
file.close()
resultPdfFile.close()
