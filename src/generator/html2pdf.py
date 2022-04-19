import os
import pdfkit

def html2pdf(html_path, pdf_path, options):
  
  with open(html_path) as f:
    pdfkit.from_file(f, pdf_path, options=options)
