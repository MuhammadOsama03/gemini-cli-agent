from ddgs import DDGS


MAX_SEARCH_QUERY_LENGTH = 500
MAX_SEARCH_RESULT_LENGTH = 4_000

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
    clean_query = query.strip()
    if len(clean_query) > MAX_SEARCH_QUERY_LENGTH:
        return f"Search error: query cannot exceed {MAX_SEARCH_QUERY_LENGTH} characters"

    try:
        results = DDGS().text(clean_query, max_results=3)

        if not results:
            return "No results found."

        lines = []
        for result in results:
            title = result.get("title", "Untitled result")
            body = result.get("body", "No summary available")
            lines.append(f"- {title}: {body}")

        summary = "\n".join(lines)
        if len(summary) > MAX_SEARCH_RESULT_LENGTH:
            return summary[: MAX_SEARCH_RESULT_LENGTH - 14].rstrip() + "\n[truncated]"
        return summary

    except Exception as e:
        return f"Search error: {e}"
