def remove_invalid_lines(document):
    
    lines = document.split('\n')
    filtered_lines = filter(lambda line: not line.startswith('-'), lines)
    rejoined_lines = '\n'.join(filtered_lines)

    return rejoined_lines
