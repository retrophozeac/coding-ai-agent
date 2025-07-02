import os
from google.genai import types
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

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the content of a file up to 10000 characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path to get content from, relative to the working directory.",
            ),
        },
    ),
)