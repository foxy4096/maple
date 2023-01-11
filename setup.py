from setuptools import setup, find_packages

DESCRIPTION = "A package for making API Wrappers for Django Ninja or Fast API 🍁"

from pathlib import Path

current_dir = Path(__file__).parent
LONG_DESCRIPTION = (current_dir / "README.md").read_text(encoding="utf-16")

setup(
    name="maple",
    version="1.0",
    author="Aditya Priyadarshi",
    author_email="adityapriyadarshi669@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/foxy4096/maple",
    packages=find_packages(),
    install_requires=["setuptools_scm", "requests"],
    keywords=["python", "API"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
