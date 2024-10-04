import re
from groq import Groq
from .tools import search, calculator
from config import SYSTEM_PROMPT
from dotenv import load_dotenv
load_dotenv()

# Initialize Groq client
client = Groq()

def get_streaming_response(messages):
    completion = client.chat.completions.create(
        model="llama-3.2-11b-text-preview",
        messages=messages,
        temperature=0,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    full_response = ""
    for chunk in completion:
        content = chunk.choices[0].delta.content or ""
        full_response += content
        print(content, end="")
    print()  # New line after response
    return full_response

def stream_agent(prompt):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ]

    def extract_action_and_input(text):
        action_pattern = r"Action: (.+?)\n"
        input_pattern = r"Action Input: \"(.+?)\""
        action = re.findall(action_pattern, text)
        action_input = re.findall(input_pattern, text)
        return action, action_input

    while True:
        response_text = get_streaming_response(messages)

        action, action_input = extract_action_and_input(response_text)

        if not action or not action_input:
            break

        if action[-1] == "Search":
            tool = search
        elif action[-1] == "Calculator":
            tool = calculator
        elif action[-1] == "DateTime":
            tool = get_current_datetime
        elif action[-1] == "Response To Human":
            break

        observation = tool(action_input[-1])
        print("\nObservation:", observation, "\n")

        messages.extend(
            [
                {"role": "assistant", "content": response_text},
                {"role": "user", "content": f"Observation: {observation}"},
            ]
        )
