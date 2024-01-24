import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

# MySQL database configuration
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Omganesha123!',
    'database': 'sample',
}

# Excel file path
excel_file_path = '/Users/harishsarvepalli/Downloads/people_analytics_start.xlsx'

# Read Excel file into a Pandas DataFrame
df = pd.read_excel(excel_file_path)


# Connect to MySQL database
conn = mysql.connector.connect(**db_config)

# Create a SQLAlchemy engine

engine = create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")
# Write DataFrame to MySQL
df.to_sql(name='Tables', con=engine, if_exists='replace', index=False,schema=db_config['database'])

# Close the MySQL connection
conn.close()





