import os
def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_directory = abs_working_dir
    if file_path:
        target_directory = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_directory.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_directory):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    MAX_CHARS = 10000
    try:
        with open(target_directory, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) == MAX_CHARS:
            file_content_string = f'{file_content_string}[...File "{target_directory}" truncated at 10000 characters]'
        return file_content_string
    except Exception as e:
        return f'Error: {str(e)}'
