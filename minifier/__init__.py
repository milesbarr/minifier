from ._css_minifier import minify_css
from ._html_minifier import minify_html
from ._json_minifier import minify_json
from ._xml_minifier import minify_xml
import os

__all__ = [
    "minify_css",
    "minify_html",
    "minify_json",
    "minify_xml",
    "minify_file",
    "minify_directory",
]

_MINIFY_BY_EXTENSION = {
    ".atom": minify_xml,
    ".css": minify_css,
    ".html": minify_html,
    ".json": minify_json,
    ".rss": minify_xml,
    ".svg": minify_xml,
    ".webmanifest": minify_json,
    ".xml": minify_xml,
}


def minify_file(filename: str | bytes | os.PathLike) -> None:
    _, ext = os.path.splitext(filename)
    minify = _MINIFY_BY_EXTENSION.get(ext)
    if not minify:
        return
    with open(filename, "r+") as f:
        s = f.read()
        minified = minify(s)
        if minified != s:
            f.seek(0)
            f.write(minified)
            f.truncate()


def minify_directory(path: str | bytes | os.PathLike) -> None:
    for root, _, files in os.walk(path):
        for filename in files:
            minify_file(os.path.join(root, filename))
