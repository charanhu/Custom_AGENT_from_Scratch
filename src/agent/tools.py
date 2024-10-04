from duckduckgo_search import DDGS
from py_expression_eval import Parser

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
    parser = Parser()
    return parser.parse(expression).evaluate({})
