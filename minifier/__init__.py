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
    src: str | bytes | os.PathLike, dst: str | bytes | os.PathLike
) -> None:
    """Minify a file based on its extension.

    Args:
        src (str | bytes | os.PathLike): Path to the source file.
        dst (str | bytes | os.PathLike): Path to the destination file.

    Raises:
        ValueError: If the file extension is not supported.
        IOError: If there are issues reading or writing files.
    """
    src = Path(src)
    dst = Path(dst)

    # Get the minify function based on the file extension.
    minify = _MINIFY_BY_EXTENSION.get(src.suffix.lower())
    if not minify:
        raise ValueError(f"Unsupported file extension: {src.suffix}")

    # Read the contents from the source file.
    with src.open() as f:
        contents = f.read()

    # Minify the contents.
    contents = minify(contents)

    # Write the minified contents to destination file.
    with dst.open("w") as f:
        f.write(contents)
