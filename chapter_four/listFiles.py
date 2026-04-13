def list_files(parent_directory, current_filepath=""):
    file_paths_lst = [] 
    for key in parent_directory:
        new_files_path = current_filepath + f'/{key}'
        if parent_directory[key] is None:
            file_paths_lst.append(new_files_path)

        else:
            file_paths_lst.extend(list_files(parent_directory[key], new_files_path))

    return file_paths_lst
