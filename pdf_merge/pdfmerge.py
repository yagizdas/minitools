from pypdf import PdfWriter
import os
thisdir = os.getcwd()
filesdir = thisdir + "\pdfs"
print(thisdir)
files = os.listdir(filesdir)
pdfs = []
for file in files:
    name, ext = os.path.splitext(file)
    if ext == '.pdf':
        pdfs.append(file)
print(pdfs)

merger = PdfWriter()

for pdf in pdfs:
    merger.append(f"{filesdir}\{pdf}")

merger.write(filesdir + "\merged\merged-pdf.pdf")
merger.close()