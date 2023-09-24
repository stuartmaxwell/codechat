import os
from typing import Optional

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

conversation_history = []


def chat_with_openai(system_content: str, user_content: str) -> Optional[str]:
    """
    Send a message to the OpenAI chatcompletion API and receive a response from the
    assistant.

    This function maintains the conversation history, allowing for context-aware
    responses.

    Args:
        prompt (str): The message to send to the assistant.

    Returns:
        str: The assistant's response, or None if there was an error in the API call.
    """
    global conversation_history

    conversation_history.append({"role": "user", "content": user_content})

    data = {
        "messages": [
            {
                "role": "system",
                "content": system_content,
            }
        ]
        + conversation_history,
        "model": "gpt-3.5-turbo",
    }

    try:
        response_obj = openai.ChatCompletion.create(**data)
        response = response_obj.to_dict()  # type: ignore
        assistant_response = response["choices"][0]["message"]["content"]
        conversation_history.append(
            {"role": "assistant", "content": assistant_response}
        )
        return assistant_response
    except Exception as e:
        print("Error:", e)
        return None
