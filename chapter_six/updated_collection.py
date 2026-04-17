def new_collection(initial_docs):
    copy_initial_docs = initial_docs.copy()
    for item in initial_docs:
        def add_doc(item):
            copy_initial_docs.append(item)
            return copy_initial_docs
    
        return add_doc

