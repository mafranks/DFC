import socket
import sqlite3

# Create empty dictionary to store the results
output = {}

# Connect to the database file
conn = sqlite3.connect('C:/Program Files/Cisco/AMP/nfm_cache.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Execute a SELECT statement to read data from a table
cur.execute('SELECT localip, remoteip FROM nfm_cache')

# Fetch all the results and print them
results = cur.fetchall()
for row in results:

    # Convert the decimals to byte strings
    #from_byte_string = abs(row[0]).to_bytes(4, byteorder='big')
    to_byte_string = abs(row[1]).to_bytes(4, byteorder='big')

    # Convert the byte string to an IP address string
    #from_ip_address = socket.inet_ntoa(from_byte_string)
    to_ip_address = socket.inet_ntoa(to_byte_string)
    
    if f"{to_ip_address}" in output:
        output[f"{to_ip_address}"] += 1
    else:
        output[f"{to_ip_address}"] = 1

# Close the cursor and database connection
cur.close()
conn.close()

# Sort dictionary by value
output_by_value = sorted(output.items(), key=lambda x: x[1], reverse=True)

# Print the results
print("Count - IP Address")
for entry in output_by_value:
    print(f"{entry[1]} - {entry[0]}")