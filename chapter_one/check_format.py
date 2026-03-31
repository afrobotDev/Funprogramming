# Identify file formats
def choose_parser(file_extension):
  return (
          'markdown' if file_extension.lower().lstrip('.') in ('markdown', 'md') 
          else 'plaintext'
  ) 
