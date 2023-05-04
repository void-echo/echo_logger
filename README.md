# Echo Logger

pip repo is [here](https://pypi.org/project/echo-logger/).

This is a simple echo logger for informative, warning and error messages.

Time and colored printing are supported.

This repository is mostly for my own use, but feel free to use it if you want.

## Usage

```python

# build (before you do this, don't forget to change the version id in setup.py)
python setup.py sdist bdist_wheel

# upload (before you do this, please rmv the outdated files of previous versions in dist/)
twine upload dist/*

# install
pip install echo-logger
```
