import os
def write_file(working_directory,file_path,content):
    abs_working_dir = os.path.abspath(working_directory)
    target_directory = abs_working_dir
    if file_path:
        target_directory = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_directory.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    # if not os.path.isfile(target_directory):
    #     #create the file if it does not exist
    try:
        with open(target_directory, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {str(e)}'