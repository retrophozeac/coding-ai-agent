
import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python import schema_run_python
from functions.call_function import call_function

def main():
    load_dotenv()

    system_prompt = """
                        You are a helpful AI coding agent.
                        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:
                        - List files and directories
                        - Read file contents
                        - Execute Python files with optional arguments
                        - Write or overwrite files
                        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
                        """
    
    args = sys.argv[1:]
    verbose = False
    if args and args[-1] == "--verbose":
        verbose = True
        args = args[:-1]

    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python
    ]
)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    user_prompt = " ".join(args)
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    api_key = os.getenv("GEMENI_API_KEY")
    client = genai.Client(api_key=api_key)
    for x in range(20):
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config = types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt)
        )
        if verbose:
            print("User prompt:", user_prompt)
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)
        print("Response:")
        print(response.text)
        print(response.candidates[0].content)
        for candidate in response.candidates:
            messages.append(candidate.content)
        if response.function_calls != None:
            function_call_part = response.function_calls[0]
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
            result = call_function(function_call_part, verbose=verbose)
            if not result.parts[0].function_response.response:
                raise Exception(f"Error calling function:")
            if verbose:
                print(f"-> {result.parts[0].function_response.response}")
            messages.append(result)
        else:
            print(response.text)
            break
    

    

if __name__ == "__main__":
    main()
