Examples
========

Basic Logging Example
-------------------

.. code-block:: python

   from echo_logger import print_info, print_err, print_debug, print_warn

   def process_data(data):
       print_info("Starting data processing")
       
       if not data:
           print_err("No data provided")
           return
           
       print_debug(f"Processing {len(data)} items")
       
       try:
           # Process data
           result = [x * 2 for x in data]
           print_info("Data processing completed successfully")
           return result
       except Exception as e:
           print_err(f"Error during processing: {str(e)}")
           return None

Function Profiling Example
------------------------

.. code-block:: python

   from echo_logger import profile
   import time

   @profile
   def complex_calculation():
       print("Starting calculation...")
       time.sleep(1)  # Simulate work
       result = sum(i * i for i in range(1000))
       print("Calculation completed")
       return result

   # The execution time will be automatically logged
   result = complex_calculation()

JSON Handling Example
-------------------

.. code-block:: python

   from echo_logger import print_json, dumps_json

   @print_json
   def get_user_data():
       return {
           "user": {
               "name": "John Doe",
               "email": "john@example.com",
               "preferences": {
                   "theme": "dark",
                   "notifications": True
               }
           }
       }

   # The JSON will be automatically pretty-printed
   user_data = get_user_data()

   # Manual JSON formatting
   formatted_json = dumps_json(user_data, indent=2, depth=3)
   print(formatted_json)

FeiShu Integration Example
------------------------

.. code-block:: python

   from echo_logger import send_feishu, monit_feishu

   # Simple message
   send_feishu(
       title_="System Status",
       content_="All systems operational",
       url_="your_webhook_url"
   )

   # Monitoring a critical function
   @monit_feishu(
       title_ok="Backup Completed",
       content_ok="Database backup finished successfully",
       url_="your_webhook_url",
       title_err="Backup Failed",
       content_err="Database backup encountered an error"
   )
   def perform_backup():
       # Backup logic here
       pass

Error Handling Example
--------------------

.. code-block:: python

   from echo_logger import try_catch, print_err

   @try_catch
   def process_file(filename):
       with open(filename, 'r') as f:
           data = f.read()
       return data

   # The function will handle any exceptions and log them
   result = process_file("nonexistent.txt")
   if result is None:
       print_err("Failed to process file")

Combined Example
--------------

.. code-block:: python

   from echo_logger import (
       print_info, print_err, profile,
       try_catch, monit_feishu
   )

   @monit_feishu(
       title_ok="Data Processing Complete",
       content_ok="Successfully processed all records",
       url_="your_webhook_url",
       title_err="Processing Error",
       content_err="Failed to process data"
   )
   @profile
   @try_catch
   def process_records(records):
       print_info(f"Processing {len(records)} records")
       
       results = []
       for i, record in enumerate(records, 1):
           try:
               # Process each record
               processed = record * 2
               results.append(processed)
               print_info(f"Processed record {i}/{len(records)}")
           except Exception as e:
               print_err(f"Error processing record {i}: {str(e)}")
               continue
               
       return results 