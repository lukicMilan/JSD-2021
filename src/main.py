from secrets import choice
from textx import metamodel_from_file
from classes.createReport import createReport

def main():

  choice = 0

  print("Unesite redni broj obrasca koji želite da izradite:\n1. Studentsko uverenje\n2. Bankovni izvod\n3. Ugovor o zakupu stana")
  choice = input("Vaš izbor: ")
  print("Generisanje: ", choice)

  metamodel = metamodel_from_file("metamodel/grammar.tx")

  if choice == '1':
    model = metamodel.model_from_file("../testfile.tff")
  elif choice == '2':
    model = metamodel.model_from_file("../bankreportTestfile.tff")
  elif choice == '3':
    model = metamodel.model_from_file("../zakupStanaTestfile.tff")
  else:
    print("Uneli ste nepostojeći broj. Molimo Vas ponovite sa validnim podacima.")
  
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

  createReport(model, options, choice)

if __name__ == "__main__":
  main()
