import json


def minify_json(s: str) -> str:
    """Minify a JSON string.

    Args:
        s (str): The JSON string to be minified.

    Returns:
        str: The minified JSON string.

    Raises:
        ValueError: If the input string is not valid JSON.
    """
    # Deserialize the JSON.
    try:
        obj = json.loads(s)
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON") from e
    
    # Serialize the JSON.
    return json.dumps(obj, separators=(",", ":"))
