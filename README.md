# Minifier

A Python tool for minifying website assets by removing unnecessary whitespace,
comments, and other redundant content while preserving functionality.

## Features

Supports minification of common web file formats:

- HTML (`.html`, `.htm`, `.xhtml`)
- CSS (`.css`)
- JSON (`.json`, `.webmanifest`)
- XML (`.xml`, `.rss`, `.atom`, `.svg`)

All minification preserves full functionality while reducing file size.

## Installation

```bash
# Clone the repository
git clone https://github.com/milesbarr/minifier.git
cd minifier

# Install the package
pip install .
```

## Usage

### Command-Line Interface

Minify a file:
```bash
python -m minifier -i input.html -o output.html
```

## License

This project is licensed under the [MIT license](LICENSE).
