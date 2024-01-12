import psycopg2
import os
import dotenv

def update_vendor(updates):
    
    conn = None
    command = """
            UPDATE vendor 
            SET vendor_name = %s,
                industry = %s
            WHERE vendor_id = %s;
            """
    try:
        dotenv.load_dotenv()
        conn = psycopg2.connect(
            post = os.getenv('DB_POST'),
            database = os.getenv('DB_NAME'),
            user = os.getenv('DB_USER'),
            password = os.getenv('PASSWORD'),
            port = os.getenv('DB_PORT')
        )
        
        cursor = conn.cursor()
        
        def updating(**kwargs):
            cursor.execute(command, tuple(kwargs.values()))

        for update in updates:
            updating(**update)
        
        cursor.execute('SELECT * FROM vendor WHERE vendor_id < 5;')
        rows = cursor.fetchall()
        
        for row in rows:
            print(f'The row has been updated:\n  - Vendor ID: {row[0]}\n  - Vendor Name: {row[1]}\n  - Industry: {row[2]}')
        
        cursor.close()
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()


updates = [
    {
    'vendor_name':'TechGuru Solutions',
    'industry':'Technology',
    'vendor_id': 1
    },
    {
    'vendor_name':'HealthMax Pharmaceuticals',
    'industry':'Healthcare',
    'vendor_id': 2
    },
    {
    'vendor_name':'BuildRight Contruction',
    'industry':'Construction',
    'vendor_id': 3
    },
    {
    'vendor_name':'Retail Roundup',
    'industry':'Retail',
    'vendor_id': 4
    }
]


if __name__ == '__main__':
    update_vendor(updates)