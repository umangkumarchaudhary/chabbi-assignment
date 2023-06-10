def get_file_types(extension_type_str, file_list):
    
    extension_type_pairs = extension_type_str.split(';')

    
    extension_type_dict = {}
    for pair in extension_type_pairs:
        extension, file_type = map(str.strip, pair.split(','))
        extension_type_dict[extension] = file_type

    result_dict = {}
    for file_name in file_list:
        if '.' in file_name:
            extension = file_name.split('.')[-1].lower()
            if extension in extension_type_dict:
                result_dict[file_name] = extension_type_dict[extension]
            else:
                result_dict[file_name] = 'unknown'
        else:
            result_dict[file_name] = 'unknown'

    return result_dict



