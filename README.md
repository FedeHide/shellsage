# ShellSage - GPT Terminal Chatbot

This project is a GPT-powered chatbot that runs directly in the terminal. You can interact with the OpenAI language model in real time, ask questions, and get responses directly in your terminal. It is highly useful in server environments without a graphical user interface, providing a straightforward and efficient way to access AI capabilities.

## Technologies Used
<div>
	<a href="https://skillicons.dev">
		<img src="https://skillicons.dev/icons?i=python" />
	</a>
</div>

------------

![shellsage-screenshot.webp](/public/shellsage-screenshot.webp)


## Requirements

Before running the project, make sure you have the following requirements:

- Python 3.8 or higher
- `pip` to install dependencies
- A valid OpenAI API key

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/gpt-terminal-chatbot.git
   cd gpt-terminal-chatbot
   ```

2. **Create a virtual environment (optional but recommended)**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure your OpenAI API key**:
    #### Create a .env file in the root of the project with the following content:

    ```
    OPENAI_API_KEY=your_api_key_here
    ```

    Make sure to replace your_api_key_here with your valid OpenAI API key. You can obtain an API key from OpenAI.


## Usage:
**To start the chatbot in the terminal, run the following command**:

```bash
python -u shellsage.py
```

## Testing without an API key:
If you do not have an OpenAI API key or want to test the script with random mock responses, you can use the test.py file. This script will simulate random responses to demonstrate how the chatbot works.

**To use the test.py script, simply run:**

```bash
python -u test.py
```

In test.py, a function randomizes responses that do not make sense, but it allows you to see how the script works without needing a valid OpenAI API key.
