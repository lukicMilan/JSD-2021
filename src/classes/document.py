class Document:

  def __init__(self):
    self.title = ""
    self.paragraph = []

  def __str__(self):
    returnStr = ""

    returnStr += f"We have title: {self.title}\n"
    returnStr += f"And paragraph: \n"

    i = 0
    for p in self.paragraph:
      returnStr += f"[{i}] {p}\n\n"
      i+=1

    return returnStr

  def interpreter(self, model):

    self.title = model.title

    for p in model.paragraph:
      self.paragraph.append(p)

  def get_dict(self):
    
    return {
      "title": self.title,
      "paragraph": self.paragraph
    }
