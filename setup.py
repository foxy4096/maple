from setuptools import setup, find_packages

DESCRIPTION = "A package for making API Wrappers for Django Ninja or Fast API 🍁"

with open("README.md", "rb") as fh:
    LONG_DESCRIPTION = fh.read().decode("utf-16")

setup(
    name="maple",
    version="1.0",
    author="Aditya Priyadarshi",
    author_email="adityapriyadarshi669@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
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