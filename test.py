#!./venv/bin/python
import openai
import rich.table
import config
import typer
import rich
import random

# configuration
PRINT = rich.print
TABLE = rich.table.Table
PROMPT = typer.prompt


def simulate_chat_completion(messages):
    """
    Simulates a chat completion response based on user input.
    """
    user_message = messages[-1]["content"]
    responses = [
        f"I see you said: {user_message}",
        "Interesting point! Can you elaborate?",
        "I'm just a simulated assistant, but that sounds great!",
        "Can you tell me more about that?",
        "That sounds fascinating! Let’s dive deeper.",
    ]
    return {"choices": [{"message": {"content": random.choice(responses)}}]}


def chat_with_gpt_terminal(simulate: bool = True):
    """
    Run a GPT-powered chatbot in the terminal until the user types 'exit'.
    """
    try:
        if not simulate:
            openai.api_key = config.API_KEY
    except AttributeError:
        raise RuntimeError("API key not found. Ensure 'config.API_KEY' is defined.")

    context = {"role": "system", "content": "You are a helpful assistant."}
    messages = [context]

    PRINT("[bold green]Welcome to the chatbot![/bold green]")

    table = TABLE("Command", "Description")
    table.add_row("exit", "Exit the chatbot")
    table.add_row("new", "Start a new conversation")
    PRINT(table)

    while True:
        content = __prompt()

        if content.lower() == "new":
            messages = [context]
            PRINT("\n🆕 [bold blue]New conversation started.[/bold blue]")
            continue

        messages.append({"role": "user", "content": content})

        try:
            if simulate:
                completion = simulate_chat_completion(messages)
            else:
                completion = openai.ChatCompletion.create(
                    model="gpt-4o-mini",
                    messages=messages,
                    max_tokens=150,
                )
        except Exception as e:
            if "insufficient_quota" in str(e):
                PRINT(
                    "[bold red]⚠️ Insufficient quota: Check your OpenAI API plan or usage details.[/bold red]"
                )
            else:
                PRINT(f"[bold red]⚠️ Unexpected error:[/bold red] {e}")
            continue

        response_content = completion["choices"][0]["message"]["content"]
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
    typer.run(lambda: chat_with_gpt_terminal(simulate=True))
