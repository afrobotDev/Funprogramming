def doc_format_checker_and_converter(conversion_function, valid_formats):
    def convert_func(filename, content):
        split_list = filename.split('.')
        if split_list[1] in valid_formats:
            return conversion_function(content)

        else:
            raise ValueError('invalid file format')

    return convert_func


def capitalize_content(content):
    return content.upper()

def reverse_content(content):
    return content[::-1]

