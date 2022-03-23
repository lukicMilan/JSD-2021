class Document:

  def __init__(self):
    self.type = ""
    self.title = ""
    self.paragraph_list = []

  def __str__(self):
    paragraph_string = f"Paragraph: \n"

    i = 0
    for p in self.paragraph_list:
      paragraph_string += f"[{i}] {p}\n\n"
      i+=1

    return f"Type: {self.type}\nTitle: {self.title}\n" + paragraph_string

  def interpreter(self, model):
    for block in model.blocks:
      if hasattr(block, 'type'):
        self.type = block.type
      if hasattr(block, 'title'):
        self.title = block.title
      
      if hasattr(block, 'paragraph'):
        self.paragraph_list.append(block.paragraph)

  def get_dict(self):
    default_template = {
        "title": self.title,
        "paragraph_list": self.paragraph_list
      }

    # TODO: Make more templates based on PDF type needed
    switcher = {
      "default": default_template
    }
    
    return switcher.get(self.type, default_template)
