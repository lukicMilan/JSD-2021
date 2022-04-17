from classes.studentsko_uverenje import StudentskoUverenje

class Document:

  def __init__(self):
    self.type = ""
    self.title = ""
    self.paragraph_list = []
    self.bank_report = None
    self.uverenje = None

  def __str__(self):
    paragraph_string = f"Paragraph: \n"

    i = 0
    for p in self.paragraph_list:
      paragraph_string += f"[{i}] {p}\n\n"
      i+=1

    return f"Type: {self.type}\nTitle: {self.title}\n" + paragraph_string

  def interpreter(self, model):
    for block in model.blocks:
      if hasattr(block, 'title'):
        self.title = block.title
      if block.__class__.__name__ == 'StudentskoUverenje':
        uverenje = StudentskoUverenje(block.studentsko_uverenje)
        self.type = "studentsko_uverenje"
        self.uverenje = uverenje.getJSON()
      if hasattr(block, 'paragraph'):
        self.paragraph_list.append(block.paragraph)

  def get_dict(self):
    default_template = {
      "title": self.title,
      "paragraph_list": self.paragraph_list
    }

    # TODO: Make more templates based on PDF type needed
    switcher = {
      "default": default_template,
      "studentsko_uverenje": self.uverenje
    }
    
    return switcher.get(self.type, default_template)
