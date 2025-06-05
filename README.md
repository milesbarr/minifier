# Minifier

A Python tool for minifying website assets by removing unnecessary whitespace,
comments, and other redundant content while preserving functionality. Ideal for
web developers looking to optimize site performance.

## Features

- Minifies common web file formats: HTML, CSS, JSON, and XML
- Preserves full functionality while reducing file size
- Simple command-line interface
- Can be used as a Python library
- Fast and lightweight, with minimal dependencies

## Supported Formats

- HTML (`.html`, `.htm`, `.xhtml`)
- CSS (`.css`)
- JSON (`.json`, `.webmanifest`)
- XML (`.xml`, `.rss`, `.atom`, `.svg`)

## Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/milesbarr/minifier@main
```

Or clone the repository and install locally:

```bash
git clone https://github.com/milesbarr/minifier.git
cd minifier
pip install .
```

## Usage

### Command-Line Interface

Minify a file:

```bash
python -m minifier -i input.html -o output.html
```

### Python API

Minify a file:

```python
from minifier import minify_file

minify_file("input.html", "output.html")
```

## License

This project is licensed under the [MIT License](LICENSE).
