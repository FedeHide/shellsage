#!./venv/bin/python
from openai import OpenAI
import rich.table
import config
import typer
import rich

# configuration
CLIENT = OpenAI()
PRINT = rich.print
TABLE = rich.table.Table
PROMPT = typer.prompt


def chat_with_gpt_terminal():
    """
    Run a GPT-powered chatbot in the terminal until the user types 'exit'.
    """

    try:
        CLIENT.api_key = config.API_KEY
    except AttributeError:
        raise RuntimeError("API key not found. Ensure 'config.API_KEY' is defined.")

    # assistant context
    context = {"role": "system", "content": "You are a helpful assistant."}
    messages = [context]

    PRINT("[bold green]Welcome to the chatbot![/bold green]")

    table = TABLE("Command", "Description")
    table.add_row("exit", "Exit the chatbot")
    table.add_row("new", "Start a new conversation")
    PRINT(table)

    while True:
        # user input
        content = __prompt()

        if content.lower() == "new":
            messages = [context]
            PRINT("\n🆕 [bold blue]New conversation started.[/bold blue]")
            continue

        # add user's message to the context
        messages.append({"role": "user", "content": content})

        try:
            # generate completion
            completion = CLIENT.chat.completions.create(
                model="gpt-4o-mini",
                store=True,
                messages=messages,
                max_tokens=150,
            )
        except Exception as e:
            PRINT(f"Error during API call: {e}")
            continue

        # extract assistant's response
        response_content = completion.choices[0].message.content
        messages.append({"role": "assistant", "content": response_content})

        PRINT(f"[bold green]> [/bold green] [green]{response_content}[/green]")


def __prompt() -> str:
    prompt = PROMPT("\n💬 Send a message to the chatbot")

    if prompt.lower() == "exit":
        exit = typer.confirm("⚠️ Are you sure you want to exit?", default=True)
        if exit:
            PRINT("👋 Goodbye!")
            raise typer.Exit()

        return __prompt()

    return prompt


if __name__ == "__main__":
    typer.run(chat_with_gpt_terminal)

# execute with python -u main.py
