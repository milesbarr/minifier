import os
from pathlib import Path

from .css import minify_css
from .html import minify_html
from .json import minify_json
from .xml import minify_xml


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
        s (str): The string to minify.
        format (str): The format of the string.

    Returns:
        str: The minified string.

    Raises:
        ValueError: If the format is not supported.
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
        input_file (str | bytes | os.PathLike): Path to the input file.
        output_file (str | bytes | os.PathLike): Path to the output
            file.

    Raises:
        ValueError: If the file extension is not supported.
        IOError: If there are issues reading or writing files.
    """
    input_file = Path(input_file)
    output_file = Path(output_file)

    # Get the minify function based on the file extension.
    minify = _MINIFY_BY_EXTENSION.get(input_file.suffix.lower())
    if not minify:
        raise ValueError(f"Unsupported file extension: {input_file.suffix}")

    # Read the contents from the input file.
    with input_file.open() as f:
        contents = f.read()
    
    # Minify the contents.
    contents = minify(contents)

    # Write the minified contents to output file.
    with output_file.open("w") as f:
        f.write(contents)
