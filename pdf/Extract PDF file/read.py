#! Python3
import PyPDF2
import os

# change the filenames/path
input_file = 'meetingminutes.pdf' # Here is an example
output_file = 'text.txt'

pdfFileObj = open(input_file, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# display number of pages
print(pdfReader.numPages)

# remove the previous output file, or the previous text will not be deleted
if (os.path.exists(output_file)):
        os.remove(output_file)

# extract text from the first page and display
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    text = '------------------ Page {} ------------------'.format(i) + '\n' # mark the page number, you can comment it if you don't need this
    text += pageObj.extractText()
    print(text)

    # write the text to the txt file
    f = open(output_file,'a')
    f.write(text)

f.close()
