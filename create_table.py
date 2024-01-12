import psycopg2
import os
import dotenv




def create_table():
    
    conn = None
    delete_commands = ["""
                    DROP TABLE vendor;
                    """,
                    """
                    DROP TABLE products;
                    """,
                    """
                    DROP TABLE customers;
                    """
                    ]
    create_commands = ["""
            CREATE TABLE IF NOT EXISTS vendor (
                vendor_id SERIAL PRIMARY KEY,
                vendor_name VARCHAR(200) NOT NULL,
                industry VARCHAR(100)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS products(
                product_id SERIAL PRIMARY KEY,
                product_name VARCHAR(100) NOT NULL,
                description TEXT,
                vendor_id INT REFERENCES vendor(vendor_id)
                ON UPDATE CASCADE ON DELETE CASCADE
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS customers(
                customer_id SERIAL PRIMARY KEY,
                customer_name VARCHAR(50) NOT NULL,
                description TEXT,
                industry VARCHAR(50)
            );
            """
            ]
    try:
        dotenv.load_dotenv()
        conn = psycopg2.connect(
        host = os.getenv('DB_HOST'),
        database = os.getenv('DB_NAME'),
        user = os.getenv('DB_USER'),
        password = os.getenv('PASSWORD'),
        port = os.getenv('DB_PORT')
        )
        
        cursor = conn.cursor()
        
        # for command in delete_commands:
        #     cursor.execute(command)
        
        for command in create_commands:
            cursor.execute(command)
    
        cursor.close()
    
        conn.commit()
    
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            

if __name__ == '__main__':
    create_table()





