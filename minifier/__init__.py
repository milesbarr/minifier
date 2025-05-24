import os
from pathlib import Path

from minifier.css import minify_css
from minifier.html import minify_html
from minifier.json import minify_json
from minifier.xml import minify_xml


__all__ = [
    "minify_css",
    "minify_html",
    "minify_json",
    "minify_xml",
    "minify_format",
    "minify_file",
    "minify_dir",
]

_MINIFY_BY_EXTENSION = {
    ".atom": minify_xml,
    ".css": minify_css,
    ".htm": minify_html,
    ".html": minify_html,
    ".json": minify_json,
    ".rss": minify_xml,
    ".svg": minify_xml,
    ".webmanifest": minify_json,
    ".xhtml": minify_html,
    ".xml": minify_xml,
}


def minify_format(s: str, format: str) -> str:
    """Minify a string based on the format.

    Args:
        s (str): The string to minify
        format (str): The format of the string

    Returns:
        str: Minified string

    Raises:
        ValueError: If the format is not supported
    """
    ext = "." + format.lower().removeprefix(".")
    minify = _MINIFY_BY_EXTENSION.get(ext, lambda s: s)
    if not minify:
        raise ValueError(f"Unsupported format: {format}")
    return minify(s)


def minify_file(
    input_file: str | bytes | os.PathLike,
    output_file: str | bytes | os.PathLike,
) -> None:
    """Minify a file based on its extension.

    Args:
        input_file (str | bytes | os.PathLike): Path to the input file
        output_file (str | bytes | os.PathLike): Path to the output file

    Raises:
        ValueError: If the file extension is not supported
        IOError: If there are issues reading or writing files
    """
    input_file = Path(input_file)
    output_file = Path(output_file)
    minify = _MINIFY_BY_EXTENSION.get(input_file.suffix.lower())
    if not minify:
        raise ValueError(f"Unsupported file extension: {input_file.suffix}")
    with input_file.open() as f:
        content = f.read()
    content = minify(content)
    with output_file.open("w") as f:
        f.write(content)
