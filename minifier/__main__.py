import argparse
from pathlib import Path

from minifier import minify_file


def main() -> None:
    """Command-line interface for minifying website assets."""
    parser = argparse.ArgumentParser(
        prog="minifier",
        description=(
            "Minify website assets by removing unnecessary whitespace, "
            "comments, and other redundant content while preserving "
            "functionality."
        ),
    )
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        required=True,
        help="Input file",
        metavar="PATH",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        required=True,
        help="Output file",
        metavar="PATH",
    )
    args = parser.parse_args()

    minify_file(args.input, args.output)


if __name__ == "__main__":
    main()
