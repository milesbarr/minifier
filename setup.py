from setuptools import setup, find_packages

setup(
    name="minifier",
    version="1.0.0",
    description="A Python package to minify website assets.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/milesbarr/minifier",
    packages=find_packages(),
    install_requires=["beautifulsoup4"],
    entry_points={
        "console_scripts": [
            "minifier=minifier.__main__:main",
        ],
    },
    python_requires=">=3.10",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    keywords="website minifier minify minification html css xml json",
    test_suite="tests",
)
