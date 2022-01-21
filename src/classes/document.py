class Document:

  def __init__(self):
    self.title = ""
    self.paragraph_list = []

  def __str__(self):
    returnStr = ""

    returnStr += f"We have title: {self.title}\n"
    returnStr += f"And paragraph: \n"

    i = 0
    for p in self.paragraph_list:
      returnStr += f"[{i}] {p}\n\n"
      i+=1

    return returnStr

  def interpreter(self, model):
    for block in model.blocks:
      if hasattr(block, 'title'):
        self.title = block.title
      
      if hasattr(block, 'paragraph'):
        self.paragraph_list.append(block.paragraph)

  def get_dict(self):
    
    return {
      "title": self.title,
      "paragraph_list": self.paragraph_list
    }
