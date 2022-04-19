import jinja2

def document2html(document, template_path, html_path):

  template_loader = jinja2.FileSystemLoader(searchpath="./")
  template_env = jinja2.Environment(loader=template_loader)
  template_file = template_path
  template_path = template_env.get_template(template_file)

  output_text = template_path.render(document)

  html_path = html_path
  html_file = open(html_path, 'w', 1, 'utf8')
  html_file.write(output_text)
  html_file.close()
