Installation
============

Requirements
-----------

* Python 3.6 or higher
* pip (Python package installer)

Installation Methods
------------------

Using pip
~~~~~~~~

The recommended way to install Echo Logger is using pip:

.. code-block:: bash

   pip install echo-logger

From Source
~~~~~~~~~~

You can also install from source:

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/yourusername/echo_logger.git
      cd echo_logger

2. Install the package:

   .. code-block:: bash

      pip install -e .

Dependencies
-----------

The package has the following dependencies:

* loguru
* requests

These will be automatically installed when you install Echo Logger using pip.

Verifying Installation
--------------------

To verify that Echo Logger is installed correctly, you can run Python and import the package:

.. code-block:: python

   >>> from echo_logger import print_info
   >>> print_info("Echo Logger is installed!") 