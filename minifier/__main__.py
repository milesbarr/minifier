import argparse
from pathlib import Path

from . import minify_file, minify_directory


def main() -> None:
    parser = argparse.ArgumentParser(description="Minifies website assets.")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    if args.path.is_file():
        minify_file(args.path)
    else:
        minify_directory(args.path)


if __name__ == "__main__":
    main()
