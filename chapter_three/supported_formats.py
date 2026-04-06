def add_format(default_formats, new_format):
    default_copy = default_formats.copy()
    default_copy[new_format] = True
    return default_copy 


def remove_format(default_formats, old_format):
    default_copy = default_formats.copy()
    default_copy[old_format] = False
    return default_copy

