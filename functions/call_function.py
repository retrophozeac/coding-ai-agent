from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.get_files_info import get_files_info
from functions.run_python import run_python_file
from google.genai import types
def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    working_directory = "./calculator"
    function_name = function_call_part.name
    function_args = function_call_part.args
    dict_func = {
        "get_file_content": get_file_content,
        "write_file": write_file,
        "get_files_info": get_files_info,
        "run_python_file": run_python_file
    }
    if not dict_func[function_name]:
        return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"error": f"Unknown function: {function_name}"},
                    )
                ],
            )
    print("hi")
    result = dict_func[function_name](working_directory, **function_args)
    return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": result},
                )
            ],
        )  