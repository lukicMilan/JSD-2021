from textx import metamodel_from_file
from classes.document import Document

def main():
    metamodel = metamodel_from_file("metamodel/grammar.tx")
    model = metamodel.model_from_file("../testfile.tff")

    document = Document()
    document.interpreter(model)
    print(document)

if __name__ == "__main__":
    main()
