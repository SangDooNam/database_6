import psycopg2
import os
import dotenv

dotenv.load_dotenv()

def create_customers(customer_name, description):
    
    conn = None
    create_command = """
        CREATE TABLE IF NOT EXISTS customers (
            customer_id SERIAL PRIMARY KEY,
            customer_name VARCHAR(50) NOT NULL,
            description TEXT,
            industry VARCHAR(50)
        );
    """
    insert_command ="""
            INSERT INTO customers(
                customer_name,
                description
            )
            VALUES(%s, %s)
            RETURNING customer_id;
        """
    try:
        conn = psycopg2.connect(
            host = os.getenv('DB_HOST'),
            database = os.getenv('DB_NAME'),
            user = os.getenv('DB_USER'),
            password = os.getenv('PASSWORD'),
            port = os.getenv('DB_PORT')
        )
            
        cursor = conn.cursor()
        
        cursor.execute(create_command)
        
        cursor.execute(insert_command, (customer_name, description))
        new_customer_id = cursor.fetchone()[0]
        conn.commit()
        cursor.execute(f'SELECT customer_id, customer_name, description FROM customers WHERE customer_id = {new_customer_id};')
        row = cursor.fetchone()
        return f'The row has been created:\n  - Customer ID: {row[0]}\n  - Customer Name: {row[1]}\n  - Description: {row[2]}'
        
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()


    
if __name__ == '__main__':
    customer_name, description = 'Andro', 'Technology'
    print(create_customers(customer_name, description))

