import time
from agent.stream_agent import stream_agent

if __name__ == "__main__":
    test_queries = [
        "How many 'e's are in the word 'openteexte'?",
        "What's the current temperature in New York City?",
        "Calculate 15% of 85",
        "What day of the week will it be 3 days from now?",
        "What's the most common letter in 'mississippi'?",
    ]

    for query in test_queries:
        print(f"\n\nQuery: {query}")
        stream_agent(query)
        time.sleep(2)  # Pause between queries
