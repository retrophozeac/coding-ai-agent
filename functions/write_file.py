import os
from google.genai import types
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
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)