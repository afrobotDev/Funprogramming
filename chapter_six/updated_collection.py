def new_collection(initial_docs):
    initial_docs_cpy = initial_docs.copy()
    def add_doc(doc):
        initial_docs_cpy.append(doc)
        
        return initial_docs_cpy

    return add_doc
