import os
import subprocess
def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_directory = abs_working_dir
    if file_path:
        target_directory = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_directory.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_directory):
        return f'Error: File "{file_path}" not found.'
    if not target_directory.endswith('.py'):
        return f'Error: File "{file_path}" not found.'
    try:
        result = subprocess.run(
            ["python3", target_directory],
            timeout=30,
            capture_output=True,
            text=True,
            check=True  
            )
        if result.returncode != 0:
            return f"STDOUT: {result.stdout}. STDERR: {result.stderr}. Process exited with code {result.returncode}."
        if not result:
            return "No output produced"
        return f"STDOUT: {result.stdout}. STDERR: {result.stderr}."
    except Exception as e:
        return f"Error: executing Python file: {e}"