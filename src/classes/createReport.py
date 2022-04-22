from classes.document import Document
from generator.document2html import document2html
from generator.html2pdf import html2pdf

def createReport(model, options, choice):
    document = Document()
    document.interpreter(model)

    generated_html = "generated.html"
    dictionary = document.get_dict()

    if dictionary:
        if choice == '1':
            document2html(dictionary, 'template.html', generated_html)
            html2pdf(generated_html, "Studentsko_Uverenje.pdf", options)
        elif choice == '2':
            document2html(dictionary, 'bankReportTemplate.html', generated_html)
            html2pdf(generated_html, "Bankovni_Izvestaj.pdf", options)
        elif choice == '3':
            document2html(dictionary, 'zakupStanaTemplate.html', generated_html)
            html2pdf(generated_html, "Zakup_Stana.pdf", options)
    else:
      print('There is no content in dictionary. Please add valid input file.')
