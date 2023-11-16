import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="echo_logger",
    version="0.0.7",
    author="Echo Void",
    author_email="void-echo@outlook.com",
    description="A simple logger for python, with color and time",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/void-echo/echo_logger/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
)
