import pyodbc

# data
server = "dist-6-505.uopnet.plymouth.ac.uk"
database = "COMP2001_JOsborneWalker"
username = "JOsborneWalker"
password = "SpqD287*"
driver = '{ODBC Driver 17 for SQL Server}'


# connection string
conn_str = (
    f'DRIVER={driver};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
    'Encrypt=Yes;'
    'TrustServerCertificate=Yes;'
    'Connection Timeout=30;'
    'Trusted_Connection=No'
)



@app.route('/trails', methods=['GET'])
def get_trails():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Hiking.Trails")
    trails = [
        {
            "TrailID": row.TrailID,
            "TrailName": row.TrailName,
            "Difficulty": row.Difficulty,
            "Location": row.Location,
            "Length": row.Length,
            "ElevationGain": row.ElevationGain,
            "RouteType": row.RouteType,
            "TrailSummary": row.TrailSummary,
            "TrailDescription": row.TrailDescription
        }
        for row in cursor.fetchall()
    ]
    conn.close()
    return jsonify(trails)