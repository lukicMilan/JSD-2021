import os
import pdfkit

def html2pdf(html_path, pdf_path, options):
  
  with open(html_path) as f:
    pdfkit.from_file(f, pdf_path, options=options)

  # If you are a Windows user, you need to uncomment lines 10-12 and comment/delete lines 6 i 7 in order to execute generator.
  # with open(html_path, encoding='utf8') as f:
  #   config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
  #   pdfkit.from_file(f, pdf_path, options=options, configuration=config)
