# Code Explainer

Inspired by some code provided by Arjan Codes here: <https://www.youtube.com/watch?v=mVX3Z46iYTQ>

## Introduction

This is a command-line tool that allows users to ask programming-related questions about code stored in multiple files. The tool will read the contents of the  
files and use them as context when interacting with OpenAI's GPT-3 language model to provide answers to the user's questions.

## Requirements

- Python 3.11 or above
- An OpenAI API key

## Installation

1 Clone the repository.
2 Install the required packages using pip: pip install -r requirements.txt
3 Set your OpenAI API key as an environment variable called OPENAI_API_KEY. For example, on Linux and macOS, you could add the following line to the ~/.bashrc
file: export OPENAI_API_KEY=your_api_key_here

## Usage

```bash
codechat.py [-h] FILE [FILE ...]
```

For example:

```bash
python codechat.py file1.txt file2.txt
```

Replace `file1.txt`, `file2.txt`, etc, with the file names or paths to the files that you want to include in the context. You can include as many files as you like.

Once the tool is running, you can enter a question at the prompt. The tool will generate a response based on the contents of the files, using OpenAI's GPT-3
language model. You can then ask more questions, and the tool will continue to use the context from the files for subsequent questions.

To exit the tool, type exit at the prompt.

## Advanced Usage

The tool provides a few additional options that allow you to customize its behavior.

- `--help`: Shows a help message with usage instructions.

For example, to print the syntax highlighted content of a file, run:

## License

This tool is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

This tool was created by Stuart Maxwell. It is based on the OpenAI GPT-3 API and uses the rich Python library for formatted output.
