from textx import metamodel_from_file
from classes.document import Document
from generator.document2html import document2html
from generator.html2pdf import html2pdf

def main():
  metamodel = metamodel_from_file("metamodel/grammar.tx")
  model = metamodel.model_from_file("../testfile.tff")
    
  document = Document()
  document.interpreter(model)
    
  # TODO: Fill options from document
  options = {
    'page-size': 'Letter',
    'margin-top': '0.35in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None,
    'enable-local-file-access': None
  }

  generated_html = "generated.html"
  document2html(document.get_dict(), 'template.html', generated_html)
  html2pdf(generated_html, "generated.pdf", options)

if __name__ == "__main__":
  main()
