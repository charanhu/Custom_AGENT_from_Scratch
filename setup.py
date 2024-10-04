from setuptools import setup, find_packages

setup(
    name="ai_assistant_tools",
    version="0.1.0",
    author="Charan",
    description="An AI assistant that uses various tools to answer queries.",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "groq",
        "duckduckgo_search",
        "py_expression_eval",
    ],
    python_requires='>=3.8',
)