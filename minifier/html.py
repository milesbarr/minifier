import re

from bs4 import BeautifulSoup, Comment

from minifier.css import minify_css
from minifier.json import minify_json


def minify_html(s: str) -> str:
    """Minify an HTML string.

    Args:
        s (str): The HTML string to be minified.

    Returns:
        str: The minified HTML string.

    Raises:
        ValueError: If the input string is not valid HTML.
    """
    # Parse the HTML.
    try:
        soup = BeautifulSoup(s, "html.parser")
    except Exception as e:
        raise ValueError("Invalid HTML") from e

    # Remove comments.
    for comment in soup.find_all(string=lambda s: isinstance(s, Comment)):
        comment.extract()

    # Minify CSS within style tags.
    for style in soup.find_all("style"):
        style.string.replace_with(minify_css(style.string))

    # Minify JSON-LD within script tags.
    for script in soup.find_all("script", type="application/ld+json"):
        script.string.replace_with(minify_json(script.string))

    # Convert to a string.
    s = soup.encode(formatter="html5").decode()

    # Collapse whitespace.
    s = re.sub(r"\s+", " ", s)

    return s
