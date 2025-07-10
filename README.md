# AI Code Assistant

A powerful AI-powered coding agent that can help you with various programming tasks using Google's Gemini AI model. This tool provides an interactive command-line interface where you can ask questions and get assistance with file operations, code execution, and project development.

## Features

- **File System Operations**: List directories, read file contents, and write/modify files
- **Code Execution**: Run Python scripts with optional arguments
- **Interactive AI Assistant**: Powered by Google's Gemini 2.0 Flash model
- **Security-Focused**: All operations are constrained to the working directory for safety
- **Verbose Mode**: Optional detailed logging of API usage and function calls

## Available Functions

The AI assistant can perform the following operations:

1. **List Files and Directories** - Browse your project structure
2. **Read File Contents** - Examine existing code and files
3. **Write/Overwrite Files** - Create new files or modify existing ones
4. **Execute Python Files** - Run Python scripts with optional command-line arguments

## Prerequisites

- Python 3.11 or higher
- Google Gemini API key

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd ai-agent
```

2. Install dependencies using uv (recommended) or pip:
```bash
# Using uv
uv sync

# Or using pip
pip install -r requirements.txt
```

3. Set up your environment variables:
```bash
cp .env.example .env
```

4. Add your Google Gemini API key to the `.env` file:
```
GEMENI_API_KEY=your_api_key_here
```

## Usage

### Basic Usage

```bash
python main.py "your prompt here"
```

### Examples

```bash
# Ask for help building a calculator
python main.py "How do I build a calculator app?"

# Request file analysis
python main.py "Analyze the structure of my project and suggest improvements"

# Ask for code generation
python main.py "Create a simple web scraper using Python"

# Request debugging help
python main.py "Help me debug the error in my main.py file"
```

### Verbose Mode

For detailed logging and debugging information:

```bash
python main.py "your prompt here" --verbose
```

This will show:
- Token usage (prompt and response tokens)
- Function calls being made
- Detailed function responses

## Project Structure

```
ai-agent/
├── main.py                 # Main application entry point
├── functions/              # Function implementations
│   ├── call_function.py    # Function call dispatcher
│   ├── get_files_info.py   # Directory listing functionality
│   ├── get_file_content.py # File reading functionality
│   ├── run_python.py       # Python script execution
│   └── write_file.py       # File writing functionality
├── calculator/             # Example project
├── tests.py               # Test suite
├── pyproject.toml         # Project configuration
├── .env                   # Environment variables
└── README.md              # This file
```

## How It Works

1. **Input Processing**: The tool takes your natural language prompt as a command-line argument
2. **AI Planning**: Gemini AI analyzes your request and creates a function call plan
3. **Function Execution**: The AI calls appropriate functions to perform file operations or code execution
4. **Iterative Process**: The AI can make multiple function calls in sequence to complete complex tasks
5. **Response Generation**: You receive both the function results and AI-generated explanations

## Security Features

- All file operations are constrained to the working directory
- Path traversal attacks are prevented
- Functions validate file paths before execution
- No system-level commands are executed outside of Python script running

## Configuration

### Environment Variables

- `GEMENI_API_KEY`: Your Google Gemini API key (required)

### Model Configuration

The tool uses `gemini-2.0-flash-001` by default. The model is configured with:
- Function calling capabilities
- System instruction for coding assistance
- Maximum of 20 iteration loops to prevent infinite loops

## Examples of What You Can Ask

- "Create a simple calculator application"
- "Analyze my code and suggest improvements"
- "Help me debug this error message"
- "Generate unit tests for my functions"
- "Refactor this code to be more efficient"
- "Create a README file for my project"
- "Set up a basic web server"
- "Help me organize my project structure"

## Limitations

- Limited to Python script execution (no arbitrary system commands)
- All operations must be within the working directory
- Maximum of 20 AI iterations per session
- Requires internet connection for Gemini API calls

- Basic file operations
- Python script execution
- Gemini AI integration
- Security constraints implementation
