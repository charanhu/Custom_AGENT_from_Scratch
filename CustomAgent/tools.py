from duckduckgo_search import DDGS
from py_expression_eval import Parser
from datetime import datetime

# Initialize calculator
parser = Parser()


# DuckDuckGo search function
def search(search_term):
    search_result = ""
    with DDGS() as ddgs:
        results = ddgs.text(search_term, max_results=5)
        for result in results:
            search_result += result["body"] + " "
    return search_result


# Calculator function
def calculator(expression):
    return parser.parse(expression).evaluate({})


# DateTime function
def get_current_datetime(format_string=None):
    current = datetime.now()
    if format_string:
        try:
            return current.strftime(format_string)
        except ValueError:
            return str(current)
    return str(current)
