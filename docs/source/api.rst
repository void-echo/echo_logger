API Reference
============

Logging Functions
---------------

.. autofunction:: echo_logger.print_info
.. autofunction:: echo_logger.print_err
.. autofunction:: echo_logger.print_debug
.. autofunction:: echo_logger.print_warn

Decorators
---------

.. autofunction:: echo_logger.profile
.. autofunction:: echo_logger.try_catch
.. autofunction:: echo_logger.print_json
.. autofunction:: echo_logger.deprecated
.. autofunction:: echo_logger.no_problem
.. autofunction:: echo_logger.save_json

Utility Functions
---------------

.. autofunction:: echo_logger.calc_time
.. autofunction:: echo_logger.dumps_json

FeiShu Integration
----------------

.. autoclass:: echo_logger.FeiShuMessage
   :members:
   :undoc-members:
   :show-inheritance:

.. autofunction:: echo_logger.send_feishu
.. autofunction:: echo_logger.monit_feishu

Color Utilities
--------------

.. autoclass:: echo_logger._colors
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: echo_logger.ColorString
   :members:
   :undoc-members:
   :show-inheritance:

Constants
--------

.. data:: echo_logger.echo_logger_debug
   :annotation: bool

   Global debug flag that controls whether logging functions will output messages.

.. data:: echo_logger.log_sink
   :annotation: io.StringIO

   String buffer for collecting log messages. 