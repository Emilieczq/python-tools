# Some functions about PyPDF2

## Installation
Run `pip3 install PyPDF2` to install PyPDF2 in your python3 library.

## Examples

### Combine PDFs
1. Run `pip3 install os` to install os in your python3 library.
2. Put all the PDFs you want to combine in the folder of combinePdfs.py. Make sure they are in the correct alpha order, or you can just number them.
3. Change the output filename in line 27, the default is 'result/result.txt'.
4. Run `python3 combinePdfs.py`.
5. The result will be stored in 'result/result.txt'.

### Extract PDF file
1. Change the input filename in line 6, the default is 'meetingminutes.pdf'.
2. Change the output filename in line 7, the default is 'text.txt'.
3. Run `python3 read.py`.
4. The result will be stored in 'text.txt'.

### Water Marker (the first page)
1. Change the input filename in line 3, the default is 'meetingminutes.pdf'.
2. Change the watermark filename in line 8, the default is 'watermark.pdf'
3. Change the output filename in line 18, the default is 'watermarkerCover.pdf'
4. Run `python3 watermarker.py`.
5. The result will be stored in 'watermarkerCover.pdf'.

