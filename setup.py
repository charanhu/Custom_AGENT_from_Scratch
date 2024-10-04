from setuptools import setup, find_packages

setup(
    name="CustomAgent",
    version="0.1.0",
    description="A streaming AI agent with search and calculator tools",
    author="Charan",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "groq",
        "duckduckgo_search",
        "py_expression_eval",
    ],
    python_requires='>=3.12',
)
