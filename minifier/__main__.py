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
        "src",
        type=Path,
        required=True,
        help="Path to the source file",
        metavar="PATH",
    )
    parser.add_argument(
        "dst",
        type=Path,
        required=True,
        help="Path to the destination file",
        metavar="PATH",
    )
    args = parser.parse_args()

    minify_file(args.src, args.dst)


if __name__ == "__main__":
    main()
