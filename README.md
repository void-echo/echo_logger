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

# upgrade
pip install echo-logger --upgrade
```



## Demo

Simple usage:

```python
print_info("Hello World!")
print_warn("Hello World!")
print_err("Hello World!")
```

<img src="README.assets/image-20230529154733777.png" alt="image-20230529154733777" style="zoom: 67%;" />

If you want to print with time:

```python
print_info("Hello World!", with_time=True)
print_warn("Hello World!", with_time=True)
print_err("Hello World!", with_time=True)
```

<img src="README.assets/image-20230529155434474.png" alt="image-20230529155434474" style="zoom:67%;" />

If you want nothing to be printed (Let's say, you finished unit testing and want to run the whole program without any logger output):

```python
echo_logger.echo_logger_debug = False  # disable any logger functions from echo_logger
print_info("Hello World!")
print_warn("Hello World!")
print_err("Hello World!")
# No output at all.
```

Just so simple and straightforward. 
