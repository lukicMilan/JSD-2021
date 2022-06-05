import platform
import pdfkit

def html2pdf(html_path, pdf_path, options):
  if platform.system() == 'Windows':
      with open(html_path, encoding='utf8') as f:
        config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
        pdfkit.from_file(f, pdf_path, options=options, configuration=config)
  else:
    with open(html_path) as f:
      pdfkit.from_file(f, pdf_path, options=options)
