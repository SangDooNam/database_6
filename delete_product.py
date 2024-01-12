import psycopg2
import os
import dotenv

dotenv.load_dotenv()

def delete_product(product_id):
    conn = None
    command = """DELETE FROM products WHERE product_id = %s"""
    
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('PASSWORD'),
            port=os.getenv('DB_PORT')
        )
    
        cursor = conn.cursor()
        
        cursor.execute(command, product_id)
        
        conn.commit()
        
        cursor.close()
    
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    product_id='1'
    delete_product(product_id)