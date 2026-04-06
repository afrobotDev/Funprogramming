valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

def pair_document_with_format(doc_names, doc_formats):
    return list(
        filter(
            lambda doc_pair: doc_pair[1] in valid_formats,
            zip(doc_names, doc_formats)
        )
    )
