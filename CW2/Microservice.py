import pyodbc

# Server connection information
server = "dist-6-505.uopnet.plymouth.ac.uk"
database = "COMP2001_JOsborneWalker"
username = "JOsborneWalker"
password = "SpqD287*"
driver = "{ODBC Driver 17 for SQL Server}"

# Set up the connection string
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Establish the connection
conn = pyodbc.connect(conn_str)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Read and execute the SQL commands from the SQL file
with open('setup.sql', 'r') as sql_file:
    sql_script = sql_file.read()

# Execute the SQL script
cursor.execute(sql_script)
conn.commit()

# Sample Data Insertion (You can add more as needed)
cursor.execute("""
-- Adding sample trail data
EXEC CW2.CreateTrail 
    @Trail_ID = 'PLY231',
    @Trail_Name = 'Plymouth WaterFront',
    @Trail_Length = 4.3,
    @Trail_Elevation_Change = 50.2,
    @Trail_Expected_Time = '01:30:00',
    @Trail_Description = 'PlymouthWaterfront Description';

EXEC CW2.CreateTrail
    @Trail_ID = 'NOX333',
    @Trail_Name = 'The Immortal Bastion',
    @Trail_Length = 3.0,
    @Trail_Elevation_Change = 40.1,
    @Trail_Expected_Time = '02:45:00',
    @Trail_Description = 'For The Glory of Noxus';
""")
conn.commit()

# Retrieving data from Trail table to confirm it's working
cursor.execute("SELECT * FROM CW2.Trail")
rows = cursor.fetchall()

# Printing out retrieved rows
for row in rows:
    print(row)

# Close the connection
conn.close()
