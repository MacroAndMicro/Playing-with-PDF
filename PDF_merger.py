
#import os
from PyPDF2 import PdfFileMerger

'''source_dir = os.getcwd()
merger = PdfFileMerger()

for file in os.listdir(source_dir):
    if file.endswith('.pdf') :
        merger.append(file)

merger.write("pawriiii_pdf.pdf")


merger.close()
'''


pdfs = ['nit_jsr_bona.pdf.pdf', 'NOC.pdf.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("gulabo.pdf")
merger.close()
