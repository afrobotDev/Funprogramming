def file_type_getter(file_extension_tuples):
    map_file = {}
    for type_ext in file_extension_tuples:
        for file_ext in type_ext[1]:
            map_file[file_ext] = type_ext[0]
    
    return lambda file_ext: map_file.get(file_ext, 'Unknown')



