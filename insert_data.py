import psycopg2
import os
import dotenv



def insert_data_into_vendor():
    
    conn = None
    
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
        command = """
                    INSERT INTO vendor 
                    (vendor_name,
                    industry)
                    VALUES
                    (%s, %s);
                """
        parameters = [
            ('TechGuru Solutions', 'Technology'),
            ('HealthMax Pharmaceuticals', 'Healthcare'),
            ('BuildRight Construction', 'Construction'),
            ('Retail Roundup', 'Retail'),
            ('Innovatech Electronics', 'Technology'),
            ('UrbanStruct Builders', 'Construction'),
            ('MarketPlace Essentials', 'Retail')
        ]
        def exists(parameter):
            cursor.execute('SELECT * FROM vendor WHERE vendor_name = %s AND industry = %s' , (parameter[0], parameter[1]))
            return cursor.fetchone() is not None
        
        for parameter in parameters:
            if not exists(parameter):
                cursor.execute(command, parameter)
        
        cursor.close()
        
        conn.commit()
        
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()


def insert_data_into_products():
    conn = None
    command = """INSERT INTO products (
        product_name,
        description,
        vendor_id
        ) VALUES
        (%s,%s,%s);
        """
    parameters = [
            ('Laptop Pro', 'High-performance laptop with extended battery life', 1),
            ('Pain Reliever', 'Effective for headache and muscular pain', 2),
            ('Wireless Earbuds', 'Noise-cancelling, long-lasting wireless earbuds', 3),
            ('Vitamin Supplements', 'Multivitamins for daily health maintenance', 4),
            ('Smartwatch 4.0', 'Latest generation smartwatch with health tracking', 5),
            ('Skin Cream', 'Dermatologically tested skin cream for sensitive skin', 6),
            ('4K LED Monitor', 'Ultra-high-definition computer monitor', 7),
            ('Antiseptic Solution', 'Safe and effective for cuts and wounds', 2)
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
        
        def exists(parameter):
            cursor.execute("""SELECT * FROM products 
                        WHERE product_name = %s 
                        AND description = %s
                        AND vendor_id = %s""", 
                        (parameter[0],parameter[1],parameter[2])
                        )
            return cursor.fetchone() is not None
        
        for parameter in parameters:
            if not exists(parameter):
                cursor.execute(command, parameter)
        
        cursor.close()
        conn.commit()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_data_into_customers():
    
    conn = None
    command = """
            INSERT INTO
            customers
            (customer_name, description, industry)
            VALUES
            (%s, %s, %s)
            """
    parameters = [
    ('Tom Bread', 'Pioneering new technology solutions', 'Technology'),
    ('Susan Palm', 'Dedicated to advancing healthcare', 'Healthcare'),
    ('Tilda Doll', 'Building the future, one project at a time', 'Construction'),
    ('Hans Bill', 'At the forefront of retail innovation', 'Retail'),
    ('Rilra Troll', 'Leading developer in tech industry', 'Technology'),
    ('Mukashi Shiro', 'Revolutionizing retail experiences', 'Retail'),
    ('Dongki Kim', 'Committed to healthcare excellence', 'Healthcare')
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
        
        def exists(parameter):
            cursor.execute('SELECT * FROM customers WHERE customer_name = %s AND industry = %s', (parameter[0],parameter[1]))
            return cursor.fetchone() is not None
        
        for parameter in parameters:
            if not exists(parameter):
                cursor.execute(command, parameter)
        
        cursor.close()
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    insert_data_into_vendor()
    insert_data_into_products()
    insert_data_into_customers()


