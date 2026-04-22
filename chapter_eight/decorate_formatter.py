def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        new_tuple = tuple(map(convert_md_to_txt, args))
        new_dict = {}
        for key, value in kwargs.items():
            new_dict[key] = convert_md_to_txt(value)

        return func(*new_tuple, **new_dict)
            
    return wrapper


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)

