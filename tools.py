from ddgs import DDGS


def calculator(operation: str, a: float, b: float) -> str:
    """
    Performs a basic math operation between two numbers.
    """
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return "Error: cannot divide by zero"
        result = a / b
    else:
        return f"Error: unknown operation '{operation}'"

    return str(result)


def web_search(query: str) -> str:
    """
    Searches the web for a given query.
    """
    if not isinstance(query, str) or not query.strip():
        return "Search error: query cannot be empty"

    try:
        results = DDGS().text(query.strip(), max_results=3)

        if not results:
            return "No results found."

        summary = ""

        for result in results:
            title = result.get("title", "Untitled result")
            body = result.get("body", "No summary available")
            summary += f"- {title}: {body}\n"

        return summary

    except Exception as e:
        return f"Search error: {e}"
