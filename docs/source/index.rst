Welcome to Echo Logger's documentation!
====================================

Echo Logger is a Python utility package that provides enhanced logging and debugging capabilities with colorful console output, timing utilities, and integration with FeiShu messaging.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api
   examples

Features
--------

* Colored console output for different log levels (INFO, ERROR, DEBUG, WARNING)
* Function timing and profiling utilities
* JSON pretty printing and serialization
* Exception handling decorators
* FeiShu messaging integration
* Deprecation warnings
* Machine information logging

Quick Start
----------

.. code-block:: python

   from echo_logger import print_info, print_err, print_debug, print_warn

   # Print different types of messages
   print_info("This is an info message")
   print_err("This is an error message")
   print_debug("This is a debug message")
   print_warn("This is a warning message")

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search` 