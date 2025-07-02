import os
from google.genai import types
def get_files_info(working_directory, directory=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_directory = abs_working_dir
        if directory:
            target_directory = os.path.abspath(os.path.join(working_directory, directory))
        if not target_directory.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_directory):
            return f'Error: "{directory}" is not a directory'
        
        # print(f"Listing files in: {target_directory}")
        files = os.listdir(target_directory)
        files_info = []
        for file in files:
            file_path = os.path.join(target_directory,file)
            size= 0
            size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            files_info.append(f"- {file}: file_size={size} bytes, is_dir={is_dir}")
        final = "\n".join(files_info)
        return final
    except Exception as e:
        return f"Error listing files: {str(e)}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
