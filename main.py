# pip install pdfrw #
from pdfrw import PdfReader, PdfWriter, PageMerge

def watermaker(path, watermark, output):
    base_pdf = PdfReader(path)
    watermark_pdf = PdfReader(watermark)
    mark = watermark_pdf.pages[0]

    for page in range(len(base_pdf.pages)):
        merger = PageMerge(base_pdf.pages[page])
        merger.add(mark).render()

    writer = PdfWriter()
    writer.write(output, base_pdf)

if __name__ == '__main__':
    watermaker('reportlab_sample.pdf', 'watermak.pdf',
               'watermarked_test.pdf')
