def word_count_memo(document, memos):
    mem_cpy = memos.copy()
    if document in mem_cpy:
        return mem_cpy[document], mem_cpy
    
    else:
        mem_cpy[document] = word_count(document)
        return mem_cpy[document], mem_cpy  


def word_count(document):
    count = len(document.split())
    return count
