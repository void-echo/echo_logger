Usage Guide
===========

Basic Logging
------------

Echo Logger provides several functions for different log levels, each with colored output:

.. code-block:: python

   from echo_logger import print_info, print_err, print_debug, print_warn

   # Basic logging
   print_info("This is an info message")
   print_err("This is an error message")
   print_debug("This is a debug message")
   print_warn("This is a warning message")

   # Logging without timestamp
   print_info("Message without timestamp", with_time=False)

Function Timing
--------------

Use the ``@profile`` decorator to measure function execution time:

.. code-block:: python

   from echo_logger import profile

   @profile
   def my_function():
       # Your code here
       pass

Exception Handling
----------------

The ``@try_catch`` decorator provides automatic exception handling:

.. code-block:: python

   from echo_logger import try_catch

   @try_catch
   def risky_function():
       # Your code here
       pass

JSON Handling
------------

Pretty print JSON data using the ``@print_json`` decorator:

.. code-block:: python

   from echo_logger import print_json

   @print_json
   def get_data():
       return {"key": "value"}

FeiShu Integration
----------------

Send messages to FeiShu:

.. code-block:: python

   from echo_logger import send_feishu

   # Send a simple message
   send_feishu(
       title_="Test Message",
       content_="This is a test message",
       url_="your_webhook_url"
   )

   # Send with machine information
   send_feishu(
       title_="System Alert",
       content_="System is running low on memory",
       url_="your_webhook_url",
       with_machine_info=True
   )

Monitoring with FeiShu
---------------------

Use the ``@monit_feishu`` decorator to monitor function execution:

.. code-block:: python

   from echo_logger import monit_feishu

   @monit_feishu(
       title_ok="Function completed successfully",
       content_ok="The function ran without errors",
       url_="your_webhook_url",
       title_err="Function failed",
       content_err="An error occurred during execution"
   )
   def monitored_function():
       # Your code here
       pass

Deprecation Warnings
-------------------

Mark functions as deprecated using the ``@deprecated`` decorator:

.. code-block:: python

   from echo_logger import deprecated

   @deprecated
   def old_function():
       # This function is deprecated
       pass 