# tuples are immutable
# add_prefix takes a tuple called documents
# and  prefixes to each items
def add_prefix(document, documents):
  prefix = f"{len(documents)}. "
  new_doc = prefix + document
  return documents + (new_doc,)
