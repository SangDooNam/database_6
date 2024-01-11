# psycopg2 CRUD

Using the `psycopg2` module create the following functions to manipulate the `suppliers` database:

  1. `update_vendor` which takes `vendor_id` and `**kwargs` as parameters:
      - Use the the `vendor_id` to identify the relevant record in the database.
      - depending on the `**kwargs` update the appropriate field for the record in the database.
      - return the updated row as a string.
    
  2. `create_customer`, which takes `customer_name` and `description` as parameters:
      - use the `customer_name` and `description` to create a new record in the table.
      - return the newly created row as a string.
    
  3. `delete_product`, which takes the `product_id` as a parameter:
      - Using the `product_id` delete the product from the database.
    
    
