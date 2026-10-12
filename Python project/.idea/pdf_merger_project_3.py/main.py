import PyPDF2

pdfiles=["pdf.2.pdf","pdf.3.pdf","sample.pdf"]
merger=PyPDF2.PdfMerger()
for filename in pdfiles:
    pdFile=open(filename,'rb')
    pdfReader=PyPDF2.PdfReader(pdFile)
    merger.append(pdfReader)


pdFile.close()
merger.write('merged.pdf')























