def count_nested_levels(nested_documents, target_document_id, level=1):
    for doc_id in nested_documents:
        if doc_id == target_document_id:
            return level

        result = count_nested_levels(nested_documents[doc_id], target_document_id, level+1)
        if result != -1:
            return result


    return -1

