from ._css_minifier import minify_css
from ._json_minifier import minify_json
from bs4 import BeautifulSoup, Comment
import re


def minify_html(html: str) -> str:
    """
    Minify HTML content.

    This function removes unnecessary whitespace, comments, and trailing slashes
    on void elements. It also minifies inline CSS and JSON-LD.

    Args:
        html (str): A string containing the HTML content.

    Returns:
        str: Minified HTML content.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Remove HTML comments.
    for comment in soup.findAll(text=lambda text: isinstance(text, Comment)):
        comment.extract()

    # Minify CSS within `<style>` tags.
    for style in soup.find_all("style"):
        minified_css = minify_css(style.string)
        style.string.replace_with(minified_css)

    # Minify JSON-LD within `<script>` tags.
    for script in soup.find_all("script", type="application/ld+json"):
        script.string.replace_with(minify_json(script.string))

    # Convert to a string.
    minified_html = soup.encode(formatter="html5").decode()

    # Collapse whitespace.
    minified_html = re.sub(r"\s+", " ", minified_html)

    return minified_html
